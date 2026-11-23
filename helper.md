# Engineering Impact Framework implementation helper

**PolarSpark LLC** | **Paul Harding, MBA ITM** | [polarspark.com](https://polarspark.com/)

Use this practical companion with [agent.md](agent.md), the [framework](docs/framework.md), and the [workbook](docs/templates.md). The agent helps implement EIF in the consumer organization's environment. This repository provides reference material and is not a destination for implementation files, organization data, or generated reports.

## Start an implementation

Give an agent the following instruction, replacing the bracketed fields. Read access to the reference repository is sufficient; the agent does not need contributor access to it.

```text
Use PolarSpark LLC's Engineering Impact Framework from:
https://github.com/polarspark/engineering-impact-framework

Read agent.md, helper.md, docs/framework.md, and docs/templates.md there.
Resolve and record the framework revision before applying its definitions.

Guide us through discovery, Baseline, Adoption, and Improvement. Help us
gather and validate evidence, implement authorized changes in our environment,
generate sprint measures and value calculations, and prepare owner decisions.
Ask the questions needed at each stage and maintain resumable progress.

Application or service: [name and location]
Proposed change or problem: [AI/tool/workflow change and intended outcome]
Consumer workspace: [separate local or approved private workspace]
Current authorized scope: [discovery, data collection, instrumentation,
implementation, or other specified actions]
Known sources and owners: [systems, available exports, responsible roles]

Treat the framework repository and any local checkout of it as read only.
Create implementation files only in our consumer workspace. Keep organization
data in our approved systems. Do not commit, push, publish, upload, or submit
implementation outputs to the framework repository. Do not deploy changes or
contact stakeholders beyond the authority we have given you.
```

These filenames are explicit entry points, not a guarantee that an agent will load them automatically. Put the instruction in the consumer's normal agent configuration or task prompt while preserving that environment's existing instructions. Do not replace local policy files with this helper.

## Intake questions

Check authorized repositories and sources first. Ask only what remains unknown, in small batches appropriate to the current stage.

| Stage | Establish | Why it matters |
| --- | --- | --- |
| Discovery | Which application, team, owner, business outcome, proposed change, and separate workspace? What actions are authorized? | Sets scope, destination, and responsibility. |
| Baseline | What tools and AI use exist now? How are sprints, work commitment, releases, acceptance, effort, and incidents recorded? | Makes the current state measurable. |
| Comparison design | Which work is eligible? Which rollout assignment or comparison is feasible? What changed concurrently? | Supports a defensible interpretation. |
| Data handling | Which systems and fields can be read? Who owns costs and feedback? Where may evidence be retained? | Supports collection without moving confidential records into the public framework. |
| Adoption | What exactly changes, when, for whom, and with which permissions, learning period, checks, and fallback? | Defines the intervention and its full cost. |
| Improvement | Which bottleneck is evidenced? What adjustment is proposed, and what result would justify keeping it? | Separates an improvement hypothesis from an arbitrary tool change. |

Use an assumption log for provisional planning choices. Do not use an unconfirmed assumption as a measured fact, financial verification, or release approval.

## Consumer workspace

Select an organization-controlled workspace outside any framework checkout. A possible structure is:

```text
<consumer_workspace>/eif/<initiative_id>/
  state.json
  implementation-plan.md
  environment-and-sources.md
  assumptions-and-gaps.md
  records/
    T01-adoption-contract.md
    T02-metric-definitions.md
    T03-baseline/<sprint_id>.md
    T04-adoption/<sprint_id>.md
    T05-improvement/<sprint_id>.md
    T06-baseline-feedback.md
    T07-adoption-feedback.md
    T08-improvement-feedback.md
    T09-maturity.md
    T10-ai-risk.md
    T11-cost-benefit-ledger.csv
    T12-decisions.md
  measurement/
    source-map.csv
    data-dictionary.md
    evidence-manifest.csv
    validation-report.md
    queries-or-adapters/
    calculations/
  reports/
    baseline-readout.md
    sprint-scorecards/
    adoption-value-readout.md
    improvement-readout.md
    handoff.md
```

Create only the records needed for the current phase and authorized scope. Use the workbook's actual fields and question wording when creating T01 through T12. Markdown and CSV are examples; use the organization's accepted formats. Implementation code and CI configuration belong in its application repository when authorized, with references from the initiative record.

`state.json` should record: initiative ID, framework version and full commit SHA, consumer workspace, current phase and stage, original baseline ID, current and previous intervention versions, application, owners, authorized scope, source and metric versions, reporting timezone, observation windows, evidence cutoff, completed artifacts, unresolved dependencies, latest owner decision, and next action. Store no credentials or identifiable survey responses in it. Inspect this state before resuming; never restart or overwrite the baseline just because an agent session changed.

## Map sources before building integrations

| Evidence | Typical source | Minimum connection to the study |
| --- | --- | --- |
| Work and commitment | Jira, Azure Boards, GitHub Issues, or approved export | Work ID, service, sprint, class, commitment, acceptance criteria, and scope changes. |
| Code and review | GitHub, GitLab, Azure Repos, or approved export | PR/commit IDs, linked work, readiness, substantive review, and approval evidence. |
| Build and release | CI and deployment system | Run ID, queued and result times, artifact identity, deployment ID, service, environment, and availability. |
| Acceptance and outcomes | Product owner record, product analytics, support, or business system | Work or outcome ID, acceptance time, customer exposure, and a defined outcome denominator. |
| Defects and incidents | QA and incident systems | Finding ID, severity, source release, detection, recovery or remediation, and follow-up cutoff. |
| Security and control execution | Scanners, policy checks, exception and release records | Applicable controls, execution results, failures, exceptions, and accountable owners. |
| Effort and cost | Approved task samples, time records, invoices, finance rates | Activity, period, work linkage, sampling coverage, quantity, unit, allocation, and cost basis. |
| AI use and evaluation | Approved usage metadata, work tags, reviews, evaluation records | Assigned rollout, actual/unknown exposure, tool configuration, known model version, evaluation and oversight evidence. |
| Experience and maturity | Authorized feedback, documentation inventory, operating samples | Phase, role, question version, response coverage, evidence, assessor, and owner. |

These are possible mappings, not requirements to buy products or enable every connector. Prefer an existing approved source or export over creating a new collection service. Request access through the organization's normal process when required; do not bypass a missing permission.

## Gather and validate evidence

1. For each selected metric, freeze its T02 definition and identify the authoritative fields. Record the source owner, query or export method, schema, grain, expected coverage, and extraction time.
2. Use approved read access to gather metadata. Keep raw payloads, source code, prompts, customer data, and identifiable feedback in their governed systems unless their collection is necessary and authorized. Put safe references and summaries in the initiative record.
3. Preserve work-to-PR and PR-to-deployment relationships as separate mappings. Many work items in one deployment must not multiply deployment counts, effort, or shared cost. Include service and environment in identifiers where needed.
4. Normalize timestamps to UTC, retain the reporting timezone, and define each half-open reporting window as start inclusive and end exclusive. Keep production availability and business acceptance as separate events.
5. Validate missingness, duplicate and unmatched records, impossible time order, source freshness, work mix, actual exposure, and observation maturity. For M01, acceptance before deployment can be legitimate: use the later endpoint rather than rejecting it automatically.
6. Save an evidence manifest with snapshot ID, source, query or export revision, extraction time, covered period, schema version, record count, checksum where practical, classification, access location, retention, and owner. Use immutable references or versioned snapshots where available.
7. Trace a sample from a report row back to its source and independently recompute it. Mark limitations and unresolved records before drawing conclusions.

If historical evidence is incomplete, document any reconstructed baseline and its limits, then establish prospective collection. Do not fill gaps with the Java example or estimated survey answers. Record when an observation window has not yet elapsed; leave affected outcomes provisional.

## Minimum data contracts

Choose an implementation suited to the target stack. The following logical records are a starting point, not a replacement for each metric's T02 definition. Optional fields depend on selected measures; missing required evidence remains visible.

| Record | Suggested fields |
| --- | --- |
| Work item | `initiative_id`, `intervention_version`, `work_id`, `service_id`, `sprint_id`, `work_class`, `risk_band`, `committed_at`, `availability_at`, `accepted_at`, `state`, `scope_change`, `source_ref`. |
| Delivery event and mappings | `service_id`, `environment`, `pr_id`, `commit_sha`, `run_id`, `artifact_id`, `deployment_id`, `event_type`, `event_at`, linked work/PR/commit/deployment keys, `source_ref`. |
| Effort observation | `observation_id`, `period`, `work_id` where available, `activity`, `person_hours`, `sampling_method`, `sample_coverage`, `allocation_rule`, `rate_basis`, `source_ref`. Use activity allocations that reconcile without duplicating the same hours. |
| AI exposure | `work_id` or declared team window, `rollout_assignment`, `eligible`, `actual_use` as yes/no/unknown, `tool`, `configuration_version`, `known_model_version`, `observed_at`, `source_ref`. |
| Quality or risk finding | `finding_id`, `deployment_id` or affected work/use case, `severity`, `detected_at`, `resolved_at`, `status`, `exception_ref`, `observation_cutoff`, `owner`, `source_ref`. |
| Feedback summary | `phase`, `sprint_id`, `role_group`, `question_id`, `question_version`, `eligible_count`, `valid_count`, `not_applicable_count`, `response_distribution`, `deidentified_themes`, `owner`. Suppress small groups under local policy. |
| Value ledger | `ledger_id`, `period`, `currency`, `cost_or_benefit_category`, `quantity`, `unit`, `rate`, `amount`, `cash_or_economic_basis`, `recognition_state`, `allocation_rule`, `overlap_key`, `realized_at`, `evidence_ref`, `verification_owner`, `verified_at`. |

Keep raw source grain separate from calculated reporting grain. A result record should carry `metric_id`, `definition_version`, `initiative_id`, `intervention_version`, `phase`, `period_start`, `period_end`, `cutoff`, `population`, `unit`, `value`, `sample_count` or `numerator` and `denominator`, `coverage`, `status`, `snapshot_refs`, `calculation_revision`, `limitations`, and `owner`. Add baseline and previous-state references for comparisons. A single generic `value` field does not replace a duration distribution, severity breakdown, or maturity profile.

## Build the implementation

Create a concrete implementation plan in the consumer environment. Each backlog item needs the target file or system, change, responsible owner, expected result, evidence hook, validation, permitted rollout, and fallback. Reuse existing application patterns, CI, telemetry, and secret management.

Implement only what the user has authorized: adapters or queries to collect evidence, calculations for selected measures, scorecard generation, and the proposed workflow or tooling change where in scope. Do not turn a request for measurement setup into an unapproved application rollout. Validate calculations before relying on them and validate both application behavior and instrumentation when making a delivery change.

For the Java example, map work IDs to PRs, CI runs, artifact digests, production deployment, and acceptance. Keep the normal Maven build and configured tests, security checks, human review, documentation, and release controls. Runtime traces can explain application behavior; they do not directly establish engineering effort saved. The [Java workflow](docs/java-workflow.md) supplies the worked process, while the actual environment determines tool versions and integration details.

## Generate the measures

Use the full metric definitions in the pinned framework. Select diagnostics that can change a decision rather than making all 28 metrics targets.

| Measure or result | Calculation or treatment |
| --- | --- |
| M01 accepted production value time | For eligible completed work, `max(availability_at, accepted_at) - committed_at`, in calendar days. Report median and p85 from underlying durations, counts, missing endpoints, and M11 unfinished work alongside it. |
| M02 delivery effort per outcome | Attributed delivery person-hours divided by comparable accepted production outcomes on the declared basis. Include review, testing, security, documentation, operations, correction, and abandoned work as specified in the period definition. Keep one-time adoption effort separately identifiable. |
| M03 realized net value | Verified non-overlapping incremental financial benefits minus complete incremental adoption cost over a common period and currency/cost basis. Do not substitute capacity equivalent for financial benefit. |
| Realized ROI | `100 * net_realized_value / incremental_cost`. Zero cost makes ROI undefined; retain the net value and explanation. |
| Recovered capacity | `(comparable_baseline_hours_per_task - current_hours_per_task) * eligible_current_volume`, adjusted for work mix where necessary. Preserve negative results. An hourly-rate conversion is potential capacity value until a financial benefit is separately verified. |
| Lower-is-better relative improvement | `100 * (baseline - current) / baseline`. When baseline is zero, report absolute change and undefined relative change. Reverse the subtraction for higher-is-better measures. |
| Rates and durations over several sprints | Sum rate numerators and denominators before division. Recompute median and p85 from pooled underlying durations using the recorded quantile method. Never average sprint percentiles. |
| Comparison-adjusted change | `(adopter_after - adopter_before) - (comparison_after - comparison_before)` in the same units. State allocation, earlier trend, work mix, and concurrent-change limits. Do not call it causal without supporting design and assumptions. |
| Improvement comparisons | Marginal compares adjusted with previous adopted state; cumulative compares adjusted with the original baseline. Retain both reference states and costs. |
| Maturity index and coverage | Within each separate profile, `100 * score_sum / (4 * scored_domains)` and `100 * scored_domains / applicable_domains`. Use U for unassessed, approved NA exclusions, and undefined results for zero denominators. List critical gaps separately. |

Every selected quality, security, experience, documentation, business, customer, and AI risk measure must follow its own definition and evidence requirements. For example, M07 counts distinct failed deployments, M17 preserves question-level response distributions and coverage, and M18 keeps assignment, actual use, and unknown exposure distinct. Use the same cohort follow-up rule before comparing defect or failure rates.

### Calculation verification example

The following is synthetic test input for checking an implementation, not an organizational result:

- Baseline: 800 delivery hours for 40 comparable outcomes gives 20 hours per outcome.
- Adoption: 640 hours for 40 outcomes gives 16 hours per outcome, a 20 percent observed reduction, and 160 recovered hours.
- At USD 100 per hour, capacity equivalent is USD 16,000, reported separately from realized benefit.
- Distinct verified financial benefits of USD 12,000 and USD 18,000 total USD 30,000. Incremental costs of USD 6,000, USD 8,000, USD 8,000, and USD 2,000 total USD 24,000. Net value is USD 6,000 and ROI is 25 percent.
- Adopter M01 moves from 10 to 8 days; comparison moves from 10 to 9.5 days. The adjusted contrast is minus 1.5 days, equal to a 15 percent reduction against the adopter's baseline, subject to the comparison's assumptions.
- Six applicable maturity domains scored 3, 2, 2, 1, 3, and U produce an index of 55.0 at 83.3 percent coverage. The missing domain remains U.

Verify missing endpoints, zero denominators, duplicate deployment joins, late defects, unknown AI exposure, negative savings, and overlapping benefits as well as the ordinary example. Keep synthetic fixtures outside organizational result inputs and label them in the validation report.

## Close each sprint

At Planning, confirm the intervention version, Sprint Goal, expected work mix, and selected measures. During delivery, collect events and handle control breaches through existing processes. At Review, verify production and business acceptance. At Retrospective, connect role-specific feedback to observed bottlenecks and transferred effort. Close the record at its declared cutoff and retain later revisions.

Each scorecard or readout should contain:

1. Initiative, application, team, phase, sprint/window, intervention and framework revisions, cutoff, and accountable owners.
2. Eligible work, capacity, rollout assignment, actual/unknown exposure, comparison group, and concurrent changes.
3. M01, M02, and M03 with baseline/current or original/previous/adjusted values, units, counts, coverage, sources, calculation versions, and status. In Baseline, M03 for the proposed change remains not evaluated.
4. Selected quality, security, experience, business/customer, documentation, and AI risk results, including breaches and missing evidence.
5. Cost and benefit reconciliation, separately stated recovered capacity and modeled benefits, uncertainty, and attribution limits.
6. Stakeholder findings with response coverage and protected identities; maturity profiles and critical gaps where assessed.
7. Agent recommendation, actual owner decision if made, next action, responsible person, due date, and evidence required at the next checkpoint.

Use the matching records: T03/T06 for Baseline, T04/T07 for Adoption, T05/T08 for Improvement. Carry T09 through T12 across phases. A sprint boundary does not require a production deployment, end a defect observation window, or prove that financial benefits have matured.

## NIST responsibilities and decisions

Carry these responsibilities through every phase in T10:

- **Govern:** owners, permitted uses, training, supplier responsibilities, permissions, escalation, and decisions.
- **Map:** task context, affected people, data, privileges, dependencies, potential harms, and intended business benefit.
- **Measure:** relevant evaluation cases, human review evidence, operational monitoring, limitations, and failure records.
- **Manage:** treatments, containment, fallback, residual risk decisions, retesting, and ongoing review.

Apply SSDF and existing secure delivery controls to the application. Use the generative AI profile when relevant to the use case. Framework maturity levels and ROI rules are local conventions and confer no NIST or ISO certification. Record the chosen reference versions and review relevant standards changes before changing an established study.

The agent prepares evidence and a recommendation. Named organizational owners decide the next permitted scope and record it in T12. A positive ROI does not override a critical control failure. An incomplete or immature result can support continued observation with an explicit evidence request and review date.

## Resume and hand off

Read the implementation state, latest source snapshots, last scorecard, and last owner decision before continuing. Preserve the original baseline and prior intervention versions. Update only the affected records, document restatements, and rerun relevant validation after extraction or calculation changes.

Leave the consumer with runnable extraction and calculation steps, metric definitions, current scorecards, costs and verified benefits, maturity and risk findings, pending observations, owners, fallback instructions, and the next review. Keep all of these in the consumer's approved environment. Do not push them to this repository, request a framework pull request, or create a public example from private evidence.
