from pathlib import Path
from docx import Document
from pypdf import PdfReader
import re
import json

root = Path(__file__).resolve().parents[1]
main = Document(root/'outputs/Engineering_Impact_Framework.docx')
forms = Document(root/'outputs/Engineering_Impact_Framework_Templates.docx')
assert len(main.inline_shapes)==4
assert len(forms.inline_shapes)==1
for doc in [main,forms]:
    assert doc.core_properties.title.startswith('Engineering Impact Framework')
    assert 'AI and SDLC Adoption Value Framework' not in '\n'.join(p.text for p in doc.paragraphs)
    for picture in doc.inline_shapes:
        assert picture._inline.docPr.get('descr')
ids = [re.match(r'M([0-9]{2}) ', p.text).group(1) for p in main.paragraphs
       if p.style.name == 'Heading 2' and re.match(r'M[0-9]{2} ',p.text)]
assert ids == [f'{i:02}' for i in range(1,29)], ids
template_ids = {re.match(r'(T[0-9]{2}) ',p.text).group(1) for p in forms.paragraphs
                if p.style.name == 'Heading 1' and re.match(r'T[0-9]{2} ',p.text)}
assert template_ids == {f'T{i:02}' for i in range(1,13)}
assert (800/40-640/40)*40 == 160
assert 160*100 == 16000
assert 12000+18000 == 30000
assert 6000+8000+8000+2000 == 24000
assert (30000-24000)/24000*100 == 25
assert (8-10)-(9.5-10) == -1.5
assert round(11/(4*5)*100,1) == 55.0
assert round(5/6*100,1) == 83.3
assert round((18000-28000)/28000*100,1) == -35.7
assert round((42000-22000)/22000*100,1) == 90.9
assert round(2/12*100,1) == 16.7
for doc in [main, forms]:
    text = '\n'.join(p.text for p in doc.paragraphs)
    assert '\u2014' not in text
    assert '**' not in text
    for p in doc.paragraphs:
        if p.style.name.startswith('Heading') or p.style.name == 'Title':
            assert re.fullmatch(r'[A-Za-z0-9 ]+',p.text),p.text
    for t in doc.tables:
        assert t.rows[0]._tr.xpath('./w:trPr/w:tblHeader')
    for rel in doc.part.rels.values():
        if rel.reltype.endswith('/hyperlink'):
            assert str(rel.target_ref).startswith('https://')
report = {'metrics':len(ids),'template_types':len(template_ids),'worked_calculations':'verified',
          'files':[]}
for old_name,new_doc in [('AI_SDLC_Adoption_Value_Framework',main),('Sprint_Scorecards_and_Stakeholder_Templates',forms)]:
    previous=Document(root/'outputs'/(old_name+'.docx'))
    assert len(previous.tables)==len(new_doc.tables)
    changes=[]
    for i,(old_table,new_table) in enumerate(zip(previous.tables,new_doc.tables)):
        before=[[c.text for c in row.cells] for row in old_table.rows]
        after=[[c.text for c in row.cells] for row in new_table.rows]
        if before!=after:
            assert old_name=='AI_SDLC_Adoption_Value_Framework'
            assert after[:len(before)]==before
            assert after[-1][0]=='1.1'
            changes.append(i)
    if old_name=='AI_SDLC_Adoption_Value_Framework':
        def metric_text(document):
            ps=document.paragraphs
            return {p.text:[q.text for q in ps[i+1:i+4]] for i,p in enumerate(ps)
                    if p.style.name=='Heading 2' and re.match(r'M[0-9]{2} ',p.text)}
        assert metric_text(previous)==metric_text(new_doc)
    for picture in new_doc.inline_shapes:
        assert picture._inline.docPr.get('descr')
report['preserved_metric_definitions_and_tables']=True
report['diagrams_with_alt_text']=len(main.inline_shapes)+len(forms.inline_shapes)
for f in (root/'outputs').glob('Engineering*.docx'):
    pdf = root/'tmp'/'qa'/f.stem/(f.stem+'.pdf')
    report['files'].append({'file':f.name,'bytes':f.stat().st_size,'rendered_pages':len(PdfReader(pdf).pages)})
(root/'tmp'/'qa'/'verification.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
