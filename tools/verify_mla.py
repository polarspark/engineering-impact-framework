from pathlib import Path
import re,json
from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader
import pypdfium2 as pdfium

root=Path(__file__).resolve().parents[1]
reports=[]
for name,expected_figures in [('Engineering_Impact_Framework_MLA',4),('Engineering_Impact_Framework_Templates_MLA',1),('Engineering_Impact_Framework_Java_Workflow_MLA',2)]:
    path=root/'outputs'/(name+'.docx')
    d=Document(path)
    assert d.core_properties.author=='Paul Harding'
    assert len(d.inline_shapes)==expected_figures
    assert d.styles['Normal'].font.name=='Times New Roman'
    assert d.styles['Normal'].font.size.pt==12
    assert all(abs(getattr(s,x).inches-1)<.001 for s in d.sections for x in ['top_margin','bottom_margin','left_margin','right_margin'])
    assert d.sections[0].header.paragraphs[0].text.startswith('Harding ')
    all_text=' '.join(d.element.body.itertext())
    assert not re.search(r'\[S\d',all_text)
    assert 'Zhao' not in all_text
    assert '**' not in all_text
    assert 'Works Cited' in all_text
    assert d.paragraphs[0].text=='Paul Harding, MBA ITM'
    assert d.paragraphs[1].text=='PolarSpark LLC'
    works=next(i for i,p in enumerate(d.paragraphs) if p.text=='Works Cited')
    entries=d.paragraphs[works+1:]
    assert entries
    for p in entries:
        assert abs(p.paragraph_format.left_indent.inches-.5)<.001
        assert abs(p.paragraph_format.first_line_indent.inches+.5)<.001
        assert (p.paragraph_format.line_spacing or p.style.paragraph_format.line_spacing)==2
    for t in d.tables:
        assert t.rows[0]._tr.xpath('./w:trPr/w:tblHeader')
        for row in t.rows:
            for c in row.cells:
                for p in c.paragraphs:
                    assert (p.paragraph_format.line_spacing or p.style.paragraph_format.line_spacing)==2
                    assert all((r.font.size or p.style.font.size).pt==12 and (r.font.name or p.style.font.name)=='Times New Roman' for r in p.runs)
    for rel in d.part.rels.values():
        if rel.reltype.endswith('/hyperlink'): assert rel.target_ref.startswith('https://')
    pdf=root/'tmp'/'qa'/name/(name+'.pdf')
    reader=PdfReader(pdf)
    if 'Java_Workflow' in name:
        assert len(reader.pages)==20, 'Java workflow must have twenty pages'
        assert all(k in all_text for k in ['JUnit','Maven','Spring Boot','M01','M02','M03','Govern','Map','Measure','Manage'])
    # Preserve a full-page render at 72 dpi for a normal-size page review.
    pd=pdfium.PdfDocument(str(pdf))
    review=pdf.parent/'review'; review.mkdir(exist_ok=True)
    pages=[]; overflow=[]
    for i in range(len(pd)):
        page=pd[i]
        page.render(scale=1).to_pil().convert('RGB').save(review/f'page-{i+1}.png')
        tp=page.get_textpage()
        for j in range(tp.count_chars()):
            ch=tp.get_text_range(j,1)
            if not ch.strip(): continue
            l,b,r,t=tp.get_charbox(j)
            if b>730: continue # MLA running head.
            if l<70 or r>542 or b<69 or t>722:
                overflow.append({'page':i+1,'char':ch,'box':[l,b,r,t]})
        text=reader.pages[i].extract_text() or ''
        assert len(text.split())>8, (name,i+1,'unexpected empty page')
        pages.append({'page':i+1,'words':len(text.split()),'first':' / '.join(text.splitlines()[:2])})
    assert not overflow,overflow[:15]
    reports.append({'file':path.name,'pages':len(pd),'sources':len(entries),'figures':len(d.inline_shapes),'body_overflow':len(overflow),'page_index':pages})
(root/'tmp'/'mla_verification.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
for report in reports:
    print({k:v for k,v in report.items() if k!='page_index'})
