"""Verify the branded business editions and render every page for review."""
from pathlib import Path
import re,json
from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parents[1]
reports=[]
for name,images in [('Engineering_Impact_Framework_Whitepaper',5),('Engineering_Impact_Framework_Workbook',2),('Engineering_Impact_Framework_Java_Workflow',3)]:
    path=ROOT/'outputs'/(name+'.docx');d=Document(path)
    assert d.core_properties.author=='Paul Harding'
    assert len(d.inline_shapes)==images
    assert d.styles['Normal'].font.name=='Calibri'
    normal_size=d.styles['Normal'].font.size
    if normal_size is None:
        defaults=d.styles.element.xpath('./w:docDefaults/w:rPrDefault/w:rPr/w:sz')
        assert defaults and int(defaults[0].get(qn('w:val')))==22
    else:assert normal_size.pt==11
    assert all(abs(getattr(s,x).inches-.75)<.001 for s in d.sections for x in ['top_margin','bottom_margin','left_margin','right_margin'])
    texts=[p.text for p in d.paragraphs]
    assert 'Paul Harding, MBA ITM' in texts
    assert any('PolarSpark LLC' in x for x in texts)
    assert any('https://polarspark.com/' in x for x in texts)
    assert 'PolarSpark LLC' in d.sections[0].header.paragraphs[0].text
    assert 'Harding' not in d.sections[0].header.paragraphs[0].text
    ref_start=texts.index('References and source notes')
    entries=[x for x in texts[ref_start+1:] if re.match(r'^\[\d+\]',x)]
    refids={int(re.match(r'^\[(\d+)\]',x).group(1)) for x in entries}
    assert len(entries)==len(refids)
    body='\n'.join(texts[:ref_start])+'\n'+'\n'.join(c.text for t in d.tables for r in t.rows for c in r.cells)
    for ids in re.findall(r'\[(\d+(?:,\s*\d+)*)\]',body):
        assert set(map(int,ids.split(',')))<=refids,ids
    if name.endswith('Whitepaper'):
        assert len(d.tables)==15
        assert all(re.search(r'\bM'+str(i).zfill(2)+r'\b',body) for i in range(1,29))
        assert 'Executive summary' in texts and 'Contents' in texts
    elif name.endswith('Workbook'):
        assert len(d.tables)==24
        assert all('T'+str(i).zfill(2) in body for i in range(1,13))
    pdf=ROOT/'tmp/qa'/name/(name+'.pdf')
    reader=PdfReader(pdf);pd=pdfium.PdfDocument(str(pdf))
    if name.endswith('Java_Workflow'):assert len(pd)==20,len(pd)
    review=pdf.parent/'review';review.mkdir(exist_ok=True)
    index=[];overflow=[]
    for i in range(len(pd)):
        page=pd[i];page.render(scale=1).to_pil().convert('RGB').save(review/f'page-{i+1}.png')
        tp=page.get_textpage()
        for j in range(tp.count_chars()):
            char=tp.get_text_range(j,1)
            if not char.strip():continue
            l,b,r,t=tp.get_charbox(j)
            if b<40 or t>750:continue
            if l<52 or r>560 or b<51 or t>740:overflow.append((i+1,char,[l,b,r,t]))
        text=reader.pages[i].extract_text() or ''
        assert len(text.split())>20,(i+1,'Unexpected sparse page')
        index.append({'page':i+1,'words':len(text.split()),'first':text.splitlines()[:2],'last':text.splitlines()[-2:]})
    assert not overflow,overflow[:20]
    (pdf.parent/'extracted.txt').write_text('\n\n'.join(p.extract_text() or '' for p in reader.pages),encoding='utf-8')
    report={'file':path.name,'pages':len(pd),'references':len(entries),'body_images':images,'overflow':len(overflow),'index':index}
    reports.append(report);print({k:v for k,v in report.items() if k!='index'})
(ROOT/'tmp/business_verification.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
