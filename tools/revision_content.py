"""Apply the approved EIF name and add explanatory figures to version 1.0."""
from copy import deepcopy


def revise(value):
    if isinstance(value,str):
        value=value.replace('AI and SDLC Adoption Value Framework','Engineering Impact Framework')
        value=value.replace('Sprint Scorecards and Stakeholder Templates','Engineering Impact Framework Templates')
        value=value.replace('Version 1.0','Version 1.1')
        return value
    if isinstance(value,list): return [revise(v) for v in value]
    if isinstance(value,tuple): return tuple(revise(v) for v in value)
    if isinstance(value,dict): return {k:revise(v) for k,v in value.items()}
    return value


def updated_content(framework,templates):
    main=revise(deepcopy(framework))
    forms=revise(deepcopy(templates))
    main[0]['items']=[(item[0],item[1].replace('This framework measures','The Engineering Impact Framework (EIF) measures')) if item[0]=='p' else item for item in main[0]['items']]
    main[0]['items'].insert(3,('i','eif_lifecycle','Figure 1  Baseline establishes the reference point while Adoption and Improvement form a repeated evaluation loop.',
        'Three phases from Baseline to Adoption to Improvement. Improvement returns to evaluation, while the original baseline is retained for cumulative comparisons.',7.0))
    for page in main:
        title=page.get('heading','')
        if title=='Phase 1 Establish current delivery': page['heading']='Phase 1 Baseline current delivery'
        elif title=='Phase 2 Adopt and evaluate': page['heading']='Phase 2 Adoption and evaluation'
        elif title=='Phase 3 Enhance and adjust': page['heading']='Phase 3 Improvement and adjustment'
        elif title=='Evidence model and data handling':
            page['items'].insert(1,('i','delivery_measurement','Figure 2  Illustrative delivery path and measurement points for M01 and M04. Actual workflows may iterate and acceptance may precede production.',
                'Delivery flows from commitment through development, review, verification, production, and acceptance. M01 ends at the later of production and acceptance; M04 starts at code commit and ends at successful production deployment.',7.0))
        elif title=='Value calculations and recognition rules':
            page['items'].insert(1,('i','value_recognition','Figure 3  Only verified non overlapping benefits enter realized value. Capacity and risk limits remain separate.',
                'Verified benefits less incremental costs produce realized net value. Recovered capacity is tracked separately. Quality and risk limits must pass independently of the financial result.',7.0))
        elif title=='Source register continued':
            for item in page['items']:
                if item[0]=='t' and item[1]==['Version','Date','Change']:
                    item[2].append(['1.1','November 23 2026','Renamed to Engineering Impact Framework and added explanatory diagrams for the lifecycle, delivery measurement, value recognition, AI oversight, and template use.'])
    pos=next(i for i,p in enumerate(main) if p.get('heading')=='AI risk evaluation and adoption decisions')+1
    main.insert(pos,{'heading':'AI review and release workflow','items':[
        ('p','This example shows how the AI risk responsibilities described in the previous sections fit an AI assisted development change. It illustrates a local implementation of the NIST AI RMF functions [S6, S7]. The functions remain active throughout the lifecycle and are not exclusive stages.'),
        ('i','ai_review_release','Figure 4  An AI assisted change reaches release through review and required controls. Failed or missing evidence leads to correction or fallback.',
            'Governance applies across task definition, AI proposal, review, release, and monitoring. A review decision sends sufficient evidence to release and monitoring. Failed or unknown evidence goes to correction or fallback and then back to review.',7.0),
        ('h','Apply the approval boundary before execution'),
        ('p','AI output does not grant permission to merge, execute a privileged command, or deploy. For agentic tooling, apply the relevant approval and access boundary before each consequential action. Retain the actor, action, result, and evidence in the approved audit system.'),
        ('h','Close the feedback loop'),
        ('p','Monitoring findings become incident records, risk treatments, or an improvement hypothesis. A corrected change returns to review and any affected evaluations. A fallback returns the workflow to an approved operating state. Do not wait for the sprint review to respond to a serious breach.')
    ]})
    forms.insert(1,{'heading':'Choosing and closing sprint records','items':[
        ('p','Choose the scorecard and stakeholder feedback form that match the initiative phase. Shared records carry forward across phases so that risks, maturity evidence, and value claims remain traceable.'),
        ('i','template_handoffs','Figure 1  Phase specific forms feed shared evidence and the next accountable decision.',
            'Begin with T01 and T02. Phase 1 uses T03 and T06, Phase 2 uses T04 and T07, and Phase 3 uses T05 and T08. Each phase updates T09, T10, and T11 before T12 records the decision and next action.',7.0),
        ('h','Complete the record in the right order'),
        ('p','Confirm the initiative version and metric definitions before the sprint. At sprint close, update the scorecard and feedback results, then reconcile the shared evidence. T12 records the permitted next step, accountable owner, conditions, and next checkpoint.'),
        ('h','Keep pending evidence visible'),
        ('p','Customer outcomes, later defects, and verified financial benefits may arrive after sprint close. Mark them pending or provisional and link the later update. Carry open actions into the next sprint instead of treating a completed form as proof that the outcome has been achieved.')
    ]})
    return main,forms
