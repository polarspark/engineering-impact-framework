method_pages = [
{'heading':'Value calculations and recognition rules','items':[
 ('p','Maintain three separate benefit views. The financial view recognizes verified incremental benefits. The capacity view reports effort released for other work. The strategic and risk view records outcomes that cannot yet be valued credibly. Never add these views without reconciling overlaps.'),
 ('h','Recovered capacity'),
 ('p','Estimate task capacity as comparable baseline effort per task minus post-change effort per task, multiplied by eligible post-change task volume. Include prompting, review, correction, QA, and documentation effort. Retain negative results. Apply a work-mix adjustment when task composition differs.'),
 ('p','A loaded hourly rate may translate recovered hours into a capacity-equivalent amount. Label it as potential capacity value. It is not cash savings unless expenditure actually changes. Track the work to which capacity was reassigned and the outcome that work produced.'),
 ('h','Realized financial value'),
 ('p','Gross realized benefit is the sum of non-overlapping verified cost reductions, documented avoided expenditures, and attributable incremental business contribution. Use contribution after relevant variable costs, rather than gross revenue. Benefit owners must identify evidence, comparison, realization date, and attribution basis.'),
 ('p','Net realized value is gross realized benefit minus total incremental adoption cost over the same window. Realized ROI is net realized value divided by incremental adoption cost, multiplied by 100. When cost is zero, ROI is undefined and net value is still reported.'),
 ('h','Total incremental adoption cost'),
 ('p','Include subscriptions, inference, platform support, integration, training time, transition disruption, evaluation, security and governance work, incremental review, remediation, and exit cost where incurred. Record one-time and recurring amounts separately. Avoid subtracting a cost twice if it already reduced the contribution calculation.'),
 ('p','Report both cash and economic cost bases when useful. Economic cost includes documented internal effort at agreed rates. Keep the basis consistent in numerator and denominator. Existing sunk cost is identified separately and does not become an incremental cost merely because the initiative is measured.'),
 ('p','For payback, report the first period when cumulative verified benefits cover cumulative incremental costs. A forecast payback requires explicit future assumptions and must be labeled forecast. Do not annualize one favorable sprint as a realized annual benefit.')
]},
{'heading':'Worked adoption value example','items':[
 ('p','Illustrative scenario only. The following figures demonstrate calculations over an eight-week evaluation window. They are assumptions, not observations or industry benchmarks. Comparable maintenance outcomes and equal follow-up are assumed.'),
 ('t',['Measure','Baseline','Post change','Interpretation'],[
 ['Accepted outcomes','40','40','Equal volume assumed'],
 ['Total delivery effort','800 h','640 h','20 h to 16 h per outcome'],
 ['Recovered effort','','160 h','800 h minus 640 h'],
 ['Capacity equivalent at USD 100 per hour','','USD 16,000','Reported outside realized benefit'],
 ['Median M01 for adopter','10 days','8 days','20 percent observed reduction'],
 ['Median M01 for comparison','10 days','9.5 days','5 percent observed reduction']],[2.45,1.0,1.0,2.55],True),
 ('p','The adopter change is minus two days. The comparison change is minus half a day. The adjusted change is minus one and a half days, equivalent to 15 percent of the adopter baseline. This is an illustrative adjusted contrast; causal interpretation still requires credible allocation, comparable trends, and no material differential changes.'),
 ('t',['Eight week economic ledger','Amount','Recognition'],[
 ['Verified avoided contractor expenditure','USD 12,000','Documented canceled incremental purchase'],
 ['Attributable incremental contribution','USD 18,000','Business owner verified after variable costs'],
 ['Gross realized benefit','USD 30,000','Non-overlapping benefits assumed'],
 ['Recurring tool cost','USD 6,000','Included cost'],
 ['Integration effort','USD 8,000','Included one-time economic cost'],
 ['Training effort','USD 8,000','Included one-time economic cost'],
 ['Evaluation and governance','USD 2,000','Included cost'],
 ['Total incremental cost','USD 24,000','Common economic basis'],
 ['Net realized value','USD 6,000','USD 30,000 less USD 24,000'],
 ['Realized ROI','25 percent','USD 6,000 divided by USD 24,000']],[3.0,1.05,2.95],True),
 ('p','The USD 16,000 capacity equivalent is excluded from the USD 30,000 benefit total. Contractor avoidance and incremental contribution must have different benefit evidence or a documented allocation that prevents duplicate claims. Training and integration effort must also be excluded from the operational effort comparison if already recognized separately here.')
]},
{'heading':'Value ledger and sensitivity','items':[
 ('h','Recognition and verification'),
 ('p','Give each benefit an ID and an overlap key linking it to the underlying capacity, expenditure, customer outcome, or avoided event. Record proposed, forecast, verified realized, rejected, and pending states. Only verified realized rows enter realized ROI. Preserve rejected and negative results for review.'),
 ('p','Assign shared benefits across initiatives using a documented rule whose total does not exceed the full benefit. A single outcome cannot be recognized in full by the AI tool initiative, the workflow initiative, and the platform initiative simultaneously.'),
 ('h','Use scenarios for uncertain inputs'),
 ('t',['Illustrative scenario','Benefit','Cost','Net value','ROI'],[
 ['Lower benefit case','USD 18,000','USD 28,000','USD -10,000','-35.7 percent'],
 ['Worked example','USD 30,000','USD 24,000','USD 6,000','25.0 percent'],
 ['Higher benefit case','USD 42,000','USD 22,000','USD 20,000','90.9 percent']],[1.7,1.27,1.27,1.4,1.36],True),
 ('p','These cases vary assumed benefit and cost and are not statistical confidence intervals. In actual reporting, replace each assumption with its source and explain why it could vary. Forecast cases remain separate from verified actuals.'),
 ('h','Risk reduction and avoided incidents'),
 ('p','Report security exposure and control changes directly. If a risk model estimates avoided expected loss, show event probability, impact assumptions, time horizon, uncertainty, and the risk owner. Keep the result in a modeled risk-benefit view. An absence of incidents does not establish realized avoided loss.'),
 ('h','Value that is not yet monetary'),
 ('p','Retain evidence of faster learning, better documentation, improved accessibility, customer trust, and reduced toil. Report the measured outcome and decision relevance. Do not invent a dollar conversion to force every benefit into ROI.'),
 ('p','Review value by sprint for operational learning and by a longer agreed window for investment decisions. Keep transition cost in the cumulative view even after a steady-operation view becomes available.')
]},
{'heading':'Maturity scoring method','items':[
 ('p','Assess SDLC practice, documentation, and AI adoption as three separate profiles. This is a proposed internal rubric informed by the cited standards and guidance. It is not an official NIST maturity model, a CMMI rating, or an ISO conformity assessment.'),
 ('t',['Level','Meaning','Evidence required'],[
 ['0','Absent','Assessment confirms the practice or required evidence is absent.'],
 ['1','Ad hoc','Some practice exists, but ownership, scope, or repeatability is inconsistent.'],
 ['2','Defined','Applicable scope, owner, documented procedure, and expected evidence are established.'],
 ['3','Verified in operation','Level 2 plus sampled operating evidence across the assessment window shows the procedure is used and exceptions are managed.'],
 ['4','Measured and improved','Level 3 plus outcome measures, a completed improvement cycle, and follow-up showing the intended effect.'],
 ['U','Unassessed','Evidence is unavailable or has not been evaluated. Do not assign zero.'],
 ['NA','Not applicable','The assessor and accountable owner record the rationale and approval.']],[.55,1.55,4.9]),
 ('h','Assign domain levels'),
 ('p','Use the domain evidence on the following pages with the common level anchors above. Award the highest cumulative level for which all applicable domain conditions are supported. Level 3 requires at least two complete sprints of operating evidence plus a relevant release or exercise when applicable. This is a starting assessment convention and may be tailored before assessment.'),
 ('p','For each domain, record evidence links, sample size and selection, date, assessor, owner, exceptions, and next action. When a required domain condition remains unassessed, report the domain as U and state what is missing.'),
 ('h','Summarize without hiding gaps'),
 ('p','Default to equal domain weights within each profile. The profile index is the sum of scored domain levels divided by four times the number of scored domains, multiplied by 100. Report assessment coverage as scored domains divided by applicable domains. Exclude approved NA domains from both counts. With no scored domains, the index is undefined.'),
 ('p','Example: six applicable domains with scores 3, 2, 2, 1, 3, and U produce 11 divided by 20, or a 55.0 index, at 83.3 percent coverage. Publish both figures and the U domain. Keep critical gaps listed separately; no average can authorize an otherwise prohibited use.')
]},
{'heading':'SDLC maturity profile','items':[
 ('p','Apply the common 0 to 4 anchors to each domain. The following evidence distinguishes a defined practice from verified use and measured improvement. These local domains use lifecycle concepts from ISO/IEC/IEEE 12207 [S1] and secure development guidance [S9].'),
 ('t',['Domain','Level 2 evidence','Level 3 evidence','Level 4 evidence'],[
 ['Planning and requirements','Named product owner, work classification, acceptance rules, and commitment definition','Sampled work meets the rules; scope changes and acceptance decisions are retained','Planning or acceptance change improves measured predictability or outcome'],
 ['Architecture and development','Review procedure, design decision ownership, coding rules, and dependency policy','Sampled changes have appropriate review and traceable design decisions','A completed change reduces relevant review, maintenance, or integration problems'],
 ['Verification and quality','Risk-based testing expectations, defect handling, and Definition of Done','Required tests run; failures and exceptions are tracked; escaped defects are linked','Measured correction reduces escaped defects or ineffective test effort'],
 ['Secure delivery','Threat and vulnerability process, required checks, accountable security owner','Applicable checks and remediation records are verified; bypasses are visible','Security improvement reduces exposure with stable or better detection'],
 ['Release and operations','Deployment, rollback, recovery, ownership, and service objectives defined','Release evidence and recovery exercise or incident response verified','Operational improvement demonstrates better recovery or reliability'],
 ['Learning and measurement','Metric definitions, owners, retrospective actions, and evaluation schedule','Scorecards reconcile to sources and actions are followed through','Completed improvement has follow-up evidence and informs the next change']],[1.13,1.92,1.98,1.97],True),
 ('h','Critical conditions'),
 ('p','Before adopting a use that can affect production, identify any missing required review, access control, deployment recovery, or incident ownership. Use the organization risk policy to decide whether the condition blocks that use. The maturity index provides context and cannot waive a required control.'),
 ('p','Reassess at phase transitions and after meaningful operating changes. During sprints, update evidence and actions rather than changing a maturity level merely because a document was created.')
]},
{'heading':'Documentation maturity profile','items':[
 ('p','Define required information by service risk and lifecycle stage, using ISO/IEC/IEEE 15289 as a documentation reference [S2]. Assess usefulness and accuracy as well as existence. Each domain uses the common level anchors.'),
 ('t',['Domain','Defined at level 2','Verified at level 3','Improved at level 4'],[
 ['Requirements and acceptance','Owned requirements, scope, and acceptance criteria linked to work','Sampled requirements match delivered behavior and acceptance evidence','Reduced clarification or rejection effort is demonstrated'],
 ['Architecture and decisions','Owned system descriptions and material decision records','Current components, dependencies, and tradeoffs verified against the service','Knowledge tasks or maintenance outcomes improve'],
 ['Development and interfaces','Build, local setup, interfaces, and dependency guidance defined','A reviewer or new engineer can follow the guidance successfully','Measured setup or integration effort improves'],
 ['Testing and quality','Test intent, execution evidence, and defect traceability defined','Sampled test evidence is relevant and reproducible','Documentation contributes to better diagnosis or defect prevention'],
 ['Security and AI use','Threats, approved AI uses, data rules, limitations, and decisions recorded','Sampled security and AI records match actual configuration and use','Measured gaps are reduced and affected teams can apply guidance'],
 ['Operations and recovery','Runbooks, ownership, release and rollback instructions defined','Relevant operational or recovery task succeeds using the current runbook','Recovery or support task success improves and is sustained']],[1.17,1.91,2.02,1.9],True),
 ('h','Inventory and validity'),
 ('p','For every required information item, retain its owner, service version or applicability, location, review trigger, validity period, and verification result. A material code, architecture, permission, or deployment change triggers review of affected information.'),
 ('p','M23 reports verified coverage and M24 tests practical usefulness. When prose is generated by AI, verify technical claims, sources where relevant, and alignment with actual behavior. Generated volume earns no maturity credit. Audit artifacts may share a repository with code if ownership and access are clear.')
]},
{'heading':'AI adoption maturity profile','items':[
 ('p','Assess the organization ability to use AI responsibly within the SDLC. The domains below are local scoring categories aligned to NIST AI RMF functions [S6, S7]. NIST does not prescribe these numeric levels or thresholds.'),
 ('t',['Domain','Defined at level 2','Verified at level 3','Improved at level 4'],[
 ['Governance and capability','Approved uses, accountable owners, training, supplier review, and escalation defined','Sampled users and configurations follow policy; exceptions and training are evidenced','Measured policy or training improvement reduces a recurring problem'],
 ['Use context and impact','Task, affected people, data, privileges, dependencies, and risk tolerance documented','Actual use and access match the documented scope; impacts reviewed with relevant roles','Context changes are detected and lead to tested scope or control improvements'],
 ['Evaluation and oversight','Evaluation set, acceptance rubric, human review, limitations, and monitoring defined','Representative tests and human review records verify behavior in the approved context','Evaluation gaps are corrected and follow-up shows improved detection or outcomes'],
 ['Treatment and continuity','Risk treatment, incident handling, fallback, supplier change, and retirement defined','Relevant response or fallback is exercised and residual risk decisions are retained','Incident lessons or drift findings lead to a verified reduction in recurrence or impact']],[1.2,1.9,2.0,1.9],True),
 ('h','Assess capability separately from adoption volume'),
 ('p','A widely deployed tool may have weak governance, and a narrowly used tool may have strong controls. Report adoption exposure M18 next to maturity, without turning adoption volume into a maturity score. Record proficiency and workflow fit through training evidence and observed work quality.'),
 ('h','Apply proportional controls'),
 ('p','A code suggestion reviewed before merge has a different consequence and permission profile from an agent that edits repositories, runs commands, or deploys changes. Define the permitted actions, approval boundary, and containment plan for each use. Extend evaluation when AI is embedded in the delivered product or affects customer decisions.')
]},
{'heading':'NIST AI adoption integration','items':[
 ('p','Use AI RMF 1.0 and its Playbook as the AI risk foundation [S6, S7]. GOVERN, MAP, MEASURE, and MANAGE operate throughout all three phases. They are not a one-to-one sequence of phase gates. The following is a proposed implementation mapping, with selected category references for traceability.'),
 ('t',['Function','Phase 1','Phase 2','Phase 3'],[
 ['GOVERN','Assign risk owners, approved uses, training, and risk tolerance','Verify operating responsibilities, training, and exceptions','Review policy, suppliers, and capability as scope changes'],
 ['MAP','Describe tasks, users, data, permissions, benefits, and potential harms','Compare actual use with intended use and review affected groups','Remap context and impact for the proposed adjustment'],
 ['MEASURE','Select evaluations, baseline measures, limitations, and review criteria','Run representative evaluations and monitor outcomes and incidents','Repeat affected evaluations and test whether changes improve outcomes'],
 ['MANAGE','Choose treatments, decision authority, fallback, and incident process','Act on findings, constrain unsafe uses, and record residual risk','Update treatments, monitor persistence, or retire unsuitable uses']],[.86,2.05,2.05,2.04],True),
 ('h','Traceability to selected outcomes'),
 ('p','T01 and T10 support GOVERN 2.1 and 2.2 for responsibility and training, MAP 1.1 and 1.4 for context and business purpose, MEASURE 2.1 and 2.3 for documented and relevant evaluation, and MANAGE 4.1 and 4.2 for monitoring and improvement [S7]. These are selected mappings, not a claim of full coverage.'),
 ('h','Generative AI and secure development'),
 ('p','Use NIST AI 600-1 to extend the risk review for generative AI [S8]. Relevant considerations include unreliable output, data privacy, information security, intellectual property, harmful bias, human reliance, and dependencies across suppliers and components. Tailor relevance to the use case.'),
 ('p','Use SSDF for the secure development process [S9]. SP 800-218A adds AI model development considerations and is particularly relevant when producing models or systems that use them [S10]. Buying an AI coding assistant does not mean the organization is training a foundation model.'),
 ('p','As of November 23 2026, NIST states that AI RMF 1.0 is under revision. Record the applied version and review changes at the next framework refresh. The Playbook is voluntary guidance, not a mandatory checklist. The local maturity scores and ROI formulas remain organizational conventions.')
]},
{'heading':'AI risk evaluation and adoption decisions','items':[
 ('h','Build a use case evaluation set'),
 ('p','Include representative work, difficult cases, known failure modes, and cases involving sensitive context or privileged actions where relevant. Define expected behavior and pass criteria before execution. Retain tool configuration, known model version, evaluator, date, repeated trials, failures, and limits of generalization. Keep held-out cases separate from examples used to tune the workflow.'),
 ('t',['Risk scenario','Example evaluation or control evidence'],[
 ['Incorrect code or invented APIs','Compile, test behavior, inspect edge cases, and verify dependencies and claims'],
 ['Weak generated tests','Check meaningful assertions, negative cases, and relevant defect detection'],
 ['Data exposure','Verify approved data handling and test redaction or access boundaries using permitted test data'],
 ['Malicious repository context','Evaluate whether untrusted instructions can redirect privileged actions'],
 ['Unapproved actions','Verify least privilege, required human approval, audit events, and containment'],
 ['Supplier or model change','Record version changes, repeat affected evaluations, and exercise fallback'],
 ['Unequal or harmful outcomes','Where relevant, inspect accessibility, language, group effects, and affected-user feedback']],[1.65,5.35]),
 ('h','Decision conditions'),
 ('p','Expand only when the intended outcome has adequate evidence, the benefit meets the locally agreed threshold, and applicable controls and risk limits pass. If outcomes are immature or data are incomplete, record a bounded observation decision. If a critical failure occurs, restrict the affected use and invoke the established incident process immediately.'),
 ('p','Record residual risks, owner, rationale, permitted scope, conditions, expiration date, and next review. A sponsor benefit preference cannot silently waive required policy. The designated authority decides exceptions under existing organizational rules.'),
 ('h','Definition of Done extensions'),
 ('p','For affected work, require reviewed code and documentation, relevant tests, security evidence, traceable dependencies, required approvals, and operational recovery information. For AI-specific work, include the applicable evaluation and known limitations. Tailor these requirements to the work rather than applying every evaluation to every change.')
]},
{'heading':'Implementation and reporting plan','items':[
 ('h','Initial setup'),
 ('p','Choose one real delivery workflow and an accountable service team. Register an initiative, complete T01, and tailor T02. Use existing work tracking, version control, CI, security, finance, and product sources before building additional collection. Collect only what will inform a decision.'),
 ('t',['Operating period','Expected work and output'],[
 ['Baseline sprints','T03 and T06; establish normal variation, work mix, data coverage, and maturity evidence'],
 ['Adoption and learning','T04 and T07; track actual exposure, all transition costs, evaluations, and early problems'],
 ['Evaluation checkpoint','T11 and T12; compare outcomes and costs and decide the next permitted scope'],
 ['Adjustment sprints','T05 and T08; test a defined change and compare marginal and cumulative effects'],
 ['Periodic review','Refresh T09 and T10; verify sustained value, critical gaps, and standard versions']],[1.55,5.45]),
 ('h','Publish a useful sprint record'),
 ('p','Show the three primary measures, selected diagnostics, sample sizes, work mix, exposure, cost, stakeholder findings, critical risks, and the next action. Give each result a factual status: observed, provisional, unavailable, or verified realized for value. Keep target attainment separate from evidence sufficiency.'),
 ('p','Continue deployment and security measurement across sprint boundaries. Sprint completion is not a required production release boundary. Release and customer outcomes can be reviewed on their own cadence and linked back to the relevant initiative.'),
 ('h','Maintain the framework'),
 ('p','The framework owner keeps metric definitions, templates, maturity anchors, and source versions under change control. Changes apply prospectively unless a documented correction requires historical restatement. Retain previous calculation versions and record the effect of any restatement.'),
 ('p','Before broad rollout, validate the chosen workflow against a sample of source records, independently recompute value, and complete one scorecard in each phase. Use that operational check to remove unnecessary collection and resolve ambiguous definitions.')
]},
{'heading':'Source register and version notes','items':[
 ('p','Sources were checked on November 23 2026. References support the stated concepts. The metric extensions, phase gates, templates, and maturity scoring are proposed implementation choices. ISO references use publicly available abstracts and descriptions; this document does not reproduce or claim a clause-level audit of the paid standards.'),
 ('l','S1 ISO IEC IEEE 12207 2026 Software life cycle processes','https://www.iso.org/standard/90219.html'),
 ('p','Lifecycle process reference. Published April 2026 and replaces the 2017 edition.'),
 ('l','S2 ISO IEC IEEE 15289 2019 Lifecycle documentation','https://www.iso.org/standard/74909.html'),
 ('p','Information item reference. ISO states that the 2019 edition was confirmed in 2025.'),
 ('l','S3 DORA Software delivery performance metrics','https://dora.dev/guides/dora-metrics/'),
 ('p','Five production delivery measures and application-level interpretation.'),
 ('l','S4 SPACE Developer productivity research','https://www.microsoft.com/en-us/research/publication/the-space-of-developer-productivity-theres-more-to-it-than-you-think/'),
 ('p','Forsgren and coauthors, ACM Queue, 2021. Supports multidimensional productivity assessment.'),
 ('l','S5 Scrum Guide 2020','https://scrumguides.org/scrum-guide.html'),
 ('p','Sprint inspection, adaptation, goals, accountabilities, and Definition of Done.'),
 ('l','S6 NIST AI 100 1 AI Risk Management Framework 1 0','https://www.nist.gov/itl/ai-risk-management-framework'),
 ('p','Voluntary AI risk framework. NIST identifies an active revision; this document uses the published 1.0 structure.'),
 ('l','S7 NIST AI RMF Core and Playbook','https://airc.nist.gov/airmf-resources/airmf/5-sec-core/'),
 ('l','S7a GOVERN suggested actions','https://airc.nist.gov/airmf-resources/playbook/govern/'),
 ('l','S7b MAP suggested actions','https://airc.nist.gov/airmf-resources/playbook/map/'),
 ('l','S7c MEASURE suggested actions','https://airc.nist.gov/airmf-resources/playbook/measure/'),
 ('l','S7d MANAGE suggested actions','https://airc.nist.gov/airmf-resources/playbook/manage/'),
 ('p','Use category references for traceability and tailor suggested actions to the actual AI use case.')
]},
{'heading':'Source register continued','items':[
 ('l','S8 NIST AI 600 1 Generative Artificial Intelligence Profile','https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf'),
 ('p','Published July 2024. Companion profile for generative AI risks and suggested actions. Relevant examples include confabulation, information security, privacy, human interaction, and component dependencies.'),
 ('l','S9 NIST SP 800 218 SSDF version 1 1','https://csrc.nist.gov/pubs/sp/800/218/final'),
 ('p','Final secure development guidance, February 2022. Used for development practice expectations.'),
 ('l','S10 NIST SP 800 218A AI SSDF Community Profile','https://csrc.nist.gov/pubs/sp/800/218/a/final'),
 ('p','Final July 2024. Adds practices concerning AI model development and relevant AI systems, used with SSDF.'),
 ('l','S11 NIST SSDF publication status','https://csrc.nist.gov/Projects/ssdf/publications'),
 ('p','As checked, SSDF 1.2 is listed as draft and SSDF 1.1 as final. A draft must not silently replace the approved reference.'),
 ('h','Framework change record'),
 ('t',['Version','Date','Change'],[
 ['1.0','November 23 2026','Initial framework with three phases, 28 metrics, value calculations, maturity profiles, NIST mapping, and companion templates.']],[.65,1.4,4.95]),
 ('h','Local adoption record'),
 ('p','Before operational use, assign the framework owner, approving authority, organizational scope, next review date, approved metric versions, and local risk policies. Record any departures from these proposed conventions in the adoption contract and metric definitions.'),
 ('p','When referenced standards or vendor behavior change, assess the effect on measurement comparability, evaluation coverage, and operating controls. Update the framework deliberately and retain the earlier version for historical interpretation.')
]}
]
