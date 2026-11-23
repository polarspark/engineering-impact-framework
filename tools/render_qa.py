from pathlib import Path
import sys
import json
import pypdfium2 as pdfium
from pypdf import PdfReader
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parents[1]
reports = []
pattern=sys.argv[1] if len(sys.argv)>1 else 'Engineering*'
for pdf in sorted((root/'tmp'/'qa').glob(pattern+'/*.pdf')):
    doc = pdfium.PdfDocument(str(pdf))
    reader = PdfReader(str(pdf))
    pages = []
    thumbs = []
    for i in range(len(doc)):
        page = doc[i]
        image = page.render(scale=1.7).to_pil().convert('RGB')
        target = pdf.parent/f'page-{i+1}.png'
        image.save(target)
        text = reader.pages[i].extract_text() or ''
        lines = text.splitlines()
        pages.append({'page':i+1,'words':len(text.split()),'first':lines[:3],'last':lines[-3:]})
        thumb = ImageOps.contain(image, (510,660))
        tile = Image.new('RGB',(530,700),'#e5e7eb')
        tile.paste(thumb,((530-thumb.width)//2,20))
        ImageDraw.Draw(tile).text((15,680),f'Page {i+1}',fill='black')
        thumbs.append(tile)
    for j in range(0,len(thumbs),6):
        group = thumbs[j:j+6]
        sheet = Image.new('RGB',(1590,1400),'white')
        for k,thumb in enumerate(group): sheet.paste(thumb,((k%3)*530,(k//3)*700))
        sheet.save(pdf.parent/f'contact-{j//6+1}.png')
    reports.append({'file':pdf.name,'pages':pages})
    (pdf.parent/'extracted.txt').write_text('\n\n'.join(p.extract_text() or '' for p in reader.pages),encoding='utf-8')
(root/'tmp'/'qa'/'layout_report.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
for report in reports:
    print(report['file'],len(report['pages']),'pages')
    for p in report['pages']: print(p['page'],p['words'],' / '.join(p['first'][:2]),' END ',' / '.join(p['last'][-2:]))
