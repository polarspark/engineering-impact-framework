"""Deterministic SVG sources and print-resolution PNGs for EIF diagrams."""
from pathlib import Path
from xml.sax.saxutils import escape
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets' / 'diagrams'
ASSETS.mkdir(parents=True, exist_ok=True)
NAVY = '#243746'
TEAL = '#16656B'
TEXT = '#142631'
LINE = '#526875'
PALE = '#EEF5F5'
GRAY = '#F1F4F6'
GOLD = '#805813'


class Diagram:
    def __init__(self, height):
        self.height = height
        self.im = Image.new('RGB', (2100,height), 'white')
        self.d = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="2100" height="{height}" viewBox="0 0 2100 {height}">', '<rect width="100%" height="100%" fill="white"/>']

    def text(self,x,y,text,size=42,bold=False,color=TEXT,anchor='middle'):
        font = ImageFont.truetype('C:/Windows/Fonts/calibrib.ttf' if bold else 'C:/Windows/Fonts/calibri.ttf',size)
        lines = text.split('\n')
        lineheight = size*1.18
        for i,line in enumerate(lines):
            yy = y + (i-(len(lines)-1)/2)*lineheight
            self.d.text((x,yy),line,font=font,fill=color,anchor={'middle':'mm','start':'lm','end':'rm'}[anchor])
            self.svg.append(f'<text x="{x}" y="{yy}" text-anchor="{anchor}" dominant-baseline="central" font-family="Calibri,Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{escape(line)}</text>')

    def rect(self,x,y,w,h,fill=PALE,stroke=LINE):
        self.d.rounded_rectangle((x,y,x+w,y+h),radius=15,fill=fill,outline=stroke,width=3)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}" stroke="{stroke}" stroke-width="3"/>')

    def node(self,x,y,w,h,title,body='',fill=PALE):
        self.rect(x,y,w,h,fill)
        if body:
            self.text(x+w/2,y+52,title,46,True)
            self.text(x+w/2,y+(h+60)/2,body,40)
        else:
            self.text(x+w/2,y+h/2,title,44,True)

    def path(self,points,color=LINE,width=6,arrow=True,dashed=False):
        if dashed:
            for a,b in zip(points,points[1:]):
                dist=math.dist(a,b)
                for start in range(0,int(dist),24):
                    end=min(start+13,dist)
                    aa=tuple(a[j]+(b[j]-a[j])*start/dist for j in range(2))
                    bb=tuple(a[j]+(b[j]-a[j])*end/dist for j in range(2))
                    self.d.line((aa,bb),fill=color,width=width)
        else:
            self.d.line(points,fill=color,width=width,joint='curve')
        coords=' '.join(f'{x},{y}' for x,y in points)
        self.svg.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="{width}"'+(' stroke-dasharray="13 11"' if dashed else '')+'/>')
        if arrow:
            a,b=points[-2:]
            angle=math.atan2(b[1]-a[1],b[0]-a[0])
            pts=[b,(b[0]-23*math.cos(angle-.48),b[1]-23*math.sin(angle-.48)),(b[0]-23*math.cos(angle+.48),b[1]-23*math.sin(angle+.48))]
            self.d.polygon(pts,fill=color)
            self.svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="{color}"/>')

    def diamond(self,cx,cy,w,h,text):
        pts=[(cx,cy-h/2),(cx+w/2,cy),(cx,cy+h/2),(cx-w/2,cy)]
        self.d.polygon(pts,fill='#FFF7E8',outline=GOLD,width=4)
        self.svg.append('<polygon points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="#FFF7E8" stroke="{GOLD}" stroke-width="4"/>')
        self.text(cx,cy,text,42,True)

    def save(self,name):
        self.im.save(ASSETS/(name+'.png'),dpi=(300,300))
        (ASSETS/(name+'.svg')).write_text('\n'.join(self.svg+['</svg>']),encoding='utf-8')


def lifecycle():
    g=Diagram(600)
    for x,title,body in [(40,'1  Baseline','Record current delivery\nDefine the expected change'),(755,'2  Adoption','Introduce the change\nEvaluate outcomes and cost'),(1470,'3  Improvement','Adjust the workflow\nVerify sustained benefit')]:
        g.node(x,35,590,235,title,body)
    g.path([(630,153),(745,153)])
    g.path([(1345,153),(1460,153)])
    g.path([(1765,270),(1765,410),(1050,410),(1050,280)],TEAL)
    g.text(1430,465,'Evaluate each new adjustment',42,bold=True,color=TEAL)
    g.path([(335,270),(335,535),(2040,535)],dashed=True,arrow=False,width=4)
    g.text(1190,570,'Retain the original baseline for cumulative comparison',40)
    g.save('eif_lifecycle')


def delivery():
    g=Diagram(650)
    xs=[35+345*i for i in range(6)]
    labels=[('Commitment','Work accepted\ninto delivery'),('Develop','Code and\ndocumentation'),('Review','Human review\nand correction'),('Verify','Tests and\nsecurity checks'),('Production','Change available\nin the service'),('Acceptance','Business outcome\naccepted')]
    for x,(title,body) in zip(xs,labels):
        g.node(x,30,300,190,title,body)
    for x in xs[:-1]: g.path([(x+300,125),(x+335,125)],width=5)
    g.path([(185,310),(1910,310)],TEAL,width=5)
    g.text(1050,270,'M01  Commitment to the later of availability and acceptance',42,True,color=TEAL)
    g.path([(680,220),(680,240)],dashed=True,arrow=False,width=4)
    g.path([(680,335),(680,460)],dashed=True,arrow=False,width=4)
    g.text(650,425,'Code commit',38,anchor='end')
    g.path([(680,470),(1565,470)],width=5)
    g.text(1150,520,'M04  Code commit to successful production deployment',40,True)
    g.text(1050,610,'Corrections and defects link back to the originating work and release',39)
    g.save('delivery_measurement')


def value():
    g=Diagram(650)
    g.node(35,25,580,290,'Verified benefits','Cost reductions\nAvoided expenditure\nIncremental contribution')
    g.text(690,170,'-',80,True)
    g.node(770,25,580,290,'Incremental cost','Tooling and inference\nIntegration and learning\nReview and controls')
    g.text(1425,170,'=',70,True)
    g.node(1510,25,555,290,'Realized net value','Benefits less cost\nROI = net value / cost\nx 100 percent')
    g.node(35,390,975,190,'Recovered capacity','Hours and potential equivalent\nTrack separately from realized benefit',GRAY)
    g.node(1090,390,975,190,'Quality and risk limits','Must pass independently\nof financial value',GRAY)
    g.text(1050,625,'Reconcile overlapping benefits and include transition costs',40,bold=True)
    g.save('value_recognition')


def oversight():
    g=Diagram(1200)
    g.rect(35,20,2030,115,NAVY,NAVY)
    g.text(1050,76,'GOVERN  Policies permissions and accountability apply throughout',44,True,'white')
    g.node(35,210,525,200,'Define task and limits','Data and approved use\nPermissions and consequences')
    g.node(790,210,525,200,'AI proposes changes','Code tests or documentation\nWithin the permitted scope')
    g.node(1540,210,525,200,'Review and verify','Human review and required\nquality and security checks')
    g.text(297,165,'MAP',40,True,color=TEAL)
    g.text(1802,165,'MEASURE',40,True,color=TEAL)
    g.path([(560,310),(780,310)])
    g.path([(1315,310),(1530,310)])
    g.path([(1802,410),(1802,520)])
    g.diamond(1802,650,450,250,'Evidence\nsufficient?')
    g.node(790,545,525,210,'Release in scope','Required approval recorded\nUse normal release controls')
    g.node(35,545,525,210,'Monitor and learn','Incidents and feedback\nInform the next adjustment')
    g.text(1052,805,'MANAGE',40,True,color=TEAL)
    g.text(297,805,'MANAGE',40,True,color=TEAL)
    g.path([(1577,650),(1325,650)],TEAL)
    g.text(1445,605,'Pass',40,True,color=TEAL)
    g.path([(790,650),(570,650)],TEAL)
    g.path([(1802,775),(1802,930)],GOLD)
    g.text(1802,855,'Fail or unknown',40,True,color=GOLD)
    g.node(1540,940,525,190,'Correct or fall back','Record failed evidence\nRetain the approved scope',GRAY)
    g.path([(2065,1035),(2085,1035),(2085,175),(2015,175),(2015,200)],GOLD)
    g.text(1050,1165,'Incident or policy breaches trigger the existing response process immediately',39)
    g.save('ai_review_release')


def templates():
    g=Diagram(960)
    g.node(35,25,2030,115,'Define the initiative and measures  T01 and T02')
    g.path([(1050,140),(1050,205)],arrow=False)
    g.path([(335,205),(1765,205)],arrow=False)
    for x,c,title,body in [(35,335,'1  Baseline','T03 sprint scorecard\nT06 stakeholder feedback'),(750,1050,'2  Adoption','T04 sprint scorecard\nT07 stakeholder feedback'),(1465,1765,'3  Improvement','T05 sprint scorecard\nT08 stakeholder feedback')]:
        g.path([(c,205),(c,265)])
        g.node(x,275,600,185,title,body)
        g.path([(c,460),(c,540)])
    g.node(35,550,2030,145,'Update shared evidence','T09 maturity     T10 AI risk     T11 cost and benefit')
    g.path([(1050,695),(1050,775)])
    g.node(595,785,910,115,'T12  Decide and assign the next action')
    g.text(1050,940,'Carry the decision and open actions into the next sprint',40,True)
    g.save('template_handoffs')


if __name__=='__main__':
    lifecycle(); delivery(); value(); oversight(); templates()
    print('Created five SVG sources and five print-resolution PNG images in',ASSETS)
