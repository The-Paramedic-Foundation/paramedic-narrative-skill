# Universal Paramedicine Documentation Standards Primer

Reference file for the `paramedic-narrative` skill. Read when no agency-specific documentation
policy has been provided, or to supplement agency policy on specific topics.

---

## Purpose of the PCR Narrative

The patient care report serves multiple functions simultaneously:

- **Clinical handoff**: The receiving provider reads the narrative to understand what
  happened before they took over care.
- **Legal record**: The PCR is discoverable, subpoenable, and may be the basis for
  testimony. Every word is permanent.
- **Quality improvement**: Chief Paramedics, QI officers, and researchers use PCRs to
  evaluate protocol compliance, clinical performance, and system-level trends.
- **Billing and reimbursement**: CMS and commercial payers require documentation of
  medical necessity. The narrative must establish why transport was necessary.
- **Continuity of care**: If the patient returns to care or is transferred between
  facilities, prior PCRs inform subsequent providers.

The narrative must serve all of these functions. A narrative that is thorough enough for
clinical handoff but vague about medical necessity will fail the billing function. A
narrative that documents what was done without documenting why will fail the QI function.

---

## Assessment Section -- Protocol and CPG References

The Assessment section must reference the protocol(s) or Clinical Practice
Guideline(s) (CPGs) that governed clinical decisions on the call. Local protocol
numbers are appropriate and sufficient for routine documentation. When a national
CPG was the operative basis for a clinical decision -- particularly one that diverges
from or supplements local protocol -- it should be named specifically.

Appropriate national CPG sources include:
- National Association of EMS Physicians (NAEMSP): position statements and CPGs
  on airway management, pain management, cardiac arrest, behavioral health restraint,
  and others
- National Association of State EMS Officials (NASEMSO): model protocols and
  national evidence-based guidelines
- American College of Emergency Physicians (ACEP): clinical policies applicable
  to prehospital settings
- Chief Paramedic-adopted national guidelines incorporated into local scope

Naming the CPG by title and source is the documentation standard when the guideline
was the operative basis. "Per NAEMSP 2023 CPG on prehospital pain management" is
more defensible than "per protocol" when the clinical decision required a nuanced
application of evidence rather than a simple protocol lookup.

---

Modern ePCR platforms (ESO, ImageTrend, Zoll RescueNet, EPCR, FirstWatch, and others)
capture a large volume of data in structured fields: vital signs, exam findings,
medications administered, times, GCS components, cardiac rhythm interpretations, and more.

**The narrative does not re-list structured field content.** It adds what the structured
fields cannot capture:

| Structured fields capture | Narrative captures |
|---|---|
| Vital sign values | Trend significance, clinical meaning of trajectory |
| Medication name, dose, route, time | Why this medication, how dose was determined, what the response was, whether effects were anticipated or adverse |
| Exam findings (checkboxes, dropdowns) | Quality, interrelationship, trajectory; findings that don't fit dropdown options |
| GCS score | Baseline vs. current, quality of speech, cooperation with exam |
| Chief complaint (dropdown) | Patient's own words, onset narrative, pertinent positives and negatives |
| Protocol number (if captured) | Clinical reasoning connecting findings to protocol criteria |
| Transport destination | Why that destination, condition during transport, condition at arrival |

**The single exception**: A specific value may be referenced in the narrative when
reasoning requires it. Even then, reference minimally to support reasoning, not to
transcribe.

---

## Medical Necessity Documentation

For Medicare, Medicaid, and most commercial payers, the PCR must establish that:

1. The patient's condition required the level of care provided (ALS vs. BLS)
2. Transport by ambulance was medically necessary (the patient could not have been
   safely transported by other means)
3. The destination was appropriate

The narrative supports medical necessity by:
- Describing the acuity of the presentation, not just the diagnosis
- Documenting why the patient could not ambulate, sit upright, or tolerate non-ambulance
  transport (when applicable)
- Documenting interventions that required ALS scope (when billing at ALS level)
- For non-emergency transport: documenting the specific medical condition that precluded
  other means

Do not write "transport to hospital for further evaluation" without supporting context.
Write why the patient required evaluation and why paramedicine transport was the appropriate means.

---

## History Source and Reliability

Every subjective history must be attributed to its source. Sources in order of typical
reliability:

- **Patient** (most reliable for subjective complaints; less reliable when altered,
  intoxicated, or has cognitive impairment -- document this explicitly)
- **Family member or caregiver** (document relationship and whether they were present
  for the event)
- **Witness** (document role: bystander, coworker, first responder)
- **Medical records or transfer documentation** (document source: discharge summary,
  medication list, prior PCR)
- **Scene findings** (document what was observed, not inferred)

When history reliability is in question, say so explicitly and document why. "History
obtained from patient; reliability limited by altered mental status" is both accurate
and legally protective.

---

## Pain Assessment Documentation

For patients reporting pain:

- Document the patient's own description of the pain (quality, location, radiation,
  onset, duration, aggravating/relieving factors)
- Document a numeric or scale rating if obtained; if a rating could not be obtained
  (altered LOC, cognitive impairment, developmental disability, intubated), document
  why and note what behavioral indicators were used instead
- For medications given for pain: document the score before and the score after
  (or behavioral indicators before and after for nonverbal patients)
- Document the clinical goal for pain management and whether it was achieved

---

## Consent and Refusal Documentation

**For patients who accept care and transport**: Brief note that patient was informed
of findings, recommended treatment, and destination, and consented verbally/in writing
(per platform documentation). No elaboration needed unless consent was complex.

**For patients who refuse treatment or transport**:
- Document that the patient was informed of: the assessment findings, the working
  impression, the recommended treatment, the potential consequences of refusal including
  risk of serious harm or death
- Document that the patient demonstrated decision-making capacity: alert, oriented,
  able to articulate understanding of the risks, not under apparent influence of substances
  or condition that would impair judgment
- Document that the refusal was voluntary and free of coercion
- Document any treatments the patient did accept
- Document instructions given and follow-up recommended
- Document that the patient signed the refusal form (if applicable per platform)

When decision-making capacity is in doubt, document why it is in doubt. When capacity
appears intact, document the indicators (orientation, coherence of reasoning, ability
to repeat information back).

---

## Transfer of Care

The transfer of care section in the Plan must include:
- Identity of the receiving provider (name and credential/role, or "receiving RN" if
  name not obtained)
- Location of transfer (unit, bay, room number if applicable)
- Method of report (verbal, written, phone patch)
- Condition of patient at time of transfer (brief, not a full re-assessment)
- Any items transferred with the patient (medications, belongings, oxygen, equipment)
- Any items given to law enforcement or other agencies (forensic cases)

Do not leave the transfer of care implied. "Report given to ED staff" is insufficient.
"Verbal report given to receiving RN [name if obtained] in ED bay [number if known];
patient transferred to ED stretcher in [position] with IV intact" is the standard.

**IMIST-AMBO Handoff Framework**

IMIST-AMBO is a validated structured handoff framework developed specifically for
paramedicine-to-hospital transfer of care. It is the recommended structure for verbal
reports and the documentation standard for what the handoff report contained. When
IMIST-AMBO was used, the narrative should reflect that the report was structured and
identify any elements that required elaboration beyond the standard framework.

The IMIST-AMBO elements:

- **I -- Identification**: Age, sex, and weight if clinically relevant (pediatric
  or weight-based medication dosing). No patient name (PHI rule) -- use "John Doe"
  or "Jane Doe" only if a placeholder reference is needed.
- **M -- Mechanism/Medical complaint**: Mechanism of injury for trauma (including
  kinematics and energy transfer); chief complaint and onset for medical.
- **I -- Injuries/Information**: Injuries identified for trauma, listed anatomically;
  relevant clinical information for medical (pertinent positives and negatives,
  clinical findings that drove assessment).
- **S -- Signs**: Vital signs and level of consciousness at initial contact and trend
  during the encounter. GCS components for altered mental status. RASS if relevant.
- **T -- Treatment and trends**: Interventions performed chronologically, patient
  response to each, and trend in condition. This is the core clinical reasoning
  section of the handoff.
- **A -- Allergies**: Known allergies and reaction type.
- **M -- Medications**: Current medications relevant to the presenting problem.
  MAT, anticoagulants, antihypertensives, insulin, and psychotropic medications
  are the categories most likely to affect receiving provider decision-making.
- **B -- Background history**: Pertinent past medical and surgical history.
- **O -- Other information**: Anything not captured above that the receiving provider
  needs: social context relevant to disposition, patient preferences or advance
  directives, family present and their role, forensic considerations, follow-up
  already arranged.

**Trauma Handoff -- ATLS Standard**

For trauma patients transferred to a trauma center or emergency department, the
handoff should meet the standard articulated in the Advanced Trauma Life Support
(ATLS) program, 11th edition. The ATLS trauma handoff standard emphasizes: mechanism
and kinematics communicated with precision sufficient for the receiving team to
reconstruct the injury environment, prehospital vital sign trend (not just arrival
values), interventions and response documented in sequence, and identification of
any clinical concern the receiving team should evaluate that was not fully assessed
in the prehospital setting.

The narrative documents that a structured trauma handoff was performed and captures
any elements of clinical significance that the structured report conveyed -- in
particular, mechanism detail, vital sign trajectory, and any deterioration or
unexpected response to treatment that the receiving team must know.

---

## Scene Observations

Scene observations belong in the Objective section. They inform clinical reasoning and
belong in the narrative when they are relevant to:
- Mechanism of injury (fall from height, vehicle intrusion, ejection, entrapment)
- Likely medical cause (found position, pill bottles, paraphernalia, environmental hazards)
- Safety and scene management (delayed access, hazardous environment, law enforcement
  involvement)
- Forensic considerations (see Forensic Standard in SKILL.md)

Document scene observations as observations. "Empty pill bottles of [medication] found
at bedside per family" is documentation. "Patient appears to have overdosed on [medication]"
is an interpretation -- document it in the Assessment section as a differential, not in
the Objective section as a fact.

---

## EtCO2 Documentation Guidance

EtCO2 is a waveform plus a value. The narrative adds what the structured value alone
cannot convey:

- **Waveform morphology**: Normal capnogram (plateau with square wave), shark fin
  (obstructive pattern), prolonged upstroke without plateau, dampened or absent waveform
- **Trend**: Rising, falling, stable, response to intervention (bronchodilator, ventilation
  rate change, ROSC)
- **Clinical interpretation**: EtCO2 in context of the presentation (low EtCO2 in
  hyperventilation vs. poor perfusion vs. metabolic acidosis; high EtCO2 in COPD baseline
  vs. acute hypoventilation)

Do not simply state "EtCO2 as charted." If EtCO2 is driving clinical reasoning, describe
the waveform and trend. If it is unremarkable, a brief reference is sufficient.

---

## Non-Accidental Trauma Indicators (Pediatric and Vulnerable Adult)

When caring for a pediatric patient or a vulnerable adult (elderly, cognitively impaired,
developmentally disabled), and the presentation or history raises concern for non-accidental
trauma, the narrative must:

- Document the stated mechanism and the stated history, attributed to their source
- Document any inconsistency between the stated mechanism and the injury pattern, described
  factually and without legal characterization
- Document developmental stage if relevant to assessing whether the stated mechanism is
  plausible
- Document who was present at the time of injury per stated history
- Document any spontaneous statements made by the patient (verbatim if possible)
- Document notifications made (law enforcement, child protective services, hospital social
  work) and to whom
- Apply the full forensic standard from SKILL.md

**Do not conclude abuse or neglect in the narrative.** Document the observations and
inconsistencies factually. The conclusion belongs to investigators and clinicians with
that authority.

---

## Stroke Documentation

For suspected stroke:

- Document last known well (LKW) time precisely, with source: "patient states she was
  last known well at approximately [time] when [activity]" or "per family, patient was
  speaking normally at [time]."
- Document Cincinnati or NIHSS findings as observed and assessed (not just the score)
- Document blood glucose result and clinical significance
- Document symptom onset narrative: sudden vs. gradual, progression, associated symptoms
- Document destination rationale when a stroke center was chosen over a closer facility

LKW is a time-sensitive data point that directly affects eligibility for fibrinolysis and
thrombectomy. It must be precise, sourced, and in the narrative even if also captured in
a specialty stroke form.

---

## STEMI Documentation

For suspected STEMI:

- Document the clinical presentation that prompted 12-lead acquisition
- Document the interpretation of the 12-lead (STEMI criteria met in which leads,
  reciprocal changes if present) -- this is narrative explanation of the clinical decision,
  not a replacement for the attached 12-lead data
- Document cath lab activation: who was notified, by what means, at what point in the
  encounter (if not captured in structured fields)
- Document patient response to any interventions (aspirin effect on pain, nitrate response
  if given, hemodynamic response)
- Document any contraindications to standard interventions if medications were withheld
- Document transport position and any hemodynamic changes during transport

---

## Airway Intervention Documentation

For any airway intervention beyond BVM ventilation:

- Document the indication (failed airway, anticipated failure, inability to maintain
  airway, oxygenation/ventilation failure)
- Document the attempt sequence: number of attempts, device used, result, complications
  at each attempt
- Document confirmation of placement: primary confirmation method (waveform capnography),
  secondary confirmation (breath sounds, chest rise, tube depth and position)
- For RSI or DSI: document sedation and paralytic indication, dose calculation (with weight
  used), anticipated vs. adverse effects, hemodynamic response, timing of intubation
  relative to medication administration
- Document post-intubation management: ventilator settings or BVM rate and volume,
  EtCO2 target and achieved value, sedation if maintained

---

## Cardiac Arrest Documentation

For cardiac arrest:

- Document presenting rhythm (first rhythm observed, not assumed)
- Document CPR quality indicators if available (feedback device data, or provider
  assessment of rate and depth)
- Document time to first defibrillation if applicable
- Document medication sequence with rationale (not dose and time -- those are in the
  flowchart -- but why each medication was given in the sequence it was)
- Document ROSC: time, presenting rhythm at ROSC, hemodynamics, mental status
- Document post-ROSC management: destination rationale (cath lab-capable facility),
  targeted temperature management decision, hemodynamic support
- For termination of resuscitation: document criteria met per protocol, Chief
  Paramedic contact if required, family notification

---

## Behavioral Health Documentation

This section covers all paramedicine encounters involving behavioral health: standard
emergency responses, dedicated crisis responses, co-response models, and community
paramedicine behavioral health visits. Documentation requirements vary by response
model and are organized accordingly below.

---

### Standard Behavioral Health Encounters

For any patient in behavioral health crisis, regardless of response model:

- Document the patient's behavior and presentation in observable terms, not diagnostic
  terms. "Patient is pacing, speaking rapidly, and expressing that others intend to
  harm him" is documentation. "Patient is paranoid and manic" is not.
- Document RASS (Richmond Agitation-Sedation Scale) at initial contact and after any
  intervention affecting level of consciousness or agitation. Document trajectory when
  the level changed during the encounter -- the endpoint value alone is insufficient
  for clinical handoff and quality review.
- Document safety risk assessment: whether the patient expressed suicidal or homicidal
  ideation, plan, or intent, in the patient's own words where possible. If the Columbia
  Suicide Severity Rating Scale (C-SSRS) or equivalent was applied, document the level
  and the clinical elements that drove it, not just the category.
- Document capacity assessment: ability to engage, articulate understanding of the
  situation, and participate in decision-making.
- Document the basis for involuntary hold if applicable: criteria met, statutory
  authority cited, notifications made per jurisdictional requirement.
- Document scene safety: law enforcement presence and role, de-escalation approach
  used (see De-escalation Documentation in SKILL.md), restraint if applied (document
  indication, type, position, monitoring, and patient response).

---

### Crisis Response and Co-Response Models

Apply this subsection to: dedicated crisis responses (paramedicine without law
enforcement), co-responses (paramedicine paired with a behavioral health clinician,
navigator, or peer support specialist), and any call where clinical decision-making
authority was shared with or led by a non-paramedic clinician.

Co-response and crisis response models involve shared clinical authority, non-standard
disposition pathways, and handoff structures that standard PCR fields were not designed
to capture. The narrative must establish role clarity, disposition rationale, and
continuity of care that a standard emergency response record does not require. The
standard behavioral health documentation requirements above apply in full; the
following additions are required.

**Response composition**

- Agencies and roles present: paramedicine crew, behavioral health clinician or
  navigator (name, credential, and agency if obtainable), law enforcement (agency
  and officer identifier if present and relevant), mobile crisis team, peer support
  specialist, or other. Document who was present and what their clinical or
  operational role was, specifically.
- Clinical decision-making lead: who held clinical authority for the patient contact.
  If the model is protocol-defined or CPG-defined, name the protocol or guideline.
- Law enforcement role: whether present, at whose request, whether they had clinical
  involvement or maintained a safety perimeter, and whether their involvement was
  required for scene safety or was incidental to the response.

**Disposition with explicit reasoning**

- Destination: emergency department, crisis stabilization unit (CSU), behavioral
  health urgent care, psychiatric emergency service, detoxification facility, shelter,
  patient's home with follow-up, or no transport.
- For any non-ED disposition, document the clinical and structural basis: clinical
  acuity assessment with scoring tool result if applied, availability of the
  alternative destination in the service area, protocol or CPG basis for the
  diversion, and patient agreement or statutory authority for the disposition.
  Consistent documentation of appropriate alternative dispositions builds the
  evidence base for their reimbursement and normalization -- what the narrative
  establishes today shapes what becomes standard practice tomorrow.
- Voluntary vs. involuntary: statutory authority cited, criteria met, notifications
  made per jurisdictional requirement.
- Handoff and continuity of care: to whom care was transferred, in what setting,
  by what method. Follow-up arranged, by whom, and when.

**What the narrative must establish**

For any crisis or co-response call, a reader must be able to answer from the
narrative alone: who was there and in what role, who held clinical responsibility,
what the patient's condition was at each stage, what disposition was chosen and on
what clinical and structural basis, and what happens next for this patient.

---

### Community Paramedicine Behavioral Health Visits

When the response is a community paramedicine visit for a behavioral health concern --
whether scheduled follow-up, referral-based, or diverted from a 911 call -- the
standard behavioral health documentation requirements apply where relevant, with the
following additions:

- Reason for visit: scheduled follow-up, referral source (agency, provider, or
  self-referral), or diversion from a 911 call to the community paramedicine program.
- Presenting behavioral health concern and its relationship to any prior acute event,
  hospitalization, or crisis contact.
- Assessment performed: mental status, safety assessment using a validated instrument
  if applied, medication adherence, functional status, living situation stability.
- Resources activated or connected: behavioral health provider contacted or scheduled,
  medication refill arranged, crisis plan reviewed or updated, family or support
  person engaged, other community resources connected.
- Disposition and next scheduled contact.

---

## Barriers to Care

Barriers encountered during the call belong in the narrative because structured fields
do not capture them. Document barriers factually. Use patient-reported language for
anything the patient stated. Do not speculate about systemic origins.

Categories that warrant narrative documentation when present:

- **Access and system delays**: Extended response interval and reason, delayed or
  incorrect dispatch, scene access difficulty (locked building, elevator, remote terrain,
  hazardous environment), staging for law enforcement clearance, time required to locate
  patient.
- **Physical environment**: Conditions that affected assessment or treatment -- confined
  space, extreme temperature, poor lighting, noise, hazardous materials precautions,
  presence of bystanders limiting examination.
- **Communication**: Language barrier and how addressed (professional interpreter,
  telephonic interpretation service, translation application, family member used with
  limitations noted), hearing impairment, speech impairment, cognitive impairment
  limiting history, altered mental status.
- **Patient-reported delays in seeking care**: Patient or family statement about why
  care was not sought sooner, documented as patient-reported when relevant to the
  clinical picture.
- **Care environment at origin**: Conditions at scene relevant to clinical reasoning --
  absence of caregiver, inaccessible medications, unsafe physical environment, absence
  of working utilities.
- **System-level factors affecting disposition**: Receiving facility diversion, absence
  of closer appropriate facility, transport interval affecting treatment decisions,
  specialty capability requiring bypass of closer facility.

---

## De-escalation Documentation

De-escalation used during a patient encounter is a clinical intervention and should
be documented with the same specificity applied to other interventions.

When a standardized technique was used (Crisis Intervention Team approach, verbal
de-escalation protocol, trauma-informed communication framework, or similar), document
the named approach, how it was applied, and the patient's response.

When a standardized technique was not named, document the elements: the patient's
presenting behavior, the communication and environmental approach used, any crew safety
measures in place, law enforcement presence and role, and the patient's response over
time. These elements, taken together, constitute the documentation of the de-escalation
intervention.

The narrative should establish what the de-escalation approach made possible -- whether
it enabled assessment, obtained consent, facilitated transport, or reduced the need for
restraint -- and over what timeframe the change occurred.

Document de-escalation in the Plan section. If the approach affected the assessment or
consent process, reference that connection in the Subjective or Objective section.

---

## Care Pathway and Alternative Disposition Documentation

This section applies to three call types: cancellations, patient refusals, and
low-acuity calls where no treatment was provided en route. It does not apply to
calls where the paramedicine response was clearly matched to an emergency-level need.

### Purpose

Structured PCR fields capture what happened on a call. They do not capture why the
call occurred, what the patient's underlying need was, what alternative care pathway
would have been appropriate, or what structural factors explain the gap between the
need and the response. That information lives, when it is documented at all, in the
narrative.

Systematic documentation of these elements serves two functions simultaneously.
For the individual encounter, it produces a complete clinical record of what was
assessed, what was offered, and what was arranged. For retrospective analysis, it
generates the data that can answer the questions driving paramedicine policy reform:
what proportion of responses were matched to emergency-level need, what structural
factors drove calls that did not require emergency response, and what alternative
care infrastructure would be needed to address those needs at lower cost and with
better patient experience.

The evidence base for community paramedicine and treatment-in-place reimbursement --
from the Renfrew County VTAC model, the federal ET3 demonstration, Florida's
on-scene treatment evaluation, and state programs in California, Oregon, and
elsewhere -- rests on exactly this kind of documentation. Individual PCR narratives,
aggregated across calls and providers, constitute the primary dataset from which
response appropriateness, alternative disposition potential, and unmet community
health need can be measured. Paramedics who document these elements accurately at
the point of care are contributing to the evidence base that supports the profession's
expansion beyond the emergency response frame.

### Cancellations

Document:
- Who cancelled (dispatch, requesting unit, law enforcement, caller, patient), at
  what point in the response, and on what stated basis. Attribute to source.
- Information available at cancellation: chief complaint as dispatched, any updates
  received en route, scene report from another unit if applicable.
- Whether the cancellation was based on clinical information or was administrative
  or operational in nature.
- Any unresolved clinical concern the responding paramedic held at the time of
  cancellation. Document the clinical basis for the concern factually. Do not
  characterize the cancellation decision as incorrect.

### Refusals

Standard refusal documentation requirements -- capacity assessment, informed refusal
process, instructions given, follow-up recommended -- are addressed in the core
documentation standards. The following elements are additional and specific to
care pathway analysis.

Document:
- **Presenting need as assessed**: The provider's clinical characterization of what
  the patient actually had, distinct from the dispatch complaint. Both should be
  documented; the gap between them is clinically and analytically significant.
- **Acuity at time of refusal**: The provider's assessment of acuity. If a scoring
  tool informed that assessment, document per the Scoring Tools standard.
- **Alternative care pathways offered**: What specific alternatives to transport
  were presented -- urgent care, primary care follow-up, telehealth, pharmacy,
  crisis line, community paramedicine follow-up if available in the service area.
  Document what was offered, not only that alternatives were discussed.
- **Patient's stated reason for refusing**: In the patient's own words where
  possible. Reasons with particular retrospective value include: cost or insurance
  concern, transportation barrier to follow-up, inability to leave home or
  dependents, prior negative experience with the healthcare system, preference for
  a specific provider or facility, and symptom minimization.
- **Situational and structural context**: Document only what is directly observable
  or patient-reported:
  - Absence of or inability to access a primary care provider
  - Recent discharge from hospital or emergency department for the same or related
    condition
  - Medication access issue (prescription unfilled, medication exhausted, cost
    barrier) as patient-reported
  - Caregiver absence or caregiver burden as relevant to the patient's situation
  - Transportation barrier to follow-up as patient-reported
  - Housing situation when directly relevant to the presenting condition
- **Disposition and follow-up**: Who was contacted, what resources were connected,
  whether community paramedicine or mobile integrated health follow-up was initiated
  or recommended, and what the patient was instructed to do.

### Low-Acuity Calls Without En Route Treatment

The threshold for applying this section: no medications administered, no procedures
performed, no cardiac monitoring initiated for clinical indication, and transport was
to an emergency department for a condition that could plausibly have been managed in
a lower-acuity setting.

Document:
- **Presenting need as assessed**: The provider's clinical characterization of what
  the patient had. Document both the dispatch complaint and the assessed condition.
- **Why emergency department**: The provider's reasoning when it goes beyond
  protocol default. If an alternative destination was clinically appropriate but
  unavailable, unauthorized by protocol, or not known to be available in the service
  area, document that specifically. This is documentation of a structural constraint,
  not a criticism of the transport decision.
- **Alternative destination availability**: Whether an alternative to the emergency
  department was considered, what alternatives exist in the service area, and why
  emergency department transport was the outcome. If the provider does not know what
  alternatives exist, mark [VERIFY] for agency follow-up -- this is itself a finding
  of operational significance.
- **Situational and structural context**: Same elements as refusals above, documented
  only when directly relevant to why this call occurred and why emergency department
  transport was the outcome.
- **Patient's statement about why they called 911**: In the patient's own words
  where possible. This is the highest-value narrative data point for population-level
  analysis of response appropriateness and is almost never captured in structured
  fields. A patient who says "I don't have a doctor" or "I couldn't get an
  appointment" or "I didn't know where else to go" is providing information that
  no structured field collects and that no retrospective analysis can recover if
  it is not documented at the time of the call.

---

## Recent Pregnancy and Maternal History

For any woman of childbearing age, the narrative should document whether she has been
pregnant within the last 12 months, regardless of presenting complaint. This is not
an obstetric documentation requirement -- it is a risk stratification requirement that
applies across presentations.

**Why the 12-month window matters clinically**

The postpartum period carries substantially elevated risk for a range of conditions
that paramedics encounter without any obvious obstetric context:

- **Peripartum cardiomyopathy**: Onset from the last month of pregnancy through 5
  months postpartum; may present with progressive dyspnea, orthopnea, chest pain,
  or acute decompensated heart failure. Frequently misattributed to other causes in
  the absence of a postpartum history.
- **Venous thromboembolism**: Risk is elevated through at least 12 weeks postpartum
  and remains above baseline through 6 months. DVT and pulmonary embolism in
  postpartum women are common and under-recognized in prehospital settings.
- **Postpartum hypertensive disorders**: New-onset or worsening hypertension,
  preeclampsia with severe features, and eclampsia can occur through 6 weeks
  postpartum and occasionally beyond. Headache, visual changes, epigastric pain,
  and altered mental status in a postpartum woman require this consideration.
- **Postpartum hemorrhage**: Secondary postpartum hemorrhage (occurring after 24
  hours and up to 12 weeks) may present as vaginal bleeding with or without
  hemodynamic compromise.
- **Postpartum sepsis**: Endometritis, wound infection, mastitis with progression
  to abscess or sepsis, and urinary tract infection are common postpartum infectious
  sources.
- **Postpartum psychiatric emergencies**: Postpartum depression, anxiety, and
  psychosis may present weeks to months after delivery. Postpartum psychosis in
  particular carries significant risk of harm to self and infant.

**Elements to document when the answer is yes**

Document in the Subjective section using GPAL format:

- **G -- Gravida**: Total number of pregnancies, including the current pregnancy
  if applicable, all losses, and all terminations regardless of outcome.
- **P -- Para**: Number of deliveries at or beyond 20 weeks, including live
  births and stillbirths. Does not include losses before 20 weeks.
- **A -- Abortus**: Number of pregnancies ending before 20 weeks, spontaneous
  and elective combined. If the patient distinguishes between the two and it is
  clinically relevant, document both.
- **L -- Living**: Number of living children. A separate count from Para -- a
  stillbirth counts in Para but not in Living; a surviving premature infant
  counts in Living.

Document as G_P_A_L_ (e.g., G3P2A1L2). If the patient cannot provide precise
counts, document what she reports and note the limitation.

Additionally document:
- Most recent pregnancy outcome (vaginal delivery, operative vaginal, cesarean,
  loss, termination) as patient-reported.
- Gestational age at delivery or loss (term at 37+ weeks, preterm with weeks
  if known, or gestational age at loss).
- **Estimated date of last delivery (EDLD)**: The date or approximate date the
  most recent pregnancy ended. If the patient does not know the exact date,
  document the approximate timeframe (e.g., "approximately 6 weeks ago per
  patient"). This is the primary risk-stratifying variable and should be
  documented even if approximate.
- Delivery complications as patient-reported (hypertensive disorders, hemorrhage,
  infection, ICU admission, readmission)
- Neonatal outcome only to the degree relevant to the clinical picture
- Current breastfeeding status when medication administration is involved
- Known postpartum diagnoses or ongoing postpartum care concerns
- Prenatal and postpartum care providers if relevant to transfer of care

**Assessment connection**

When recent pregnancy history is present and the presentation is consistent with a
postpartum condition, the Assessment section must make the connection explicit.
Documenting obstetric history in the Subjective section without connecting it to the
differential in the Assessment section fails the clinical reasoning standard. The
narrative should reflect that postpartum etiology was actively considered.

**If currently pregnant**

Document confirmed or suspected pregnancy. Prompt for:

- **Estimated gestational age (EGA)**: Ask in weeks. If the patient does not
  know weeks, ask for the estimated due date (EDD) and calculate approximate
  EGA from the current date. Document whichever the patient can provide and
  note the basis (patient-reported weeks, EDD calculation, or clinical
  estimation). EGA determines the viability threshold, guides treatment
  decisions, and informs destination rationale.
- **Estimated due date (EDD)**: Document if known. Provides a cross-check for
  EGA and is relevant to receiving facility handoff.
- Obstetric provider or midwife if known.
- Known complications of the current pregnancy.
- Fetal status if EGA is at or beyond the threshold of viability (generally 23
  weeks or beyond) and fetal assessment was performed.

**If recent pregnancy is denied**

Document the denial briefly. No further obstetric history is required unless the
presentation otherwise suggests it.

## Substance Use History

Substance use history is narrative-relevant when it affects clinical management,
medication selection, risk stratification, or disposition. Prompt for it when the
presentation suggests it is clinically material. Do not prompt universally.

**When to prompt**: Altered mental status, withdrawal signs or symptoms, intoxication,
trauma with mechanism suggesting impairment, behavioral health crisis, or any call
where the provider notes alcohol or substance involvement without providing clinical
detail.

**Alcohol use and withdrawal risk**

Alcohol use disorder is among the most prevalent conditions in prehospital patient
populations and among the most consequentially underdocumented. The clinical history
that changes management is specific:

- Current use pattern as patient-reported (daily use, quantity, duration of current
  drinking episode if relevant)
- Time and amount of last drink -- the foundational variable for withdrawal risk
  assessment and CIWA-Ar interpretation
- Prior alcohol withdrawal seizures -- must be documented explicitly when present;
  a patient with prior withdrawal seizures is at substantially higher risk of
  seizure in the current episode regardless of current CIWA-Ar score
- Prior delirium tremens (DTs) -- similarly high-risk historical marker; document
  explicitly
- Prior detoxification, hospitalization for withdrawal, or inpatient treatment
- Current sobriety, recovery program participation, or abstinence period if relevant

When alcohol withdrawal is in the differential, the narrative must establish the
clinical basis for that assessment beyond the CIWA-Ar score. The score quantifies
current severity. The history establishes risk trajectory. Both belong in the record.

**Other substances**

- Type of substance if known or reported by the patient or a reliable source.
  Do not speculate about substance type from presentation alone.
- Route of use when relevant to clinical management: intravenous use and infection
  risk, inhalation and respiratory considerations, insufflation and mucosal injury.
- Last use if relevant to withdrawal or toxicological timeline.
- Opioid use history and prior naloxone administration when relevant to dosing
  decisions and response expectations.

**Medication-assisted treatment (MAT)**

Current buprenorphine, methadone, or naltrexone should be documented when reported.
Each has direct implications for opioid dosing, withdrawal assessment, and
disposition decisions that the receiving provider must know.

**Screening instruments**

If AUDIT-C, CAGE, PHQ-2, or another validated screening instrument was applied,
document per the Scoring Tools standard: instrument name, result, and how it
informed clinical reasoning or disposition.

**Documentation standard**

Attribute all substance use history to its source: patient-reported, reported by
family or bystander (named or described by role), or directly observed. Use the
patient's own words where they are clinically significant. Do not characterize use
pattern as a legal or moral conclusion. "Patient reports daily alcohol use with
last drink approximately 18 hours prior to contact" is documentation. "Patient
appears to be an alcoholic" is not.

---

## Scoring Tools and Decision Instruments

When a validated scoring tool, clinical decision rule, or structured assessment
instrument was applied, the narrative must document the tool by name, the score or
result, the components that drove the score, and how the result informed clinical
reasoning or the transport decision. Structured PCR fields may capture the score.
The narrative captures the reasoning.

**Governing principle**: This list is not exhaustive. If any validated instrument
was applied that is not listed here, document it by name, state the result, identify
the components, and explain how it informed the clinical decision. The obligation is
to document the reasoning behind the tool's use, not to apply a specific tool. If a
relevant tool was considered but not applied, document that and the reason when the
omission is clinically meaningful.

**Cardiovascular**
- HEART Score (chest pain), if applied: note which components elevated the risk
  category and how the total informed disposition or treatment. Troponin is a
  laboratory value, not a field-available one -- document a HEART Score as
  calculated only if a troponin result was actually obtained (for example,
  point-of-care testing on a critical care transport unit). If troponin was not
  available, the score was not fully calculated; document what was assessed
  without presenting it as a completed HEART Score.
- Killip Classification when relevant to AMI severity documentation.

**Neurological**
- Cincinnati Prehospital Stroke Scale (CPSS): document which elements were
  positive. "CPSS" is the same instrument as the Cincinnati Prehospital Stroke
  Scale, not a separate tool -- it is a general stroke screen, not a large-vessel
  occlusion (LVO) screen.
- Los Angeles Prehospital Stroke Screen (LAPSS) if applied.
- GCS component scores (eye, verbal, motor) when clinical reasoning requires the
  breakdown, not just the total.
- VAN screen for large vessel occlusion consideration -- a distinct instrument
  from Cincinnati/CPSS. Document separately; a positive Cincinnati/CPSS does not
  by itself indicate a positive VAN.

**Respiratory**
- PERC rule: valid only for patients already assessed as low pretest probability
  for pulmonary embolism -- document that basis before which criteria were
  absent and the clinical conclusion.
- Wells Criteria for PE if applied.
- CURB-65 if relevant to pneumonia severity and transport decision. The "U"
  (urea/BUN) component is a laboratory value not generally available in the
  field. Document CURB-65 only when a urea/BUN value was actually obtained;
  otherwise the field-appropriate variant is CRB-65 (the same instrument without
  the urea component) -- name it as CRB-65 rather than presenting a partial
  CURB-65 as complete.

**Triage -- Mass Casualty and Multi-Patient Incidents**

- **SALT Triage** (Sort, Assess, Lifesaving Interventions, Treatment/Transport):
  SALT is the national standard for mass casualty and multi-patient triage in the
  United States. When SALT was applied, the narrative must document:
  - The scene-level sort findings: how patients were distributed across triage
    categories (Immediate, Delayed, Minimal, Expectant, Dead) and the basis for
    the overall incident triage picture.
  - For the specific patient being documented: the SALT category assigned, the
    assessment findings that drove that category (LSI response, breathing status,
    perfusion, and obedience to commands), and whether the category changed during
    the encounter and why.
  - Resource allocation decisions that followed from triage: transport sequence,
    destination assignment, interventions prioritized or deferred based on triage
    category.
  - Any lifesaving interventions (LSIs) performed during triage (hemorrhage control,
    airway opening, needle decompression, auto-injector administration) and their
    effect on the patient's triage category.

  SALT operates at the scene level, not the individual patient level. Document the
  triage picture for the scene, then document the individual patient encounter. Do
  not conflate the two -- the PCR documents one patient; the triage picture provides
  the clinical context in which that patient was encountered.

**Trauma**
- **Revised Trauma Score (RTS)**: Document components if calculated (GCS, SBP,
  RR) and how the score informed destination decision or clinical concern.
- **ACS Field Triage Decision Scheme** (National Guideline for the Field Triage of
  Injured Patients, American College of Surgeons, 2021 revision): the national
  standard for trauma center destination decisions. The 2021 revision organizes
  criteria into RED (high-risk) and YELLOW (moderate-risk) tiers, across four
  categories. When this framework was applied, document which specific criteria
  triggered the destination decision, organized by these categories:
  - *Injury Patterns* (RED): penetrating injuries to head, neck, torso, or
    proximal extremities; skull deformity or suspected skull fracture; suspected
    spinal injury with new motor or sensory loss; chest wall instability,
    deformity, or suspected flail chest; suspected pelvic fracture; suspected
    fracture of two or more proximal long bones; crushed, degloved, mangled, or
    pulseless extremity; amputation proximal to wrist or ankle; active bleeding
    requiring a tourniquet or wound packing with continuous pressure. Penetrating
    injury is an Injury Patterns criterion, not a Mechanism criterion.
  - *Mental Status and Vital Signs* (RED): unable to follow commands (motor GCS
    <6 -- not total GCS); RR <10 or >29 breaths/min; respiratory distress or need
    for respiratory support; room-air SpO2 <90%. Systolic BP thresholds are
    age-banded: age 0-9, SBP <70 + (2 x age in years); age 10-64, SBP <90 mmHg or
    heart rate greater than SBP; age 65+, SBP <110 mmHg or heart rate greater
    than SBP.
  - *Mechanism of Injury* (YELLOW): high-risk auto crash (partial or complete
    ejection; significant intrusion, >12 inches at the occupant site or >18
    inches at any site; need for extrication; death in the passenger
    compartment; unrestrained child age 0-9 or in an unsecured child safety
    seat; vehicle telemetry data consistent with severe injury); rider separated
    from a transport vehicle with significant impact (motorcycle, ATV, horse, or
    similar); pedestrian or bicycle rider thrown, run over, or with significant
    impact; fall from height greater than 10 feet (all ages).
  - *EMS Judgment* (YELLOW, considered alongside the above): low-level falls in
    young children (age 5 or younger) or older adults (age 65 or older) with
    significant head impact; anticoagulant use; suspicion of child abuse;
    special, high-resource healthcare needs; pregnancy greater than 20 weeks;
    burns in conjunction with trauma; preference for pediatric-capable centers
    for children.
  Document which specific criterion or criteria were met, not only the
  destination outcome. "Transported to Level I trauma center per ACS Field
  Triage criteria -- Mental Status and Vital Signs criterion met (motor GCS 4,
  SBP 88)" is the documentation standard. The criterion drives the decision;
  the decision alone does not document the criterion.
  Source: American College of Surgeons, *National Guideline for the Field
  Triage of Injured Patients* (2021), facs.org/fieldtriageguidelines.
- **Ottawa Knee or Ankle Rules** if applied and relevant to transport or treatment.

**Toxicological and substance use**
- CIWA-Ar: document the total score, which domain scores were elevated (tremor,
  diaphoresis, anxiety, agitation, perceptual disturbances, headache, nausea,
  orientation), and how the score informed treatment and destination decisions.
- COWS: document total score, elevated domains, and treatment rationale.
- Poison severity scoring if applied.

**Screening instruments (when applied per protocol or provider discretion)**
- AUDIT-C (Alcohol Use Disorders Identification Test, Consumption subscale): a
  three-item screen for hazardous drinking. Document the score and the clinical
  context that prompted its use.
- CAGE (Cut down, Annoyed, Guilty, Eye-opener): a four-item screen for alcohol
  use disorder. Document the number of positive responses and the clinical context.
- PHQ-2 (Patient Health Questionnaire, 2-item): depression screening. Document
  the score and how it informed assessment or disposition.

**Obstetric**
- Apgar score components when documenting newborn assessment.

**Behavioral health**
- C-SSRS level if applied; document the clinical elements that drove the category,
  not just the label.

---

*This primer reflects universal paramedicine documentation standards as of 2026.
Agency-specific policies take precedence where they differ. When in doubt, apply the
more stringent standard.*
