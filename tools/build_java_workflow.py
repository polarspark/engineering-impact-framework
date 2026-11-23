from pathlib import Path
import build_mla as mla
from java_workflow_content import PAGES
from diagram_assets import Diagram, GRAY

ROOT=Path(__file__).resolve().parents[1]

def diagrams():
    g=Diagram(840)
    g.node(40,30,600,180,'Customer and API','Order submission and retry')
    g.node(760,30,580,180,'Java order service','Spring Boot and PostgreSQL')
    g.node(1460,30,600,180,'Runtime evidence','Traces, errors, latency')
    g.path([(640,120),(760,120)]); g.path([(1340,120),(1460,120)])
    g.node(40,350,900,180,'Delivery evidence','Work, PR, CI, artifact and release IDs',GRAY)
    g.node(1160,350,900,180,'Outcome and cost evidence','Acceptance, defects, effort and ledger',GRAY)
    g.path([(1760,210),(1760,280),(1610,280),(1610,350)])
    g.node(570,670,960,140,'Sprint scorecard and decision','Join stable work and release identifiers')
    g.path([(490,530),(490,600),(800,600),(800,670)])
    g.path([(1610,530),(1610,600),(1300,600),(1300,670)])
    g.save('java_evidence')
    g=Diagram(720)
    for x,title,body in [(30,'Java PR','Work ID and commit SHA'),(560,'Verify','Build and configured tests'),(1090,'Security','Required scan and policy'),(1620,'Review','Human review\nEvidence complete')]:
        g.node(x,40,450,190,title,body)
        if x<1600: g.path([(x+450,135),(x+530,135)])
    g.node(1180,410,890,190,'Controlled release','Artifact digest, availability and acceptance')
    g.path([(1845,230),(1845,410)])
    g.node(30,410,890,190,'Correct and repeat','Retain failed results and correction effort',GRAY)
    g.path([(780,230),(780,320),(475,320),(475,410)])
    g.path([(30,505),(10,505),(10,135),(30,135)])
    g.text(1050,320,'Failed or missing check',38)
    g.text(1050,680,'A missing required result prevents the normal release path',42,True)
    g.save('java_pipeline')

def build():
    mla.REFERENCES.update({
      'SPRING':('"Testing Spring Boot Applications"','"Testing Spring Boot Applications." *Spring Boot*, https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html. Accessed 23 Nov. 2026.'),
      'MAVEN':('"Apache Maven Surefire"','"Apache Maven Surefire." *Apache Maven*, Apache Software Foundation, https://maven.apache.org/surefire/. Accessed 23 Nov. 2026.'),
      'OTEL':('"Instrumentation Ecosystem"','"Instrumentation Ecosystem." *OpenTelemetry*, https://opentelemetry.io/docs/languages/java/instrumentation/. Accessed 23 Nov. 2026.'),
    })
    diagrams(); mla.used.clear()
    d=mla.document('Engineering Impact Framework Java Application Workflow')
    for i,(title,items) in enumerate(PAGES):
        if i: mla.heading(d,title,new_page=True)
        step=0
        for item in items:
            if item[0]=='i': mla.figure(d,*item[1:])
            elif item[0]=='n':
                step+=1
                p=mla.para(d,str(step)+'. '+item[1],indent=False)
                p.paragraph_format.left_indent=mla.Inches(.25)
                p.paragraph_format.first_line_indent=mla.Inches(-.25)
            elif item[0]=='b': mla.para(d,item[1],'List Bullet',False)
            else: mla.para(d,item[1])
    mla.used.update(['HARDING','S3','S6','S8','S9','SPRING','MAVEN','OTEL'])
    mla.works_cited(d)
    target=ROOT/'outputs'/'Engineering_Impact_Framework_Java_Workflow_MLA.docx'
    d.save(target); print(target)

if __name__=='__main__': build()
