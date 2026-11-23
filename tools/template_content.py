from copy import deepcopy

templates = [
{'title':'Sprint Scorecards and Stakeholder Templates','items':[
 ('p','Reusable forms for the AI and SDLC Adoption Value Framework. Version 1.0, November 23 2026. Copy a fresh form for each initiative, sprint, assessment, or decision. Replace bracketed prompts with local records. Preserve earlier versions.'),
 ('p','Metric IDs M01 to M28 refer to the definitions in the framework document. These are editable Word forms for manual completion. Calculations are not automated. Complete the numerator, denominator, sample, source, and period fields before interpreting a result.'),
 ('t',['Template','Purpose','Phase'],[
 ['T01','Adoption contract and readiness','1 and material changes'],
 ['T02','Metric definition record','All'],
 ['T03','Baseline sprint scorecard','1'],
 ['T04','Adoption sprint scorecard','2'],
 ['T05','Adjustment sprint scorecard','3'],
 ['T06','Baseline stakeholder feedback','1'],
 ['T07','Adoption stakeholder feedback','2'],
 ['T08','Adjustment stakeholder feedback','3'],
 ['T09','Maturity assessment','All checkpoints'],
 ['T10','AI use case and risk record','All'],
 ['T11','Cost and benefit ledger with value summary','All'],
 ['T12','Evaluation decision and improvement action','All checkpoints']],[.75,4.25,2.0]),
 ('h','Completion rules'),
 ('p','Use Not assessed until evidence is available. Distinguish zero, unavailable, provisional, and not applicable. A blank result never means a pass. Apply existing organizational security and release policies. Keep identifiable responses and sensitive technical evidence in their governed systems.'),
 ('p','Each scorecard should show the reporting window, data cutoff, intervention version, and sample coverage. Late acceptance, defects, and value verification may require a later revision. Retain a link to that revision in the original scorecard.')
],},
{'heading':'T01 Adoption contract','items':[
 ('f','Initiative ID and version','Enter ID, version, owner, and date',0),
 ('f','Application and team','Enter service, team, business sponsor, and scope',0),
 ('f','Problem and desired outcome','Describe the delivery problem and why improvement matters',1),
 ('f','Current practice','Record existing AI, tools, workflow, permissions, and relevant maturity gaps',1),
 ('f','Proposed change and hypothesis','State the change, expected mechanism, eligible work, and affected people',1),
 ('t',['Required planning field','Local definition'],[
 ['Baseline window','[Sprints and dates]'],
 ['Learning and evaluation windows','[Dates, cutoff, and outcome follow-up]'],
 ['Eligible work and comparison','[Classification, assignment rule, exclusions, and rationale]'],
 ['Primary measures','[M01 M02 M03 and locally justified thresholds]'],
 ['Diagnostics and guardrails','[Selected IDs, boundaries, and breach response]'],
 ['Cost and benefit boundaries','[Currency, period, rate source, expected benefits, and overlap rule]'],
 ['Known concurrent changes','[Staffing, incidents, releases, or other tooling]'],
 ['Fallback and exit criteria','[How to restrict or stop the use and who acts]']],[2.1,4.9]),
 ('f','Local framework departures','Record changed conventions and their effective dates',0)
]},
{'heading':'T01 Readiness and authorization record','items':[
 ('p','Complete before the affected adoption scope begins. Reuse this page when a material scope or permission change occurs. These are local organizational decision fields, not a NIST certification checklist.'),
 ('f','Initiative and proposed scope','Enter initiative version and permitted actions',0),
 ('t',['Readiness condition','Evidence and owner','Result'],[
 ['Baseline and data gaps understood','[Link and owner]','Not assessed'],
 ['Eligible work and comparison defined','[Link and owner]','Not assessed'],
 ['Business outcome and thresholds defined','[Link and owner]','Not assessed'],
 ['Approved AI use and data handling','[T10 link and owner]','Not assessed'],
 ['Permissions and oversight boundary','[T10 link and owner]','Not assessed'],
 ['Required testing and security controls','[Evidence and owner]','Not assessed'],
 ['Training and support available','[Evidence and owner]','Not assessed'],
 ['Fallback and incident handling defined','[Evidence and owner]','Not assessed'],
 ['Costs and evaluation ownership assigned','[T11 link and owner]','Not assessed']],[2.7,3.05,1.25]),
 ('f','Open conditions or exceptions','State consequence, authority, expiry, and permitted scope',2),
 ('f','Decision','Proceed within stated scope, resolve conditions, or do not proceed',0),
 ('f','Accountable owners and decision date','Record delivery, product, metric, security, AI risk, and finance owners as applicable',1),
 ('f','Next review','Enter date and triggering events',0)
]},
{'heading':'T02 Metric definition record','items':[
 ('p','Copy one record per selected metric or local variant. Keep the prior definition when the meaning changes.'),
 ('f','Metric identity','Enter metric ID, name, version, and owner',0),
 ('f','Decision supported','Explain what movement would cause the team to do',1),
 ('t',['Definition field','Local specification'],[
 ['Population and grain','[Eligible entities, service, work class, and one-row meaning]'],
 ['Calculation and unit','[Formula in words, numerator, denominator, and unit]'],
 ['Timing','[Start event, end event, window, timezone, and follow-up]'],
 ['Source and linkage','[Systems, stable IDs, joins, and de-duplication]'],
 ['Aggregation','[Rate method, duration percentiles, cohort rule, and sample count]'],
 ['Exclusions and unknowns','[Excluded cases, unknown handling, and not-applicable rule]'],
 ['Coverage and freshness','[Expected records, matched records, cutoff, and extraction lag]'],
 ['Threshold and guardrails','[Direction, practical threshold, risk limit, and rationale]'],
 ['Comparison and uncertainty','[Baseline, control group, variation, limitations, and analyst method]'],
 ['Change control','[Effective date, approver, and historical restatement rule]']],[2.0,5.0]),
 ('f','Worked calculation and validation','Include a representative record or arithmetic check and its source',2),
 ('f','Known limitations','Explain what the measure cannot establish',1)
]},
{'heading':'T03 Phase 1 baseline sprint scorecard','items':[
 ('f','Context','Initiative and current-state version; team; service; sprint; owner',0),
 ('f','Window and evidence','Start; end; timezone; cutoff; source snapshot; outcome follow-up',0),
 ('f','Work mix and capacity','Committed, added, removed, completed, accepted, open; classes; available capacity',0),
 ('f','Existing AI and other changes','Record exposure yes no unknown and concurrent operational changes',0),
 ('t',['ID','Measure','Sprint value','Window value','N or n/d','Evidence'],[
 ['M01','Time to accepted value','[Median p85]','[Median p85]','[N]','[Link]'],
 ['M02','Effort or cost per outcome','[Value]','[Value]','[Hours N]','[Link]'],
 ['M03','Adoption value status','Not evaluated','Not evaluated','[Scope]','[T11]'],
 ['[ID]','Delivery diagnostic','[Value]','[Value]','[N or n/d]','[Link]'],
 ['[ID]','Quality or security','[Value]','[Value]','[N or n/d]','[Link]'],
 ['[ID]','Experience or outcome','[Value]','[Value]','[N or n/d]','[Link]']],[.5,1.8,1.05,1.05,1.0,1.6],True),
 ('p','In Phase 1, record current cost and benefit boundaries in T11. M03 is not yet evaluated for the proposed change. Recompute window rates and percentiles from underlying records. N is sample count; n/d is numerator divided by denominator; p85 is the 85th percentile.'),
 ('t',['Required baseline evidence','Finding and next action'],[
 ['Data gaps and provisional cohorts','[Coverage, unmatched records, missingness, late outcomes]'],
 ['Maturity and critical gaps','[T09 profile indices, coverage, and critical conditions]'],
 ['Stakeholder feedback','[T06 roles, eligible counts, responses, and themes]'],
 ['AI risk readiness','[T10 open risks and required treatment]']],[2.0,5.0]),
 ('f','Baseline decision','Sufficient, extend collection, or restricted interpretation; rationale and owner',1),
 ('f','Next action and checkpoint','Action, accountable owner, due date, and evidence required',0)
]},
{'heading':'T04 Phase 2 adoption sprint scorecard','items':[
 ('f','Context','Initiative and intervention version; service; team; sprint; owner',0),
 ('f','Window and exposure','Dates; timezone; cutoff; learning or steady period; assigned group; actual and unknown exposure',0),
 ('f','Comparability','Work mix; capacity; concurrent changes; comparison group; source snapshot and follow-up',0),
 ('t',['ID','Measure','Baseline','Post change','N or n/d','Change'],[
 ['M01','Time to accepted value','[Median p85]','[Median p85]','[Both N]','[Days %]'],
 ['M02','Effort or cost per outcome','[Value]','[Value]','[Both N]','[Hours %]'],
 ['M03','Realized net value','[Boundary]','[Currency]','[T11]','[Cumulative]'],
 ['[ID]','Selected diagnostic','[Value]','[Value]','[Both]','[Unit]'],
 ['[ID]','Selected diagnostic','[Value]','[Value]','[Both]','[Unit]']],[.5,1.8,1.15,1.15,1.0,1.4],True),
 ('f','Comparison group and adjusted contrast','Show baseline and post values; compute same-unit changes; state assumptions',1),
 ('t',['Guardrail','Limit','Observed and evidence','Result'],[
 ['Quality and reliability','[Local limit]','[Value source]','Not assessed'],
 ['Security and AI risk','[Local limit]','[Value source]','Not assessed'],
 ['Review and human impact','[Local limit]','[Value source]','Not assessed']],[1.65,1.4,2.65,1.3],True),
 ('f','Value and stakeholder findings','T11 actual cost, capacity separately, verified benefit; T07 response counts and themes',1),
 ('f','Sprint response','Continue, restrict, adjust, or escalate; rationale, owner, and next checkpoint',0),
 ('p','State observed, provisional, or unavailable for each result. An evaluation decision is recorded in T12. Guardrail breaches receive immediate action under existing policy.')
]},
{'heading':'T05 Phase 3 adjustment sprint scorecard','items':[
 ('f','Context','Initiative; original version; previous version; adjustment version; sprint; owner',0),
 ('f','Adjustment hypothesis','Specific bottleneck, change, expected effect, date, cost, and affected risk',1),
 ('f','Window and comparability','Dates; cutoff; work mix; capacity; exposure; source snapshot; follow-up',0),
 ('t',['ID','Measure','Original','Previous','Adjusted','Marginal change'],[
 ['M01','Accepted value time','[Value]','[Value]','[Value]','[Days %]'],
 ['M02','Effort or cost','[Value]','[Value]','[Value]','[Unit %]'],
 ['M03','Net realized value','[Boundary]','[Value]','[Value]','[Currency]'],
 ['[ID]','Targeted diagnostic','[Value]','[Value]','[Value]','[Unit]'],
 ['[ID]','Relevant guardrail','[Value]','[Value]','[Value]','[Unit]']],[.5,1.7,1.05,1.05,1.05,1.65],True),
 ('f','Sample and evidence quality','N or numerators and denominators for each state; sources; missingness; provisional outcomes',1),
 ('f','Cumulative result','Compare adjusted state with original baseline; retain the comparison-group result',1),
 ('f','Sustained benefit and risk','Check benefit erosion, new costs, transferred effort, evaluation results, and fallback',1),
 ('f','Stakeholders and maturity','T08 findings and response counts; relevant T09 changes with evidence',0),
 ('f','Decision and next action','Keep, revise, revert, or observe; owner; due date; acceptance evidence; T12 link',1),
 ('p','Marginal improvement compares adjusted with previous state. Cumulative improvement compares adjusted with the original baseline. Retain failed adjustments and their costs.')
]},
]

core_questions = [
 ['C1','I can obtain the information I need to complete my work.','[1-5 or N/A]'],
 ['C2','Our workflow provides timely and useful feedback.','[1-5 or N/A]'],
 ['C3','I can maintain the required quality within normal working hours.','[1-5 or N/A]'],
 ['C4','Responsibilities and handoffs are clear.','[1-5 or N/A]']
]

phase_questions = {
1:[
 ['Developers','I can understand and safely change the code in my assigned work.','[1-5 or N/A]'],
 ['Engineers and platform','Our environments and build tools support delivery without recurring workarounds.','[1-5 or N/A]'],
 ['QA and operations','Delivered changes include the evidence and support information I need.','[1-5 or N/A]'],
 ['Security','I can identify required controls and verify how changes meet them.','[1-5 or N/A]'],
 ['Business and product','Delivered outcomes meet the agreed need at a useful time.','[1-5 or N/A]'],
 ['Customers if relevant','I can complete the intended task reliably using the current application.','[1-5 or N/A]']
],
2:[
 ['Developers','I can understand and maintain the AI-assisted changes I use or review.','[1-5 or N/A]'],
 ['Engineers and platform','The adopted tooling works reliably within approved permissions.','[1-5 or N/A]'],
 ['QA and operations','I can verify and support changes produced through the adopted workflow.','[1-5 or N/A]'],
 ['Security','I have enough evidence to evaluate AI-related data handling and control risks.','[1-5 or N/A]'],
 ['Business and product','The adopted workflow is helping deliver the intended business outcome.','[1-5 or N/A]'],
 ['Customers if relevant','I can complete the intended task reliably using the released application.','[1-5 or N/A]']
],
3:[
 ['Developers','The adjusted workflow supports changes I can understand and maintain.','[1-5 or N/A]'],
 ['Engineers and platform','The adjustment addresses the identified operating bottleneck.','[1-5 or N/A]'],
 ['QA and operations','The adjusted workflow preserves the evidence and supportability I need.','[1-5 or N/A]'],
 ['Security','The adjustment preserves required controls and addresses identified AI risks.','[1-5 or N/A]'],
 ['Business and product','The adjustment is improving the intended business outcome.','[1-5 or N/A]'],
 ['Customers if relevant','I can complete the intended task reliably after the relevant release.','[1-5 or N/A]']
]}

for phase, tid, label in [(1,'T06','baseline'),(2,'T07','adoption'),(3,'T08','adjustment')]:
    templates.append({'heading':f'{tid} Phase {phase} {label} stakeholder feedback','items':[
      ('p','Copy this form for each respondent. Ask the four core questions consistently across phases for internal roles. Ask the relevant role question and use the open responses to explain the rating. Customers receive only applicable customer questions and follow-up, without internal productivity questions.'),
      ('f','Response context','Initiative; phase; version or release; sprint or date; role; exposure yes no unknown',0),
      ('p','Agreement scale: 1 strongly disagree, 2 disagree, 3 neither agree nor disagree, 4 agree, 5 strongly agree. Use N/A when the respondent lacks relevant experience. Do not code N/A as a midpoint.'),
      ('t',['ID','Stable internal question','Response'],deepcopy(core_questions),[.4,5.25,1.35],True),
      ('t',['Role','Phase specific question','Response'],phase_questions[phase],[1.25,4.4,1.35],True),
      ('f','Example and effect','Describe a specific task or event, its effect, and any effort moved to another role',1),
      ('f','Improvement or concern','What should change next; include any quality, security, customer, or knowledge concern',1),
      ('p','Report urgent risks through the existing incident channel immediately. Participation and identity handling follow local policy. Preserve the core question wording when comparing phases; phase-specific questions are interpreted separately.'),
      ('f','Aggregator record','Eligible and valid responses by role; N/A count; distribution; median; favorable share; themes; owner action',0)
    ]})

templates += [
{'heading':'T09 Maturity assessment record','items':[
 ('f','Assessment context','Initiative; service; phase; dates; assessor; owners; evidence window',0),
 ('p','Use the domain definitions in the framework. Scores: 0 absent, 1 ad hoc, 2 defined, 3 verified in operation, 4 measured and improved. U means unassessed. NA requires an approved applicability rationale. Copy additional rows for each domain.'),
 ('t',['Profile and domain','Score','Evidence and sample','Gap and owner'],[
 ['SDLC planning','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['SDLC development','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['SDLC quality','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['SDLC secure delivery','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['Documentation domain','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['Documentation domain','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['AI governance','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['AI context','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['AI evaluation','[0-4 U NA]','[Links N selection]','[Action owner date]'],
 ['AI treatment','[0-4 U NA]','[Links N selection]','[Action owner date]']],[1.7,1.0,2.3,2.0],True),
 ('t',['Profile','Score sum','Scored domains','Applicable domains','Index and coverage'],[
 ['SDLC','[Sum]','[N]','[N]','[Percent and percent]'],
 ['Documentation','[Sum]','[N]','[N]','[Percent and percent]'],
 ['AI adoption','[Sum]','[N]','[N]','[Percent and percent]']],[1.2,1.0,1.3,1.5,2.0],True),
 ('p','Index is score sum divided by four times scored domains, multiplied by 100. Coverage is scored domains divided by applicable domains, multiplied by 100. An index with no scored domains is undefined. Use equal domain weights.'),
 ('f','Critical gaps and applicability decisions','List separately from indices; include risk consequence, approval, and NA rationales',1),
 ('f','Assessment decision and next review','Record profile changes, action owner, evidence required, and review date',0)
]},
{'heading':'T10 AI use case and risk record','items':[
 ('f','Use case inventory','Initiative; use case ID; tool and vendor; known model version; owner; phase; date',0),
 ('f','Context and affected people','Task; benefit; users; affected customers or groups; prohibited uses',1),
 ('f','Data and privileges','Input data classes; destinations and retention; repository access; command and deployment permissions',1),
 ('f','Human oversight and fallback','Approval boundary; responsible reviewer; override; provider outage or retirement plan',1),
 ('t',['Risk ID and scenario','Consequence and tolerance','Treatment and owner','Residual decision'],[
 ['[ID incorrect output]','[Impact tolerance]','[Control owner date]','Not assessed'],
 ['[ID data exposure]','[Impact tolerance]','[Control owner date]','Not assessed'],
 ['[ID unsafe action]','[Impact tolerance]','[Control owner date]','Not assessed'],
 ['[ID other relevant risk]','[Impact tolerance]','[Control owner date]','Not assessed']],[1.65,1.75,2.15,1.45],True),
 ('t',['Evaluation record','Result and evidence'],[
 ['Test set, scope, and configuration','[ID version held-out cases repeated trials evaluator date]'],
 ['Acceptance criteria and findings','[By risk category; critical failures; limitations; M25-M27]'],
 ['Monitoring and reporting','[Events owners cadence incident channel and change triggers]'],
 ['NIST reference mapping','[Applicable function or subcategory; local interpretation; evidence]']],[2.0,5.0],True),
 ('f','Risk authority decision','Permitted scope; conditions; residual risk owner; exception expiry; next review',1)
]},
{'heading':'T11 Cost and benefit ledger','items':[
 ('p','Copy a ledger row for every cost or benefit. Keep each amount on a consistent currency and economic or cash basis. Benefits require independent verification and overlap reconciliation before recognition.'),
 ('f','Ledger context','Initiative; phase; version; period; currency; cost basis; owner; cutoff',0),
 ('t',['ID','Type and category','Quantity and unit','Rate','Amount','State'],[
 ['[ID]','[Cost subscription]','[Qty unit]','[Rate]','[Value]','[Actual forecast]'],
 ['[ID]','[Cost training]','[Hours]','[Rate]','[Value]','[Actual forecast]'],
 ['[ID]','[Cost integration]','[Hours]','[Rate]','[Value]','[Actual forecast]'],
 ['[ID]','[Cost support review]','[Hours]','[Rate]','[Value]','[Actual forecast]'],
 ['[ID]','[Benefit reduction]','[Qty unit]','[Rate]','[Value]','[Proposed verified]'],
 ['[ID]','[Benefit contribution]','[Qty unit]','[Rate]','[Value]','[Proposed verified]'],
 ['[ID]','[Capacity only]','[Hours]','[Rate]','[Value]','[Potential]']],[.45,1.95,1.2,.8,1.0,1.6],True),
 ('h','Evidence record for each ledger ID'),
 ('f','Evidence and verifier','Ledger ID; source; baseline or counterfactual; verification owner; date',1),
 ('f','Attribution and allocation','Method; eligible scope; share assigned; associated initiatives; uncertainty',1),
 ('f','Overlap reconciliation','Overlap key; linked capacity or outcome; excluded duplicate amounts; reviewer',1),
 ('f','Recognition period and assumptions','Realization date; actual or forecast; rate source; one-time or recurring; cost allocation',1),
 ('p','Multiply quantity by rate only when appropriate to the category. Preserve directly evidenced totals where applicable. Do not recognize speculative avoided incidents as realized cash benefit. Retain negative and rejected rows.')
]},
{'heading':'T11 Value summary and reconciliation','items':[
 ('f','Summary context','Initiative; phase; version; period; currency; economic or cash basis; verifier',0),
 ('t',['Value component','Current period','Cumulative','Evidence'],[
 ['Verified cost reductions','[Amount]','[Amount]','[Ledger IDs]'],
 ['Verified avoided expenditure','[Amount]','[Amount]','[Ledger IDs]'],
 ['Verified incremental contribution','[Amount]','[Amount]','[Ledger IDs]'],
 ['Gross realized benefit','[Sum above]','[Sum above]','[Overlap checked]'],
 ['Recurring incremental cost','[Amount]','[Amount]','[Ledger IDs]'],
 ['One-time and transition cost','[Amount]','[Amount]','[Ledger IDs]'],
 ['Other incremental cost','[Amount]','[Amount]','[Ledger IDs]'],
 ['Total incremental cost','[Sum costs]','[Sum costs]','[Allocation checked]'],
 ['Net realized value','[Benefit less cost]','[Benefit less cost]','[Verified]'],
 ['Realized ROI','[Net / cost x 100]','[Net / cost x 100]','[Percent or undefined]']],[2.9,1.25,1.25,1.6],True),
 ('f','Capacity reported separately','Recovered hours; work classes; sampled coverage; loaded rate; potential equivalent; redeployment',1),
 ('f','Unrecognized or modeled benefits','Pending benefits; scenarios; risk reduction model; limitations',1),
 ('f','Double counting and cost completeness','Confirm overlaps, shared allocation, transition costs, and common period and basis',1),
 ('f','Verification and next checkpoint','Verifier; date; unresolved evidence; owner; review date',0),
 ('p','Only verified realized benefits enter realized ROI. A zero cost denominator makes ROI undefined. An unverified benefit remains pending. M03 can be negative.')
]},
{'heading':'T12 Evaluation decision and improvement action','items':[
 ('f','Decision context','Initiative; phase; version; scope; decision date; accountable authority',0),
 ('f','Evidence reviewed','Scorecards; metric versions; comparison; samples; value ledger; feedback; risk and maturity records',1),
 ('t',['Decision consideration','Finding and consequence'],[
 ['Primary outcomes and practical thresholds','[Baseline post change adjusted contrast and limitations]'],
 ['Value and affordability','[Actual cost verified benefit net value capacity separately]'],
 ['Quality and security guardrails','[Pass fail or unassessed with evidence and action]'],
 ['Stakeholder and customer effects','[Roles response counts themes and material disagreement]'],
 ['Evidence sufficiency','[Missing data small samples delayed outcomes and causal limits]'],
 ['AI risk and maturity gaps','[Residual risks conditions critical gaps and ownership]']],[2.15,4.85]),
 ('f','Decision and rationale','Expand, continue observing, adjust, discontinue, or restrict; name permitted scope',1),
 ('t',['Action','Owner and due date','Acceptance evidence'],[
 ['[Action or adjustment hypothesis]','[Owner date]','[Metric result or control evidence]'],
 ['[Documentation or training update]','[Owner date]','[Verified use or task outcome]'],
 ['[Evaluation or risk treatment]','[Owner date]','[Result and risk decision]']],[2.6,1.65,2.75],True),
 ('f','Conditions and dissent','Exceptions, expiry, affected parties, differing interpretations, and escalation',1),
 ('f','Next review and fallback','Date; triggers; who acts; previous approved state; communication owner',0)
]}
]

# Provide an explicit assessment row for every domain in the framework.
t09_index = next(i for i, record in enumerate(templates) if record.get('heading') == 'T09 Maturity assessment record')
t09 = templates[t09_index]
domain_names = [
 'SDLC planning and requirements', 'SDLC architecture and development',
 'SDLC verification and quality', 'SDLC secure delivery',
 'SDLC release and operations', 'SDLC learning and measurement',
 'Documentation requirements and acceptance', 'Documentation architecture and decisions',
 'Documentation development and interfaces', 'Documentation testing and quality',
 'Documentation security and AI use', 'Documentation operations and recovery'
]
domain_rows = [[name,'[0-4 U NA]','[Links N selection]','[Action owner date]'] for name in domain_names]
ai_rows = [[name,'[0-4 U NA]','[Links N selection]','[Action owner date]'] for name in
 ['AI governance and capability','AI use context and impact','AI evaluation and oversight','AI treatment and continuity']]
t09_first = {'heading':'T09 SDLC and documentation assessment','items':t09['items'][:2] + [
 ('t',['Profile and domain','Score','Evidence and sample','Gap and owner'],domain_rows,[1.9,.9,2.2,2.0],True),
 ('p','Complete the AI profile and profile calculations on the following page. Each level requires the applicable evidence described in the framework. Critical gaps remain visible regardless of the index.')
]}
t09_second = {'heading':'T09 AI assessment and profile summary','items':[
 ('f','Assessment context','Same initiative, scope, dates, and assessor as the preceding assessment page',0),
 ('t',['Profile and domain','Score','Evidence and sample','Gap and owner'],ai_rows,[1.9,.9,2.2,2.0],True)
] + t09['items'][3:]}
templates[t09_index:t09_index+1] = [t09_first,t09_second]
