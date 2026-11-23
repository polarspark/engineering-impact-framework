"""Build MLA editions without changing the prior reference editions."""
from pathlib import Path
from copy import deepcopy
import re
import json
from PIL import ImageFont
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import build_framework as base
from framework_content import framework
from metric_content import metric_pages
from method_content import method_pages
from template_content import templates
from revision_content import updated_content
from mla_references import REFERENCES, TABLE_TITLES

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'
used=set()
table_counter=0
section_title=''
section_table_index=0


def citation(key):
    used.add(key)
    return REFERENCES[key][0]


def convert(text):
    text=text.replace('Version 1.1','Version 1.2')
    text=text.replace('The source register identifies their roles and versions.', 'The Works Cited section identifies these references.')
    def subst(match):
        inside=match.group(0)[1:-1]
        keys=[]
        for start,end in re.findall(r'S(\d+)-S(\d+)',inside):
            keys.extend('S'+str(i) for i in range(int(start),int(end)+1))
        if not keys:
            keys=['S'+x for x in re.findall(r'S(\d+)',inside)]
        return '('+'; '.join(citation(k) for k in dict.fromkeys(keys))+')'
    return re.sub(r'\[S\d+[^\]]*\]',subst,text)


def font(run,size=12):
    run.font.name='Times New Roman'
    run.font.size=Pt(size)
    run.font.color.rgb=RGBColor(0,0,0)
    run._element.get_or_add_rPr().rFonts.set(qn('w:ascii'),'Times New Roman')
    run._element.rPr.rFonts.set(qn('w:hAnsi'),'Times New Roman')


def rich(para,text):
    for segment in re.split(r'(\*\*.*?\*\*|\*[^*]+?\*)',text):
        if not segment: continue
        bold=segment.startswith('**') and segment.endswith('**')
        italic=not bold and segment.startswith('*') and segment.endswith('*')
        visible=segment[2:-2] if bold else segment[1:-1] if italic else segment
        for piece in re.split(r'(https://[^\s]+)',visible):
            if piece.startswith('https://'):
                url=piece.rstrip('.,;')
                node=OxmlElement('w:hyperlink')
                rid=para.part.relate_to(url,'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink',is_external=True)
                node.set(qn('r:id'),rid)
                run_node=OxmlElement('w:r'); pr=OxmlElement('w:rPr')
                fonts=OxmlElement('w:rFonts'); fonts.set(qn('w:ascii'),'Times New Roman'); fonts.set(qn('w:hAnsi'),'Times New Roman'); pr.append(fonts)
                sz=OxmlElement('w:sz'); sz.set(qn('w:val'),'24'); pr.append(sz)
                run_node.append(pr); tx=OxmlElement('w:t'); tx.text=url; run_node.append(tx); node.append(run_node); para._p.append(node)
                if piece[len(url):]: para.add_run(piece[len(url):])
            elif piece:
                run=para.add_run(piece); font(run); run.bold=bold; run.italic=italic
    return para


def para(doc,text='',style=None,indent=True):
    p=doc.add_paragraph(style=style)
    rich(p,convert(text))
    pf=p.paragraph_format
    pf.first_line_indent=Inches(.5 if indent and not style else 0)
    pf.space_before=pf.space_after=Pt(0)
    pf.line_spacing=2
    pf.widow_control=True
    return p


def heading(doc,text,level=1,new_page=False):
    p=para(doc,text,'Heading '+str(level),False)
    p.paragraph_format.keep_with_next=True
    p.paragraph_format.page_break_before=new_page
    for r in p.runs: r.bold=True
    return p


def document(title):
    d=Document()
    s=d.sections[0]
    s.page_width=Inches(8.5); s.page_height=Inches(11)
    s.top_margin=s.bottom_margin=s.left_margin=s.right_margin=Inches(1)
    s.header_distance=Inches(.5)
    for name in ['Normal','Title','Heading 1','Heading 2','Heading 3','List Bullet','List Number','Caption','TOC 1','TOC Heading']:
        try: st=d.styles[name]
        except KeyError: continue
        st.font.name='Times New Roman'; st.font.size=Pt(12); st.font.color.rgb=RGBColor(0,0,0)
        st.font.bold=False; st.font.italic=False
        st.paragraph_format.space_before=st.paragraph_format.space_after=Pt(0)
        st.paragraph_format.line_spacing=2
        if st.element.pPr is not None:
            for node in list(st.element.pPr.findall(qn('w:pBdr'))): st.element.pPr.remove(node)
    d.core_properties.title=title
    d.core_properties.author='Paul Harding'
    d.core_properties.last_modified_by='Paul Harding'
    d.core_properties.subject='Engineering Impact Framework MLA edition'
    d.core_properties.keywords='PolarSpark LLC; Engineering Impact Framework; AI adoption; SDLC'
    hp=s.header.paragraphs[0]
    hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    rr=hp.add_run('Harding '); font(rr)
    fld=OxmlElement('w:fldSimple'); fld.set(qn('w:instr'),'PAGE')
    run=OxmlElement('w:r'); rp=OxmlElement('w:rPr')
    fonts=OxmlElement('w:rFonts'); fonts.set(qn('w:ascii'),'Times New Roman'); fonts.set(qn('w:hAnsi'),'Times New Roman'); rp.append(fonts)
    sz=OxmlElement('w:sz'); sz.set(qn('w:val'),'24'); rp.append(sz); run.append(rp)
    tt=OxmlElement('w:t'); tt.text='1'; run.append(tt); fld.append(run); hp._p.append(fld)
    para(d,'Paul Harding, MBA ITM',indent=False)
    para(d,'PolarSpark LLC',indent=False)
    para(d,'23 November 2026',indent=False)
    title_p=para(d,title,'Title',False)
    title_p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    d.settings.element.append(base.element('w:updateFields',**{'w:val':'true'}))
    return d


def table(doc,heads,rows,widths=None,*ignored):
    global table_counter,section_table_index
    table_counter+=1
    titles=TABLE_TITLES.get(section_title,[])
    name=titles[section_table_index] if section_table_index<len(titles) else section_title
    section_table_index+=1
    label=para(doc,f'Table {table_counter}',indent=False)
    label.paragraph_format.keep_with_next=True
    caption=para(doc,name,indent=False); caption.paragraph_format.keep_with_next=True
    actual_widths=[6.5/len(heads)]*len(heads) if widths is None else [x*6.5/sum(widths) for x in widths]
    # Keep unbroken words readable at 12 points within the narrower MLA text block.
    regular=ImageFont.truetype('C:/Windows/Fonts/times.ttf',120)
    bold_font=ImageFont.truetype('C:/Windows/Fonts/timesbd.ttf',120)
    minima=[]
    for c,head in enumerate(heads):
        tokens=[(w,bold_font) for w in str(head).split()]
        tokens += [(w,regular) for row in rows for w in str(row[c]).split()]
        minima.append(max(f.getlength(w)/10/72 for w,f in tokens)+.17)
    if sum(minima)<6.5:
        remaining=6.5-sum(minima)
        weights=[max(.05,w-m) for w,m in zip(actual_widths,minima)]
        actual_widths=[m+remaining*w/sum(weights) for m,w in zip(minima,weights)]
    t=base.table(doc,heads,rows,actual_widths)
    # Remove the helper's extra spacer paragraph. MLA uses uniform double spacing.
    spacer=doc.paragraphs[-1]
    if not spacer.text: spacer._p.getparent().remove(spacer._p)
    for ri,row in enumerate(t.rows):
        for cell in row.cells:
            tcpr=cell._tc.get_or_add_tcPr()
            for shd in list(tcpr.findall(qn('w:shd'))): shd.set(qn('w:fill'),'FFFFFF')
            for p in cell.paragraphs:
                # Retain the helper's alignment while applying uniform MLA type and spacing.
                pf=p.paragraph_format; pf.space_before=pf.space_after=Pt(0); pf.line_spacing=2
                pf.first_line_indent=Inches(0)
                pf.keep_with_next=ri==0
                for r in p.runs: font(r); r.bold=ri==0
    return t


def figure(doc,name,caption,description,*ignored):
    cap=re.sub(r'^Figure (\d+)\s+',r'Fig. \1. ',caption)
    n=re.search(r'Fig\. (\d+)',cap).group(1)
    para(doc,f'The relationship is illustrated in figure {n}.')
    p=doc.add_paragraph(); p.paragraph_format.keep_with_next=True
    p.paragraph_format.space_before=p.paragraph_format.space_after=Pt(0)
    p.paragraph_format.line_spacing=1
    pic=p.add_run().add_picture(str(ROOT/'assets'/'diagrams'/(name+'.png')),width=Inches(6.5))
    pic._inline.docPr.set('descr',description)
    pic._inline.docPr.set('title',name.replace('_',' ').title())
    if name=='delivery_measurement': cap+=' Original measurement diagram; the commit to production concept follows DORA ('+citation('S3')+').'
    elif name=='ai_review_release': cap+=' Original local workflow informed by NIST AI RMF ('+citation('S7')+').'
    else: cap+=' Original framework diagram.'
    para(doc,cap,indent=False)


def record_field(doc,label,hint='Enter response',lines=1):
    para(doc,'**'+label+'** ['+hint+']',indent=False)
    if lines:
        # A normal blank paragraph creates editable response space without a fixed height.
        for _ in range(lines): para(doc,'',indent=False)


def content(doc,pages,is_forms=False):
    global section_title,section_table_index
    for index,page in enumerate(pages):
        section_title=page.get('heading',page.get('title',''))
        section_table_index=0
        if index:
            # Forms begin on fresh pages so they can be copied and reused independently.
            heading(doc,section_title,new_page=is_forms)
        for item in page['items']:
            k=item[0]
            if k=='p': para(doc,item[1])
            elif k=='h': heading(doc,item[1],2)
            elif k in ['b','n']: para(doc,item[1],'List Bullet' if k=='b' else 'List Number',False)
            elif k=='t': table(doc,*item[1:])
            elif k=='f': record_field(doc,*item[1:])
            elif k=='i': figure(doc,*item[1:])
            elif k=='m':
                ident,name,definition,source,use=item[1:]
                heading(doc,ident+' '+name,2)
                para(doc,'**Definition and calculation.** '+definition)
                para(doc,'**Source and accountability.** '+source)
                para(doc,'**Interpretation and action.** '+use)
            elif k=='l': raise ValueError('Unexpected old source register')


def works_cited(doc):
    p=para(doc,'Works Cited',indent=False)
    p.paragraph_format.page_break_before=True; p.paragraph_format.keep_with_next=True
    p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    entries=sorted((REFERENCES[k][1] for k in used),key=lambda x:re.sub(r'^[*\" ]+','',x).casefold())
    for entry in entries:
        p=para(doc,entry,indent=False)
        p.paragraph_format.left_indent=Inches(.5)
        p.paragraph_format.first_line_indent=Inches(-.5)
        p.paragraph_format.keep_together=True


def prepare():
    main,forms=updated_content(deepcopy(framework)+deepcopy(metric_pages)+deepcopy(method_pages),deepcopy(templates))
    # Replace the source register with MLA entries, retaining the version and local adoption record.
    end=main[-1]
    keep=False; retained=[]
    for item in end['items']:
        if item[0]=='h' and item[1]=='Framework change record': keep=True
        if keep: retained.append(deepcopy(item))
    for item in retained:
        if item[0]=='t': item[2].append(['1.2','23 November 2026','MLA edition with author credit, in text citations, numbered tables and figures, and Works Cited.'])
    main=main[:-2]+[{'heading':'Framework version and adoption notes','items':retained}]
    for pages in [main,forms]:
        for page in pages:
            page['items']=[(i[0],i[1].replace('Version 1.1','Version 1.2')) if i[0]=='p' else i for i in page['items']]
    main[0]['items'].append(('p','The three phases, metric extensions, value calculations, maturity scoring, templates, and diagrams are original elements of this framework. The cited standards and research supply the stated foundations. Public descriptions and abstracts were consulted for ISO standards; this document does not claim a clause by clause conformity assessment.'))
    forms[0]['items'].append(('p','These forms implement the companion *Engineering Impact Framework* (Harding). Their delivery concepts draw on DORA and Scrum (Harvey; Schwaber and Sutherland). Their maturity and AI risk records use the published NIST foundations while retaining local scoring and approval rules (Tabassi; "AI RMF Core").'))
    for page in main:
        if page.get('heading')=='NIST AI adoption integration':
            page['items'].append(('p','The local interpretation also draws on the Playbook suggested actions ("Govern"; "Map"; "Measure"; "Manage"). NIST identifies an active revision of AI RMF 1.0 ("AI Risk Management Framework").'))
        if page.get('heading')=='Framework version and adoption notes':
            page['items'].insert(0,('p','As checked on 23 November 2026, NIST lists SSDF 1.1 as final and SSDF 1.2 as draft ("Publications"). Record the approved reference version when adopting the framework.'))
    for page in forms:
        title=page.get('heading','')
        if title=='T09 SDLC and documentation assessment':
            page['items'].insert(1,('p','The domain references are ISO/IEC/IEEE 12207:2026 and 15289:2019 [S1, S2]. Scores and evidence thresholds are local framework definitions.'))
        elif title=='T10 AI use case and risk record':
            page['items'].insert(1,('p','Tailor this record to the AI RMF and the generative AI profile where relevant [S6, S8]. The form is a local implementation tool.'))
    return main,forms


if __name__=='__main__':
    main,forms=prepare()
    report=[]
    for name,pages,title in [('Engineering_Impact_Framework_MLA',main,'Engineering Impact Framework'),('Engineering_Impact_Framework_Templates_MLA',forms,'Engineering Impact Framework Templates')]:
        used.clear(); table_counter=0
        d=document(title)
        content(d,pages,is_forms='Templates' in name)
        if 'Templates' in name: used.update(['HARDING','S3','S5','S6','S7'])
        else: used.update(['GOVERN','MAP','MEASURE','MANAGE','STATUS','S11'])
        works_cited(d)
        target=OUT/(name+'.docx'); d.save(target)
        report.append({'file':str(target),'sources':sorted(used),'tables':table_counter,'figures':len(d.inline_shapes)})
        print(str(target))
    (ROOT/'tmp'/'mla_build.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
