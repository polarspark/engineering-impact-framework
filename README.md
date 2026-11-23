# Engineering Impact Framework

**Paul Harding, MBA ITM**

**PolarSpark LLC**

Version 1.2 | 23 November 2026

The Engineering Impact Framework (EIF) measures the value of adopting AI tools and changing software development workflows in normal application delivery. It uses three phases: **Baseline**, **Adoption**, and **Improvement**. Agile sprints provide the inspection cadence, while release, customer, and financial evidence can mature over longer observation windows.

## Documents

| Document | Read on GitHub | Download the MLA Word edition |
| --- | --- | --- |
| Framework: metric definitions, value calculations, maturity profiles, and NIST integration | [Framework](docs/framework.md) | [Framework DOCX](outputs/Engineering_Impact_Framework_MLA.docx) |
| Reusable sprint scorecards, stakeholder feedback, and evidence records T01 through T12 | [Templates](docs/templates.md) | [Templates DOCX](outputs/Engineering_Impact_Framework_Templates_MLA.docx) |
| Twenty page Java application workflow with tool examples and worked calculations | [Java workflow](docs/java-workflow.md) | [Java workflow DOCX](outputs/Engineering_Impact_Framework_Java_Workflow_MLA.docx) |

The Word editions use MLA formatting, author and company identification, in-text citations, and Works Cited sections. The Markdown editions preserve their content for browsing and version review; Word controls pagination. Workflow diagrams have editable SVG sources and print resolution PNGs in [assets/diagrams](assets/diagrams).

## Use the framework

1. Choose one application, service team, and proposed change. Record the initiative, current tools, hypothesis, owners, and permitted scope in T01.
2. Freeze metric definitions and evidence boundaries in T02. Start with time to accepted production value, delivery effort per comparable outcome, and realized net adoption value.
3. Establish Baseline with T03 and T06. Assess SDLC, documentation, and AI adoption separately in T09. Record applicable AI risks in T10.
4. Evaluate actual adoption through T04 and T07. Reconcile full costs and verified benefits in T11, then record the evaluation decision in T12.
5. Test a defined adjustment with T05 and T08. Compare the adjusted state with both the original baseline and the preceding adopted state.

Keep delivery, quality, security, business outcomes, customer feedback where appropriate, and developer experience visible together. Recovered hours are capacity until a financial benefit is verified. Never use lines of code, prompt counts, or story points as individual productivity ratings or dollar value.

## Foundations and interpretation

The framework draws on ISO/IEC/IEEE lifecycle and documentation references, DORA, SPACE, Scrum, NIST AI RMF, the NIST generative AI profile, and NIST SSDF. Detailed citations appear in each document. Public descriptions and abstracts were consulted for ISO standards. This is an original PolarSpark framework with proposed local metric extensions, formulas, maturity scoring, and forms. It does not establish certification or a clause by clause conformity assessment.

The Java workflow follows an illustrative Spring Boot order service through implementation, tests, PR review, security checks, controlled release, acceptance, sprint comparison, value reconciliation, and improvement. All worked observations and financial figures are synthetic teaching examples. The repository is documentation, not a deployed Java application or telemetry collector.

## Author

Paul Harding, MBA ITM, PolarSpark LLC. The author credential follows the name displayed on [Paul Harding’s LinkedIn profile](https://www.linkedin.com/in/pauldkharding/), checked on 23 November 2026. No additional certifications are asserted.

## Source and reproduction

Content and document builders are in [tools](tools). With Python and the packages in [requirements.txt](requirements.txt), run:

```text
python tools/diagram_assets.py
python tools/build_mla.py
python tools/build_java_workflow.py
python tools/prepare_publication.py
```

The image builders use Windows Calibri and Times New Roman fonts. `export_word.ps1` renders documents through Microsoft Word on Windows. The original build was visually reviewed after rendering; inspect new renders after changing content or formatting. Generated QA images and temporary PDFs are excluded from the repository.
