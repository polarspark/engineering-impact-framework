"""Restyle the complete reference editions as PolarSpark business publications."""
from pathlib import Path
from copy import deepcopy
import re,json
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH,WD_TAB_ALIGNMENT
from docx.enum.style import WD_STYLE_TYPE
from docx.text.paragraph import Paragraph
from docx.text.hyperlink import Hyperlink
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from mla_references import REFERENCES

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'
LOGO=ROOT/'assets/brand/polar-spark-mark.png'
WEB='https://polarspark.com/'
VERSION='1.3'
REFERENCES=deepcopy(REFERENCES)
REFERENCES.update({
 'HARDING':('Harding','Paul Harding. *Engineering Impact Framework*. PolarSpark LLC, business white paper, version 1.3, 23 November 2026. https://github.com/polarspark/engineering-impact-framework/blob/main/outputs/Engineering_Impact_Framework_Whitepaper.docx.'),
 'SPRING':('"Testing Spring Boot Applications"','Spring. "Testing Spring Boot Applications." *Spring Boot Reference Documentation*. https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html. Accessed 23 November 2026.'),
 'MAVEN':('"Apache Maven Surefire"','Apache Software Foundation. "Apache Maven Surefire." https://maven.apache.org/surefire/. Accessed 23 November 2026.'),
 'OTEL':('"Instrumentation Ecosystem"','OpenTelemetry. "Instrumentation Ecosystem." https://opentelemetry.io/docs/languages/java/instrumentation/. Accessed 23 November 2026.'),
})
KEYS=list(REFERENCES)
IDS={k:i+1 for i,k in enumerate(KEYS)}
ALIASES={re.sub(r'\*','',v[0]):k for k,v in REFERENCES.items()}
used=set()

def node(tag,**attrs):
    e=OxmlElement(tag)
    for k,v in attrs.items(): e.set(qn(k),str(v))
    return e

def cite(keys):
    used.update(keys)
    return '['+', '.join(str(IDS[k]) for k in keys)+']'

def convert(text):
    if text.startswith('The measurement rules, maturity rubric, suggested observation windows'):
        return 'Measurement rules, scoring, suggested observation windows, and decision thresholds are proposed organizational conventions. Tailor them to local ownership, evidence, and risk policies. All worked results are illustrative. Alignment with a cited standard does not establish certification or regulatory compliance.'
    if text.startswith('The three phases, metric extensions, value calculations, maturity scoring'):
        return 'The phases, metric extensions, value calculations, maturity scores, templates, and diagrams are PolarSpark framework designs. ISO references use public descriptions and abstracts. This white paper does not establish conformity or certification.'
    text=text.replace('Version 1.2','Version 1.3')
    text=text.replace('Design status','Scope and interpretation')
    text=text.replace('The Works Cited section','The references section')
    text=text.replace('Works Cited','references')
    text=text.replace('Engineering Impact Framework Templates','Engineering Impact Framework Workbook')
    def replace(m):
        clean=m.group(1).replace('*','')
        parts=[p.strip() for p in clean.split(';')]
        if parts and all(p in ALIASES for p in parts):
            return cite([ALIASES[p] for p in parts])
        return m.group(0)
    return re.sub(r'\(([^()]+)\)',replace,text)

def markup(p):
    parts=[]
    for x in p.iter_inner_content():
        if isinstance(x,Hyperlink): parts.append(x.text)
        elif x.text:
            t=x.text
            if x.bold: t='**'+t+'**'
            elif x.italic: t='*'+t+'*'
            parts.append(t)
    return ''.join(parts)

def font(r,size=11,bold=None):
    r.font.name='Calibri';r.font.size=Pt(size);r.font.color.rgb=RGBColor(0,0,0)
    if bold is not None:r.bold=bold
    pr=r._element.get_or_add_rPr()
    fonts=pr.rFonts
    if fonts is not None:
        fonts.set(qn('w:ascii'),'Calibri');fonts.set(qn('w:hAnsi'),'Calibri')

def rich(p,text,size=11):
    for bit in re.split(r'(\*\*.*?\*\*|\*[^*]+?\*)',text):
        if not bit:continue
        bold=bit.startswith('**') and bit.endswith('**')
        italic=not bold and bit.startswith('*') and bit.endswith('*')
        value=bit[2:-2] if bold else bit[1:-1] if italic else bit
        for item in re.split(r'(https://[^\s]+)',value):
            if not item:continue
            if item.startswith('https://'):
                url=item.rstrip('.,;')
                rel=p.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
                a=node('w:hyperlink',**{'r:id':rel})
                r=node('w:r');rp=node('w:rPr')
                rp.append(node('w:rFonts',**{'w:ascii':'Calibri','w:hAnsi':'Calibri'}))
                rp.append(node('w:sz',**{'w:val':int(size*2)}));rp.append(node('w:color',**{'w:val':'17588A'}))
                r.append(rp);t=node('w:t');t.text=url;r.append(t);a.append(r);p._p.append(a)
                if item[len(url):]:font(p.add_run(item[len(url):]),size)
            else:
                r=p.add_run(item);font(r,size);r.bold=bold;r.italic=italic
    return p

def clear(p):
    for el in list(p._p):
        if el.tag!=qn('w:pPr'):p._p.remove(el)

def add(doc,text='',style=None,before=None,size=None):
    p=before.insert_paragraph_before(style=style) if before is not None else doc.add_paragraph(style=style)
    if size is None:size={'Title':30,'Subtitle':15,'Heading 1':15,'Heading 2':12,'TOC Heading':15}.get(style,11)
    rich(p,text,size)
    if style and (style.startswith('Heading') or style in ['Title','TOC Heading']):
        for r in p.runs:r.bold=True
    return p

def field(p,instruction):
    e=node('w:fldSimple',**{'w:instr':instruction})
    r=node('w:r');pr=node('w:rPr');pr.append(node('w:sz',**{'w:val':'18'}));r.append(pr)
    t=node('w:t');t.text='1';r.append(t);e.append(r);p._p.append(e)

def styles(d):
    s=d.sections[0]
    s.top_margin=s.bottom_margin=s.left_margin=s.right_margin=Inches(.75)
    s.header_distance=s.footer_distance=Inches(.3)
    sizes={'Normal':11,'Title':30,'Subtitle':15,'Heading 1':15,'Heading 2':12,'Heading 3':11,'Caption':9.5,'List Bullet':11,'List Number':11,'TOC 1':10.5,'TOC Heading':15}
    for name,size in sizes.items():
        st=d.styles[name] if name in d.styles else d.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
        st.font.name='Calibri';st.font.size=Pt(size);st.font.color.rgb=RGBColor(0,0,0)
        st.font.italic=False;st.font.bold=name.startswith('Heading') or name=='Title'
        pf=st.paragraph_format
        pf.first_line_indent=Inches(0)
        pf.line_spacing=1.12;pf.space_before=Pt(10 if name.startswith('Heading') else 0);pf.space_after=Pt(6)
        if name.startswith('Heading'):pf.keep_with_next=True
        if st.element.pPr is not None:
            for e in list(st.element.pPr.findall(qn('w:pBdr'))):st.element.pPr.remove(e)
    d.core_properties.author='Paul Harding'
    d.core_properties.last_modified_by='Paul Harding'
    d.core_properties.subject='PolarSpark LLC business publication on AI and SDLC adoption value'
    d.core_properties.keywords='PolarSpark LLC; polarspark.com; Engineering Impact Framework; business white paper'
    s.different_first_page_header_footer=True
    hp=s.header.paragraphs[0];clear(hp)
    pic=hp.add_run().add_picture(str(LOGO),width=Inches(.23))
    pic._inline.docPr.set('descr','PolarSpark official radial spark company logo')
    font(hp.add_run('  PolarSpark LLC  |  Engineering Impact Framework'),8.5)
    hp.paragraph_format.space_after=Pt(0)
    d.styles['Footer'].paragraph_format.tab_stops.clear_all()
    for footer in [s.footer,s.first_page_footer]:
        fp=footer.paragraphs[0];clear(fp)
        fp.paragraph_format.tab_stops.clear_all()
        fp.paragraph_format.tab_stops.add_tab_stop(Inches(7),WD_TAB_ALIGNMENT.RIGHT)
        rich(fp,WEB,9)
        font(fp.add_run('\tVersion 1.3  |  '),9);field(fp,'PAGE')
        fp.paragraph_format.space_after=Pt(0)

def body(d):
    for p in list(d.paragraphs):
        if p._p.findall('.//'+qn('w:drawing')):
            pf=p.paragraph_format;pf.first_line_indent=Inches(0);pf.space_before=Pt(3);pf.space_after=Pt(3);pf.line_spacing=1
            continue
        text=convert(markup(p))
        clear(p)
        size=15 if p.style.name=='Heading 1' else 12 if p.style.name=='Heading 2' else 11
        if text.startswith('Fig. '):size=9.5
        rich(p,text,size)
        pf=p.paragraph_format
        if p.style.name not in ['List Bullet','List Number']:
            pf.first_line_indent=Inches(0);pf.left_indent=Inches(0)
        pf.line_spacing=1.12;pf.space_before=Pt(9 if p.style.name.startswith('Heading') else 0);pf.space_after=Pt(6)
        p.alignment=WD_ALIGN_PARAGRAPH.LEFT
        if text.startswith('Fig. '):
            p.style='Caption';pf.space_after=Pt(9)
        if not text:
            pf.space_after=Pt(10);pf.line_spacing=1
    for shape in d.inline_shapes:
        shape.height=int(shape.height*7/6.5);shape.width=Inches(7)
    for t in d.tables:
        for col in t.columns:col.width=int(col.width*7/6.5)
        for i,row in enumerate(t.rows):
            for c in row.cells:
                c.width=int(c.width*7/6.5)
                pr=c._tc.get_or_add_tcPr()
                for sh in list(pr.findall(qn('w:shd'))):pr.remove(sh)
                pr.append(node('w:shd',**{'w:fill':'101F3B' if i==0 else 'F0F5FB' if i%2==0 else 'FFFFFF'}))
                for p in c.paragraphs:
                    text=convert(markup(p));clear(p);rich(p,text,10.3)
                    pf=p.paragraph_format;pf.line_spacing=1.04;pf.space_before=Pt(2);pf.space_after=Pt(3);pf.first_line_indent=Inches(0)
                    for r in p.runs:
                        font(r,10.3,i==0)
                        r.font.color.rgb=RGBColor(255,255,255) if i==0 else RGBColor(0,0,0)
def captions(d):
    # Use the logical table order; no page-dependent labels are introduced.
    for i,t in enumerate(d.tables,1):
        prev=t._tbl.getprevious()
        if prev is None or prev.tag!=qn('w:p'):continue
        title=Paragraph(prev,d)
        label_el=prev.getprevious()
        if label_el is None or label_el.tag!=qn('w:p'):continue
        label=Paragraph(label_el,d)
        if not label.text.startswith('Table '):continue
        titletext=title.text
        clear(label);rich(label,f'**Table {i}. {titletext}**',10)
        label.style='Caption';label.paragraph_format.keep_with_next=True
        label.paragraph_format.space_before=Pt(7);label.paragraph_format.space_after=Pt(4)
        title._p.getparent().remove(title._p)

def brand(d,anchor,title,kind,subtitle):
    p=add(d,before=anchor)
    p.paragraph_format.space_after=Pt(9)
    shape=p.add_run().add_picture(str(LOGO),width=Inches(.68))
    shape._inline.docPr.set('title','PolarSpark Logo');shape._inline.docPr.set('descr','Official PolarSpark radial spark logo on the company navy background')
    font(p.add_run('   PolarSpark LLC'),17,True)
    p=add(d,kind,before=anchor,size=10);p.paragraph_format.space_after=Pt(10)
    p=add(d,title,'Title',anchor);p.paragraph_format.space_after=Pt(10)
    for r in p.runs:font(r,30,True)
    p=add(d,subtitle,'Subtitle',anchor);p.paragraph_format.space_after=Pt(18)
    add(d,'**Paul Harding, MBA ITM**',before=anchor)
    add(d,'PolarSpark LLC  |  '+WEB,before=anchor)
    p=add(d,'Version 1.3  |  23 November 2026',before=anchor,size=10)
    p.paragraph_format.space_after=Pt(18)

def front(d,mode,title):
    # Replace the student-paper author/date block while retaining all substantive content.
    for p in list(d.paragraphs)[:4]:p._p.getparent().remove(p._p)
    anchor=d.paragraphs[0]
    if mode=='main' and anchor.text.startswith('Version '):
        anchor._p.getparent().remove(anchor._p);anchor=d.paragraphs[0]
    desc={
      'main':('BUSINESS WHITE PAPER','Measuring the value of AI and software delivery changes'),
      'forms':('IMPLEMENTATION WORKBOOK','Sprint scorecards and stakeholder feedback templates'),
      'java':('WORKFLOW GUIDE','A Java application example for adoption and valuation'),
    }
    brand(d,anchor,title,*desc[mode])
    if mode=='java':
        # Preserve the original twenty-page navigation and workflow page boundaries.
        return
    if mode=='main':
        add(d,'A change to engineering practice should earn its place through measurable delivery outcomes, acceptable risk, and value that can be verified. This white paper provides the decision model and evidence records for evaluating AI tools, changes to existing AI use, and new development workflows in real delivery.',before=anchor)
        add(d,'The framework combines sprint observations with production, business, and stakeholder evidence. It keeps recovered engineering capacity separate from realized financial benefits and assesses SDLC practice, documentation, and AI adoption as distinct maturity profiles.',before=anchor)
        add(d,'**Baseline** records current delivery. **Adoption** evaluates the introduced change. **Improvement** tests an adjustment against both the original baseline and the preceding state.',before=anchor)
        add(d,'**Intended readers** Engineering leaders, product owners, security and platform teams, finance partners, and business sponsors.',before=anchor)
        p=add(d,'Contents','TOC Heading',anchor);p.paragraph_format.page_break_before=True
        p=add(d,before=anchor);field(p,'TOC \\o "1-1" \\h \\z \\u')
        p=add(d,'Executive summary','Heading 1',anchor);p.paragraph_format.page_break_before=True
    else:
        add(d,'Use this workbook to document a proposed change, establish a defensible baseline, close sprint observations, and reconcile costs and verified benefits. The records support decisions across Baseline, Adoption, and Improvement.',before=anchor)
        add(d,'Copy a fresh form for each initiative or reporting window. Keep stable metric definitions, evidence references, responsible owners, and unresolved findings. Use the companion white paper for the full metric catalogue, maturity rubric, and value recognition rules.',before=anchor)
        add(d,'**Included records** Adoption contract, metric definitions, three phase scorecards, role specific feedback, maturity assessment, AI risk record, value ledger, and evaluation decision.',before=anchor)
        p=add(d,'Using this workbook','Heading 1',anchor);p.paragraph_format.page_break_before=True

def references(d,keys):
    used.update(keys)
    p=add(d,'References and source notes','Heading 1');p.paragraph_format.page_break_before=True
    add(d,'References support the stated concepts. The framework’s metric extensions, value calculations, maturity scores, templates, and diagrams are local design choices. ISO references use public descriptions and abstracts rather than a clause by clause conformity assessment.',size=10)
    for k in sorted(used,key=lambda k:IDS[k]):
        p=add(d,f'[{IDS[k]}] '+REFERENCES[k][1],size=9.5)
        p.paragraph_format.keep_together=True;p.paragraph_format.space_after=Pt(7)

def feedback_forms(d):
    active=False
    for el in list(d.element.body):
        if el.tag==qn('w:p'):
            p=Paragraph(el,d)
            if p.style.name=='Heading 1':
                active=bool(re.match(r'T0[678] ',p.text))
            if not active:continue
            if not p.text.strip():
                el.getparent().remove(el);continue
            pf=p.paragraph_format;pf.line_spacing=1.05;pf.space_after=Pt(4)
        elif active and el.tag==qn('w:tbl'):
            for margin in el.xpath('.//w:tcMar/w:top|.//w:tcMar/w:bottom'):
                margin.set(qn('w:w'),'40')
            for pe in el.xpath('.//w:p'):
                p=Paragraph(pe,d);p.paragraph_format.line_spacing=1
                p.paragraph_format.space_before=Pt(1);p.paragraph_format.space_after=Pt(1)

def build(only=None):
    specs=[
      ('Engineering_Impact_Framework_MLA','Engineering_Impact_Framework_Whitepaper','main','Engineering Impact Framework',list(REFERENCES)[:16]),
      ('Engineering_Impact_Framework_Templates_MLA','Engineering_Impact_Framework_Workbook','forms','Engineering Impact Framework Workbook',['S1','S2','S3','S5','S6','S7','S8','HARDING']),
      ('Engineering_Impact_Framework_Java_Workflow_MLA','Engineering_Impact_Framework_Java_Workflow','java','Engineering Impact Framework Java Workflow',['S3','S6','S8','S9','HARDING','SPRING','MAVEN','OTEL']),
    ]
    report=[]
    for source,target,mode,title,keys in specs:
        if only and mode!=only:continue
        used.clear();d=Document(OUT/(source+'.docx'))
        # Remove the old bibliography. The business references are rebuilt below.
        p=next(p for p in d.paragraphs if p.text=='Works Cited')
        el=p._p
        while el is not None and el.tag!=qn('w:sectPr'):
            following=el.getnext();el.getparent().remove(el);el=following
        styles(d);body(d);captions(d);front(d,mode,title)
        if mode=='main':
            for t in d.tables:
                if t.rows[0].cells[0].text=='Version':
                    previous=t.rows[-1]
                    row=t.add_row()
                    row._tr.get_or_add_trPr().append(node('w:cantSplit'))
                    for c,old,value in zip(row.cells,previous.cells,['1.3','23 November 2026','PolarSpark business white paper and companion guides with official logo, company website, business layout, and numbered references.']):
                        c._tc.remove(c._tc.tcPr);c._tc.insert(0,deepcopy(old._tc.tcPr))
                        c.text=value
                        for p in c.paragraphs:
                            p.paragraph_format.space_after=Pt(4);p.paragraph_format.line_spacing=1.04
                            for r in p.runs:font(r,10.3)
            for p in d.paragraphs:
                if p.style.name=='Heading 1' and p.text in ['Primary outcome metric definitions','Value calculations and recognition rules','NIST AI adoption integration','Implementation and reporting plan']:
                    p.paragraph_format.page_break_before=True
        references(d,keys)
        if mode=='forms':feedback_forms(d)
        d.core_properties.title=title
        path=OUT/(target+'.docx');d.save(path)
        report.append({'file':path.name,'references':len(used),'reference_ids':sorted(IDS[k] for k in used),'body_images':len(d.inline_shapes)})
        print(path)
    (ROOT/'tmp/business_build.json').write_text(json.dumps(report,indent=2),encoding='utf-8')

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--only',choices=['main','forms','java'])
    build(parser.parse_args().only)
