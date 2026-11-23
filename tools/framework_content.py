framework = []
templates = []

def page(heading, *items, title=False):
    return {('title' if title else 'heading'):heading, 'items':list(items)}

framework.append(page('AI and SDLC Adoption Value Framework',
 ('p','Version 1.0   November 23 2026'),
 ('p','This framework measures whether a change to software development practices improves delivery and produces value worth its total cost. It covers first adoption of AI, changes to existing AI tools, and new engineering workflow patterns. Teams apply it to normal operational delivery and feature work.'),
 ('p','We assess a team delivering an application or service. Agile sprints provide the inspection cadence. Production releases, business acceptance, customer outcomes, and later defects provide evidence that may arrive after the sprint ends.'),
 ('h','Decisions this framework supports'),
 ('b','Establish whether the current workflow can be measured and where improvement would matter.'),
 ('b','Determine whether an adoption should expand, continue under observation, change, or stop.'),
 ('b','Confirm that benefits persist and that quality, security, and stakeholder experience remain acceptable.'),
 ('h','How to use the documents'),
 ('p','Use this document for definitions, calculations, scoring, governance, and interpretation. Copy the forms in the companion Sprint Scorecards and Stakeholder Templates document for each initiative and sprint. Every measure uses an identifier that remains consistent across both documents.'),
 ('p','Start with three primary measures: time to accepted production value, delivery effort or cost, and realized net adoption value. Add the diagnostics needed to explain the proposed change and its risks. Do not make every metric a target.'),
 ('h','Design status'),
 ('p','The measurement rules, maturity rubric, suggested observation windows, and decision thresholds in this document are proposed organizational conventions. They require local ownership and tailoring. Worked examples are illustrative and do not describe an actual organization. Standards alignment does not establish certification or regulatory compliance.'),
 title=True))

framework.append(page('Framework structure and operating rules',
 ('t',['Part','What it establishes'],[
 ['Operating model','Three phases, roles, sprint cadence, and adoption contract'],
 ['Measurement','Evidence, comparable work, metric definitions, and attribution'],
 ['Value','Capacity, financial benefits, total costs, and sensitivity'],
 ['Maturity','Separate SDLC, documentation, and AI adoption profiles'],
 ['NIST integration','AI risk responsibilities and evidence across all phases'],
 ['Templates','Reusable records provided in the companion document']],[1.45,5.55]),
 ('h','Rules that apply throughout'),
 ('b','Measure team systems and application outcomes. Do not use lines of code, prompt counts, commits, or story points as individual productivity ratings.'),
 ('b','Keep speed, value, and risk visible separately. A financial benefit cannot offset an unacceptable security condition.'),
 ('b','Define eligible work, comparison groups, cost boundaries, and thresholds before evaluating results. Record all changes to those definitions.'),
 ('b','Preserve the original baseline. When a new adjustment begins, retain both the original baseline and the preceding operating state.'),
 ('b','Record actual use and unknown exposure. A license, an installed extension, or a generated suggestion does not establish useful adoption.'),
 ('b','Make missing data visible. Do not replace unknown results with zero or label unmeasured risk as acceptable.'),
 ('p','The design draws on lifecycle standards [S1, S2], DORA delivery research [S3], SPACE productivity research [S4], Scrum [S5], and NIST guidance [S6-S10]. The source register identifies their roles and versions. Detailed controls and legal obligations must be mapped to the organization separately.')
))

framework.append(page('Phase 1 Establish current delivery',
 ('p','Phase 1 establishes how work is delivered today and what the proposed change should improve. For an organization already using AI, the baseline includes that usage. The intervention is the incremental change from the recorded current state.'),
 ('h','Required activities'),
 ('n','Choose the application, accountable team, business outcome, and workflow stage. Map commitment, development, review, testing, security, production availability, and acceptance.'),
 ('n','Record existing AI products, versions where available, approved uses, data handling, permissions, and human review. Record other automation and planned process changes.'),
 ('n','Collect representative historical data and prospective feedback. A starting window is four to six complete sprints, extended for low volumes, seasonality, or atypical operations.'),
 ('n','Assess the SDLC, documentation, and AI adoption maturity profiles. Capture evidence and gaps rather than relying only on workshop opinions.'),
 ('n','Define the adoption hypothesis, three primary measures, selected diagnostics, quality and security limits, costs, comparison method, and observation windows.'),
 ('h','Required evidence'),
 ('p','Retain the adoption contract T01, metric definitions T02, baseline sprint records T03, stakeholder feedback T06, maturity assessment T09, and applicable AI risk records T10. Separate incomplete records and unavailable fields from measured results.'),
 ('h','Exit decision'),
 ('p','The delivery owner confirms that the workflow and scope are defined. Metric owners confirm usable evidence or explicit limitations. The product owner confirms the desired outcome. Security and the AI risk owner confirm that the proposed use fits the agreed risk tolerance. Unresolved critical controls prevent expansion into the affected use.'),
 ('p','A reconstructed baseline may be used when history is incomplete, with its limitations recorded. If there is no defensible baseline or comparison, report the current state and begin prospective collection before claiming improvement.')
))

framework.append(page('Phase 2 Adopt and evaluate',
 ('p','Phase 2 measures the change in real delivery. Start with a staged rollout where feasible, using comparable teams or workstreams and an explicit allocation rule. A staged rollout can operate in production while retaining normal release and security controls.'),
 ('h','Required activities'),
 ('n','Record activation dates, eligible work, exposure, training, vendor configuration, and changes in permissions. Distinguish assigned access, actual use, and evaluated output.'),
 ('n','Identify the learning period in advance. Include its costs in the investment view and report its delivery results separately from steady operation. Do not remove poor results after observing them.'),
 ('n','Collect sprint measures and role-specific feedback. Include review, QA, security, operations, and documentation effort so a local speedup cannot conceal transferred work.'),
 ('n','Compare with baseline and the comparison group where available. Track work mix, available capacity, incidents, release constraints, and simultaneous changes.'),
 ('n','Evaluate at the agreed checkpoint, initially after four to six post-change sprints. Extend observation for insufficient volume, unstable operation, or delayed outcomes.'),
 ('h','Required evidence'),
 ('p','Use T04 for each adoption sprint, T07 for stakeholder feedback, T11 for costs and benefits, and T12 for the evaluation decision. Update the AI risk register and record any tool or model change that could affect the result.'),
 ('h','Decision options'),
 ('t',['Decision','Evidence and response'],[
 ['Expand','Benefits meet the agreed practical threshold and applicable controls and guardrails pass. Name the next scope.'],
 ['Continue observing','Evidence is incomplete or too variable. Name the missing evidence, next checkpoint, and permitted scope.'],
 ['Adjust','A specific workflow or control problem has a testable correction. Create a versioned adjustment.'],
 ['Discontinue or restrict','Costs exceed the justified benefit, outcomes deteriorate, or unacceptable risk persists. Execute the fallback plan.']],[1.3,5.7])
))

framework.append(page('Phase 3 Enhance and adjust',
 ('p','Phase 3 tests whether improvements can be sustained and extended. Treat each meaningful change as a versioned intervention, including model upgrades, prompt or context changes, permission changes, and new workflow patterns.'),
 ('h','Required activities'),
 ('n','Select a bottleneck supported by evidence. For example, faster coding may expose slow review or weak test reliability.'),
 ('n','Record the adjustment, expected effect, affected risks, cost, and rollback condition. Change one major element at a time when practical.'),
 ('n','Compare the adjusted state with both the original baseline and the preceding adopted state. This distinguishes cumulative value from the marginal value of the adjustment.'),
 ('n','Repeat relevant AI evaluations and production monitoring when behavior, scope, data access, or versions change. Verify that previous benefits and controls still hold.'),
 ('n','Update documentation, learning materials, ownership, and the improvement backlog. Reassess maturity at a meaningful release or quarterly checkpoint, rather than forcing a new score every sprint.'),
 ('h','Required evidence'),
 ('p','Use adjustment scorecard T05 and feedback T08. Carry forward T09-T12 for maturity, AI risk, value, and decisions. Preserve prior decisions and source snapshots so cumulative claims remain reproducible.'),
 ('h','Sustainability review'),
 ('p','Look for benefit erosion, review fatigue, supplier dependency, rising inference cost, knowledge loss, and deferred maintenance. Check whether new hires and less experienced engineers can understand and support the resulting code.'),
 ('p','An adjustment is complete when its agreed outcomes have been observed for the stated window, controls have passed, and ongoing ownership is assigned. Financial and customer outcomes that have not matured remain pending. Completion of implementation alone does not establish benefit realization.')
))

framework.append(page('Ownership and sprint cadence',
 ('t',['Accountability','Responsible role','Decision or evidence'],[
 ['Initiative','Engineering or delivery lead','Scope, intervention version, execution, and fallback'],
 ['Business outcome','Product owner or business sponsor','Acceptance, outcome target, and business benefit'],
 ['Measurement','Named metric or analytics owner','Definitions, joins, completeness, and calculations'],
 ['Security and AI risk','Security lead and designated AI risk owner','Risk tolerance, testing, exceptions, and escalation'],
 ['Value verification','Finance or delegated benefit owner','Cost boundaries, attribution, and realized benefits'],
 ['Operational quality','QA and operations owners','Release quality, reliability, and downstream burden'],
 ['Documentation','Service or knowledge owner','Required artifacts, accuracy, and maintenance']],[1.18,2.0,3.82]),
 ('h','Use existing ceremonies'),
 ('p','At Sprint Planning, identify the intervention version and expected work mix. Confirm the Sprint Goal and relevant Definition of Done. During the sprint, gather delivery events and respond immediately to risk breaches. Avoid daily individual productivity reporting.'),
 ('p','At the Sprint Review, inspect delivered and accepted outcomes with business stakeholders. At the Retrospective, examine bottlenecks, effort transfer, and developer feedback. Close the scorecard after the data cutoff and name any pending observations.'),
 ('p','At each evaluation checkpoint, the accountable owners decide whether to expand, observe, adjust, or stop. Keep a decision record with the evidence, dissent, conditions, and next review date. These activities extend local measurement practice and are not additional Scrum requirements [S5].'),
 ('h','Tailor thresholds before use'),
 ('p','Set improvement thresholds from baseline variation, business importance, available volume, and cost. Set security and operational limits from existing policy and service objectives. Record both practical significance and evidence sufficiency. A target such as a 15 percent reduction in lead time is illustrative until locally justified.')
))

framework.append(page('Evidence model and data handling',
 ('p','Link work to delivery and outcomes using stable identifiers. Store raw evidence in its governed source and retain reproducible references or snapshots. Use a separate measurement layer for aggregation.'),
 ('t',['Record','Minimum fields'],[
 ['Adoption','Initiative ID, version, hypothesis, phase, scope, dates, owner, tool and known model version'],
 ['Work item','Work ID, service, work class and risk class, commitment time, sprint, acceptance criteria'],
 ['Delivery','PR and commit IDs, review and test events, deployment ID, environment, availability time'],
 ['Outcome','Acceptance time, defect or incident ID, severity, affected release, business outcome ID'],
 ['Exposure','Work ID or team window, assigned rollout group, actual use yes no or unknown, source'],
 ['Value','Ledger ID, period, category, quantity, rate, allocation, evidence, verifier, overlap key'],
 ['Feedback','Phase, role, sprint, question version, response, eligible count, response count'],
 ['Risk','AI use case, data classes, privileges, evaluations, owner, treatment, residual risk']],[1.05,5.95]),
 ('h','Joining and reconciliation'),
 ('p','Allow many work items per PR and many PRs per deployment without multiplying deployment counts or costs. Count deployments once per defined service and environment. Allocate shared effort and costs once using a recorded rule. Track unmatched records and delayed evidence.'),
 ('h','Privacy and collection'),
 ('p','Collect the minimum telemetry needed. Prefer event metadata over raw prompts, source code, or customer data. Apply existing access, retention, and classification rules. Keep respondent identities out of team scorecards. Use a locally approved minimum reporting group, for example five respondents, and combine or suppress smaller groups.'),
 ('p','This framework does not require keystroke capture, screen recording, or continuous individual time tracking. Sampled effort diaries or existing task records may support effort estimates if collection burden and uncertainty are reported.')
))

framework.append(page('Comparison and calculation rules',
 ('h','Define the population'),
 ('p','Choose work classes and risk or complexity bands before analysis. Keep feature work, maintenance, incidents, and security remediation identifiable. Compare like work within the same application context. Report available team capacity and changes in scope. Story points remain a local planning tool and must not be converted into cross-team productivity or financial value.'),
 ('h','Use consistent time boundaries'),
 ('p','Store timestamps in UTC and display a named reporting timezone. A reporting window includes events at its start and excludes events at its end. Use elapsed calendar time for delivery measures unless a business-hours variant is explicitly labeled. Report complete sprints and state the extraction cutoff.'),
 ('p','For durations, report the median and 85th percentile of underlying item durations. Use one documented quantile method, such as linear interpolation at position one plus the percentile times the count minus one. Never average sprint percentiles. For rates, sum numerators and denominators across the window before dividing.'),
 ('h','Retain unfinished and delayed outcomes'),
 ('p','Completion-based metrics can hide stalled work. Report age and count of unfinished work alongside completion times. Define a follow-up window for defects and acceptance, initially 30 days where suitable. Mark recent cohorts provisional until their full follow-up ends. Use the same follow-up for baseline and post-change cohorts.'),
 ('h','Interpret change'),
 ('p','For a lower-is-better metric, percent improvement is baseline minus post-change, divided by baseline, multiplied by 100. For higher-is-better measures, reverse the subtraction. When baseline is zero, report absolute change and mark relative change undefined. For percentages, show percentage-point change as well as endpoints.'),
 ('p','Prefer staged allocation or a credible comparison group. An adjusted change is the adopting group change minus the comparison group change in the same units. Check earlier trends and concurrent differences. This method supports attribution only when its assumptions are credible; it does not remove all confounding.'),
 ('p','Record counts, variation, exclusions, work mix, and uncertainty. Use suitable intervals or analyst review when volume permits. Avoid claims of statistical certainty from a few sprints or rare incidents. Without a defensible causal design, describe the finding as an association.')
))
