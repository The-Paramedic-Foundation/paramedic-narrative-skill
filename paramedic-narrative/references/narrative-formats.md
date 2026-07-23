# Narrative Formats Reference

**The Paramedic Foundation** · paramedicfoundation.org · Version 1.4.0

Section definitions and quality checklists for every narrative format supported by
the Paramedic-Narrative skill. The active format is declared in the agency
configuration with per-call override. If no format is declared, SOAP with Clinical
Summary is the default.

**Universal rules that apply in every format:**

- All core standards apply regardless of format: never invent detail, [VERIFY]
  tagging, ABC/LOC cluster treatment, medication administration standard,
  controlled substance audit trail, forensic and evidentiary standard, scoring
  tools documentation, style rules, and the standing provider review disclaimer.
- The narrative explains WHY; structured ePCR fields hold WHAT and WHEN. No format
  is an excuse to restate structured data.
- Each fact appears once, in the section where it does the most work.
- The Clinical Summary statement is an optional labeled opening paragraph
  compatible with every format below.

**Universal quality checklist (apply to every draft, then apply the
format-specific checklist):**

1. No invented, assumed, or inferred clinical detail anywhere.
2. Every unresolved item tagged [VERIFY].
3. No duplication of structured field content or across sections.
4. History attributed to source with reliability noted when in question.
5. Clinical reasoning present: working impression, alternatives considered,
   protocol or CPG named.
6. Medication and controlled substance standards met when applicable.
7. Forensic standard applied when triggered.
8. Transfer of care documented: receiving provider, condition at transfer, items
   transferred.
9. Standing provider review disclaimer appended.

---

## SOAP (default)

**Sections:** Clinical Summary (optional) / Subjective / Objective / Assessment /
Plan

- **Subjective**: History not in structured fields. History source and
  reliability. Pertinent positives and negatives. Cognitive/communication status
  when relevant. Source-attributed statements and verbatim quotes for forensic
  cases.
- **Objective**: ABC/LOC quality, interrelationship, and trajectory. Scene
  observations relevant to decision-making. Findings not in structured fields.
  Reference structured data ("vitals and cardiac monitoring as charted").
- **Assessment**: Protocol or CPG by name or number. Clinical reasoning connecting
  findings to working diagnosis. No restatement of S or O.
- **Plan**: Chronological. Treatment rationale, medication indication, dose
  calculation, response, complication characterization. Controlled substance audit
  trail. Transport decision and rationale. Condition at destination. Transfer of
  care.

**Checklist:** reasoning lives in Assessment, not scattered; Plan is chronological;
no S/O content repeated in A.

---

## SOAPE

**Sections:** SOAP plus **Evaluation**

- **Evaluation**: Patient response to the overall treatment plan, reassessment
  findings and trajectory, condition at transfer of care, and whether clinical
  goals were met. Move response-to-intervention content here rather than leaving
  it all in Plan.

**Checklist:** SOAP checklist, plus: Evaluation covers trajectory and goal
attainment, not a restatement of Plan; final patient condition explicit.

---

## SOAPIER

**Sections:** Subjective / Objective / Assessment / Plan / Intervention /
Evaluation / Revision

- **Plan**: The intended course of care and its rationale, stated prospectively.
- **Intervention**: What was actually done, chronologically, with indication and
  dose rationale. Controlled substance audit trail lives here.
- **Evaluation**: Patient response to each intervention and overall trajectory.
- **Revision**: Any change to the plan based on response -- what changed, why, and
  the result. If the plan was not revised, state that care proceeded as planned.

**Checklist:** Plan states intent, Intervention states action, Evaluation states
response, Revision states adaptation; the four are not blended.

---

## CHART

**Sections:** Chief complaint / History / Assessment / Rx (Treatment) / Transport

- **Chief complaint**: In the patient's words where possible, with source.
- **History**: HPI, pertinent positives and negatives, history source and
  reliability, relevant context not in structured fields.
- **Assessment**: Exam and ABC/LOC narrative treatment plus working impression
  with reasoning and protocol/CPG reference. In CHART, clinical reasoning lives
  here.
- **Rx (Treatment)**: Chronological treatments with indication, dose rationale,
  response, complications. Controlled substance audit trail.
- **Transport**: Destination and rationale, movement method, position, condition
  en route and on arrival, transfer of care.

**Checklist:** chief complaint attributed; Assessment carries both findings and
reasoning; Transport ends with transfer of care.

---

## CHARTE

**Sections:** CHART plus **Exceptions**

- **Exceptions**: Anything unusual: refusals of specific interventions, delays and
  causes, equipment issues, protocol deviations with rationale and medical
  direction contact if made, and anything a reviewer should understand.

**Checklist:** CHART checklist, plus: exceptions actually exceptional (not routine
content moved down); protocol deviations paired with rationale.

---

## DCHART-E

**Sections:** Dispatch / Chief complaint / History / Assessment / Rx (Treatment) /
Transport / Exceptions

- **Dispatch**: Dispatch complaint, response mode, scene type, other agencies and
  roles, delays and why. The call frame.
- Remaining sections as in CHARTE.

**Checklist:** CHARTE checklist, plus: Dispatch captures the response picture
including delays and mutual aid roles.

---

## CHRONOLOGICAL

**Sections:** Single timeline narrative from dispatch to transfer of care.

- Ordered strictly by sequence: dispatch and response, arrival picture, patient
  contact and history, assessment findings, each intervention with indication and
  response at the point in the timeline it occurred, transport decision,
  en route course, arrival condition, transfer of care.
- Clinical reasoning is woven in at the decision points where it occurred ("Given
  the positive Cincinnati and last known well of 0830 per spouse, transport was
  initiated emergent to...").

**Checklist:** sequence unambiguous without repeating structured timestamps;
reasoning attached to each decision point; no orphan findings without narrative
purpose.

---

## HEAD-TO-TOE

**Sections:** Scene and history context, then systems-based exam narrative (head,
neck, chest, abdomen, pelvis, extremities, neurological, skin), then impression,
treatment, and transport. Common for trauma.

- Exam narrative documents pertinent findings and pertinent negatives by region,
  limited to what is not captured in structured exam fields or what drove
  decisions.
- Mechanism of injury and kinematics documented with the specificity the forensic
  or trauma standard requires.
- Impression connects the injury pattern to the working assessment and destination
  decision (ACS Field Triage criterion when applicable).

**Checklist:** regions with findings addressed and clinically significant
negatives included; mechanism detail sufficient to justify the destination and SMR
decisions; no full restatement of the structured exam.

---

## DRAATT

**Sections:** Dispatch / Response / Arrival / Assessment / Treatment / Transport

- **Dispatch**: Complaint as dispatched, unit, response mode.
- **Response**: Anything notable en route -- updates, staging, delays.
- **Arrival**: Scene picture, where the patient was found, first impression, who
  was present.
- **Assessment**: History with source, exam highlights, ABC/LOC treatment, working
  impression with reasoning and protocol reference.
- **Treatment**: Chronological interventions with indication, response,
  complications. Controlled substance audit trail.
- **Transport**: Destination rationale, en route course, condition on arrival,
  transfer of care.

**Checklist:** Response and Arrival distinct (en route vs. on scene); Assessment
carries the reasoning; Transport ends with handoff.

---

## AT CHART

**Sections:** Arrival / Treatment / Chief complaint / History / Assessment / Rx /
Transport

- **Arrival**: Scene picture and first impression on contact.
- **Treatment (initial)**: Immediate lifesaving or stabilizing interventions
  performed on contact, before or during the primary assessment, with indication.
- Remaining sections as in CHART; **Rx** carries subsequent treatments after the
  initial stabilization.

**Checklist:** initial stabilization clearly separated from subsequent treatment;
no duplication between Treatment and Rx; reasoning in Assessment.

---

## FACT

**Sections:** Findings / Assessment / Care / Transport

A lean format for BLS and low-acuity calls.

- **Findings**: Presentation, history highlights with source, pertinent negatives,
  exam highlights.
- **Assessment**: Working impression and reasoning, protocol reference.
- **Care**: What was done and the response; what was considered and withheld with
  rationale.
- **Transport**: Destination and rationale, or disposition if not transported
  (apply the care pathway documentation standard for low-acuity calls).

**Checklist:** lean but complete -- medical necessity still established; care
pathway elements documented for low-acuity ED transports; brevity never achieved
by omitting reasoning.

---

## REFUSAL / NON-TRANSPORT Template

**Sections:** Encounter context / Capacity assessment / Informed refusal process /
Alternatives offered / Witness / Disposition and follow-up

- **Encounter context**: Dispatch complaint, presenting need as assessed, acuity
  assessment at time of refusal.
- **Capacity assessment**: The clinical basis for decision-making capacity:
  orientation, understanding of condition and risks, ability to communicate a
  consistent choice, absence of impairing condition -- documented as assessed, not
  as a conclusion alone.
- **Informed refusal process**: Risks explained in plain language (including the
  specific risks of non-transport for this presentation), patient's demonstrated
  understanding, patient's stated reason for refusal in their own words.
- **Alternatives offered**: Specific alternatives discussed (urgent care, primary
  care, telehealth, crisis line, CP/MIH follow-up) and the patient's response to
  each.
- **Witness**: Who witnessed the refusal (name, role); signature status per agency
  policy; per the agency protocol cited in the agency configuration.
- **Disposition and follow-up**: Instructions given, who remains with the patient,
  callback guidance, any follow-up arranged. Apply the care pathway documentation
  standard for refusals.

**Checklist:** capacity documented with its clinical basis; risks specific to the
presentation, not generic; refusal reason patient-attributed; witness and agency
protocol named; follow-up explicit.

---

## IFT Template

**Sections:** Transfer context / Sending report / Patient at transfer /
Care during transport / Arrival and handoff

- **Transfer context**: Sending and receiving facilities and providers, reason for
  transfer, medical necessity for the level of transport (why this level of care
  and crew configuration was required).
- **Sending report**: Who gave report, patient course at sending facility as
  reported, records, imaging, and belongings accompanying the patient.
- **Patient at transfer**: Condition at time of custody transfer to the transport
  crew, lines, drips with rates, devices, airway status, monitoring in place.
- **Care during transport**: Monitoring, titrations, interventions en route with
  indication and response; critical care values where applicable (ventilator
  settings, vasoactives, invasive monitoring).
- **Arrival and handoff**: Condition on arrival, receiving provider (name and
  role), report given, lines/devices/records/belongings transferred.

**Checklist:** medical necessity for transport level explicit; every line, drip,
and device accounted for at both ends; en route changes paired with rationale and
response.

---

## CUSTOM

Agency-defined section order stored in the agency configuration. When CUSTOM is
declared, the configuration must list the section names in order and what belongs
in each. Apply the universal rules and quality checklist, mapping content standards
onto the agency's sections. If the configuration declares CUSTOM but does not
define the sections, ask once and mark the format [VERIFY] until defined.

---

*Published by The Paramedic Foundation under CC BY 4.0.*
*paramedicfoundation.org · info@paramedicfoundation.org*
