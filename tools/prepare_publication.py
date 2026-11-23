"""Create readable repository editions from the final, verified Word files."""
from pathlib import Path
from docx import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.ns import qn
from docx.text.hyperlink import Hyperlink

ROOT=Path(__file__).resolve().parents[1]
DOCS=ROOT/'docs'
DOCS.mkdir(exist_ok=True)

def inline(p):
    result=[]
    for part in p.iter_inner_content():
        if isinstance(part,Hyperlink):
            result.append('['+part.text+']('+part.url+')')
        else:
            t=part.text
            if part.bold and t.strip(): t='**'+t+'**'
            elif part.italic and t.strip(): t='*'+t+'*'
            result.append(t)
    return ''.join(result).strip()

def export(stem,target):
    d=Document(ROOT/'outputs'/(stem+'.docx'))
    chunks=[]
    for el in d.element.body:
        if el.tag==qn('w:p'):
            p=Paragraph(el,d)
            pictures=el.findall('.//'+qn('wp:docPr'))
            for pic in pictures:
                name=pic.get('title','').lower().replace(' ','_')
                assert (ROOT/'assets'/'diagrams'/(name+'.png')).exists(),name
                chunks.append('!['+pic.get('descr','Workflow diagram')+'](../assets/diagrams/'+name+'.png)')
            text=inline(p)
            if not text: continue
            if p.style.name=='Title': text='# '+text
            elif p.style.name.startswith('Heading '):
                text='#'*(int(p.style.name.split()[-1])+1)+' '+text
            elif p.style.name=='List Bullet': text='- '+text
            elif p.style.name=='List Number': text='1. '+text
            elif text=='Works Cited': text='## Works Cited'
            chunks.append(text)
        elif el.tag==qn('w:tbl'):
            t=Table(el,d)
            rows=[]
            for row in t.rows:
                rows.append('| '+' | '.join('<br>'.join(inline(p) for p in c.paragraphs).replace('|','\\|') for c in row.cells)+' |')
            rows.insert(1,'| '+' | '.join('---' for _ in t.columns)+' |')
            chunks.append('\n'.join(rows))
    text='\n\n'.join(chunks)+'\n'
    assert 'Paul Harding, MBA ITM' in text and 'PolarSpark LLC' in text
    assert 'https://' in text and 'Works Cited' in text
    (DOCS/target).write_text(text,encoding='utf-8')

if __name__=='__main__':
    for stem,target in [
       ('Engineering_Impact_Framework_MLA','framework.md'),
       ('Engineering_Impact_Framework_Templates_MLA','templates.md'),
       ('Engineering_Impact_Framework_Java_Workflow_MLA','java-workflow.md')]:
        export(stem,target)
        print(DOCS/target)
