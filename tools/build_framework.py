from pathlib import Path
import json
import re
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs'
OUT.mkdir(exist_ok=True)

def element(tag, **attrs):
    node = OxmlElement(tag)
    for key, value in attrs.items():
        node.set(qn(key), str(value))
    return node

def new_doc(title):
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Inches(8.5), Inches(11)
    sec.top_margin, sec.bottom_margin = Inches(.65), Inches(.65)
    sec.left_margin = sec.right_margin = Inches(.72)
    sec.header_distance = sec.footer_distance = Inches(.28)
    for name in ['Normal', 'Title', 'Subtitle', 'Heading 1', 'Heading 2', 'Heading 3', 'List Bullet', 'List Number']:
        style = doc.styles[name]
        style.font.name = 'Calibri'
        style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.widow_control = True
    normal = doc.styles['Normal']
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.06
    for name, size in [('Title', 28), ('Subtitle', 13), ('Heading 1', 20), ('Heading 2', 12.5), ('Heading 3', 11)]:
        style = doc.styles[name]
        style.font.size = Pt(size)
        style.font.bold = name != 'Subtitle'
        style.paragraph_format.space_before = Pt(8 if name != 'Title' else 0)
        style.paragraph_format.space_after = Pt(7)
        style.paragraph_format.keep_with_next = True
        # Remove theme color and built-in title border residues.
        if style.element.rPr is not None:
            for color in style.element.rPr.findall(qn('w:color')):
                color.attrib.pop(qn('w:themeColor'), None)
        if style.element.pPr is not None:
            for border in list(style.element.pPr.findall(qn('w:pBdr'))):
                style.element.pPr.remove(border)
    doc.core_properties.title = title
    doc.core_properties.subject = 'Sprint based measurement of AI and SDLC adoption value'
    doc.core_properties.author = ''
    doc.core_properties.keywords = 'AI observability SDLC DORA SPACE NIST AI RMF sprint value maturity'
    doc.core_properties.comments = ''
    hp = sec.header.paragraphs[0]
    hp.add_run('ENGINEERING IMPACT FRAMEWORK').font.size = Pt(8)
    hp.paragraph_format.space_after = Pt(0)
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    fp.add_run('Version 1.1   November 23 2026   Page ').font.size = Pt(8)
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    rr = OxmlElement('w:r')
    rr.append(element('w:t'))
    rr[0].text = '1'
    fld.append(rr)
    fp._p.append(fld)
    doc.settings.element.append(element('w:updateFields', **{'w:val': 'true'}))
    return doc

def p(doc, text, style=None):
    para = doc.add_paragraph(style=style)
    # Use ** only as an authoring convention, never as visible markup.
    parts = re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        run = para.add_run(part[2:-2] if part.startswith('**') else part)
        run.bold = part.startswith('**')
    return para

def h(doc, text, level=2):
    assert re.match(r'^[A-Za-z0-9 ]+$', text), text
    return doc.add_heading(text, level)

def table(doc, heads, rows, widths=None, small=False, min_height=None):
    t = doc.add_table(rows=1, cols=len(heads))
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    if widths is None:
        widths = [7.06 / len(heads)] * len(heads)
    for col, width in zip(t.columns, widths):
        col.width = Inches(width)
    for c, head, width in zip(t.rows[0].cells, heads, widths):
        c.width = Inches(width)
        c.text = head
    for row in rows:
        cells = t.add_row().cells
        for c, value, width in zip(cells, row, widths):
            c.width = Inches(width)
            c.text = str(value)
    for ri, row in enumerate(t.rows):
        row._tr.get_or_add_trPr().append(element('w:cantSplit'))
        if ri == 0:
            row._tr.get_or_add_trPr().append(element('w:tblHeader'))
        if min_height and ri > 0:
            row.height = Inches(min_height)
        for ci, cell in enumerate(row.cells):
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tcpr = cell._tc.get_or_add_tcPr()
            borders = element('w:tcBorders')
            for side in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
                borders.append(element('w:' + side, **{'w:val':'single','w:sz':'4','w:color':'D9D9D9'}))
            tcpr.append(borders)
            margins = element('w:tcMar')
            for side in ['top','bottom','left','right']:
                margins.append(element('w:' + side, **{'w:w':'85','w:type':'dxa'}))
            tcpr.append(margins)
            fill = '243746' if ri == 0 else ('F1F4F6' if ri % 2 == 0 else 'FFFFFF')
            tcpr.append(element('w:shd', **{'w:fill':fill}))
            for para in cell.paragraphs:
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(2)
                para.paragraph_format.line_spacing = 1.02
                para.paragraph_format.keep_with_next = False
                if ri > 0 and len(str(rows[ri-1][ci])) < 12 and len(heads) > 3:
                    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in para.runs:
                    run.font.size = Pt(9.3 if small else 10.3)
                    run.font.bold = ri == 0
                    run.font.color.rgb = RGBColor(255,255,255) if ri == 0 else RGBColor(0,0,0)
    doc.add_paragraph().paragraph_format.space_after = Pt(1)
    return t

def link(doc, label, url):
    para = doc.add_paragraph()
    rel = doc.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    node = OxmlElement('w:hyperlink')
    node.set(qn('r:id'), rel)
    rr = OxmlElement('w:r')
    pr = OxmlElement('w:rPr')
    pr.append(element('w:color', **{'w:val':'154B72'}))
    pr.append(element('w:u', **{'w:val':'single'}))
    rr.append(pr)
    tt = OxmlElement('w:t'); tt.text = label; rr.append(tt)
    node.append(rr); para._p.append(node)
    para.paragraph_format.space_after = Pt(3)

def field(doc, label, hint='Enter response', lines=1):
    para = p(doc, '**' + label + '**  [' + hint + ']')
    para.paragraph_format.space_after = Pt(4)
    for _ in range(lines):
        pp = doc.add_paragraph('________________________________________________________________________________')
        pp.paragraph_format.space_after = Pt(4)
        for rr in pp.runs:
            rr.font.color.rgb = RGBColor(150,150,150)
            rr.font.size = Pt(9)

def metric(doc, ident, name, definition, source, use):
    h(doc, ident + ' ' + name)
    p(doc, '**Definition and calculation.** ' + definition)
    p(doc, '**Source and accountability.** ' + source)
    p(doc, '**Interpretation and action.** ' + use)

def figure(doc, name, caption, description, width=7.0):
    para=doc.add_paragraph()
    para.paragraph_format.keep_with_next=True
    para.paragraph_format.space_after=Pt(3)
    shape=para.add_run().add_picture(str(ROOT/'assets'/'diagrams'/(name+'.png')),width=Inches(width))
    shape._inline.docPr.set('descr',description)
    shape._inline.docPr.set('title',name.replace('_',' ').title())
    cap=p(doc,caption)
    cap.paragraph_format.space_after=Pt(8)
    for run in cap.runs: run.font.size=Pt(10)

def render_content(doc, pages, include_toc=False):
    for i, page in enumerate(pages):
        if i == 1 and include_toc:
            toc_heading=doc.add_paragraph('Contents', 'Heading 2')
            toc_heading.paragraph_format.page_break_before=True
            tp = doc.add_paragraph()
            tf = OxmlElement('w:fldSimple')
            tf.set(qn('w:instr'), 'TOC \\o "1-1" \\h \\z \\u')
            tp._p.append(tf)
        if 'title' in page:
            heading=doc.add_paragraph(page['title'], 'Title')
        else:
            heading=h(doc, page['heading'], 1)
        if i:
            heading.paragraph_format.page_break_before=True
        for item in page['items']:
            kind = item[0]
            if kind == 'p': p(doc, item[1])
            elif kind == 'h': h(doc, item[1])
            elif kind == 'b': p(doc, item[1], 'List Bullet')
            elif kind == 'n': p(doc, item[1], 'List Number')
            elif kind == 't': table(doc, *item[1:])
            elif kind == 'm': metric(doc, *item[1:])
            elif kind == 'f': field(doc, *item[1:])
            elif kind == 'l': link(doc, *item[1:])
            elif kind == 'i': figure(doc, *item[1:])
            else: raise ValueError(kind)

if __name__ == '__main__':
    from framework_content import framework
    from metric_content import metric_pages
    from method_content import method_pages
    from template_content import templates
    from revision_content import updated_content
    framework += metric_pages + method_pages
    framework,templates=updated_content(framework,templates)
    for name, content in [('Engineering_Impact_Framework', framework), ('Engineering_Impact_Framework_Templates', templates)]:
        doc = new_doc(content[0].get('title', name))
        render_content(doc, content, include_toc=name == 'Engineering_Impact_Framework')
        target = OUT / (name + '.docx')
        doc.save(target)
        print(str(target))
    manifest = {'framework_sections':len(framework), 'template_sections':len(templates), 'date':'2026-11-23'}
    (ROOT / 'tools' / 'content_manifest.json').write_text(json.dumps(manifest, indent=2))
