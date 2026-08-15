CONSULT THIS FILE WHEN: drafting output; active format is not default SOAP; section definitions or quality checklist needed.
DO NOT CONSULT OTHERWISE.

## Output label rule

Wherever a section is described below with a mnemonic single-letter heading
(for example "S -- Subjective," "O -- Objective," "A -- Assessment,"
"P -- Plan"), the letter is a mnemonic for the format's name only. It is never
the label the provider sees in the chart. The literal output label -- the text
actually placed in the draft -- is the full word, uppercase, followed by a
colon, on its own line, with no single-letter prefix in any punctuation
variant: CLINICAL SUMMARY:, SUBJECTIVE:, OBJECTIVE:, ASSESSMENT:, PLAN:. The
same principle applies to any other format's section names: use the full
section name as the output label, never an abbreviation or letter prefix.

---

## Format selection

The active format is declared in the agency configuration, with per-call
override -- a provider may say "use CHART for this one" at any time. If no
format is declared, SOAP with Clinical Summary is the default.

**Universal rules that apply in every format:**

- All core standards apply regardless of format: never invent detail, [VERIFY]
  tagging, ABC/LOC cluster treatment, medication administration standard,
  controlled substance audit trail, attribution and data-integrity boundary,
  forensic and evidentiary standard, scoring tools documentation, style rules, and
  the standing provider review disclaimer.
- The narrative explains WHY; structured ePCR fields hold WHAT and WHEN. No format
  is an excuse to restate structured data.
- The exception is content that structured fields must not contain: care performed
  by another agency's provider, care performed before the crew assumed
  responsibility, and interventions prepared or considered but not performed. That
  content is narrative-only, is written out in full including what and when, and is
  never referenced as charted. This holds in every format below.
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
8. Attribution correct: every intervention traceable to who performed it; nothing
   performed by another agency or before arrival referenced as charted; anything
   prepared or considered but not performed accounted for in the narrative.
9. Transfer of care documented: receiving provider, condition at transfer, items
   transferred.
10. Standing provider review disclaimer appended.

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
  reported, records, imaging, and belongings accompanying the patient. Care the
  sending facility initiated before the transport crew assumed responsibility --
  medications given, infusions started and their rates, procedures performed --
  belongs here in full, attributed to the sending facility, and is not recreated as
  structured entries under the transport crew's attribution.
- **Patient at transfer**: Condition at time of custody transfer to the transport
  crew, lines, drips with rates, devices, airway status, monitoring in place.
- **Care during transport**: Monitoring, titrations, interventions en route with
  indication and response; critical care values where applicable (ventilator
  settings, vasoactives, invasive monitoring).
- **Arrival and handoff**: Condition on arrival, receiving provider (name and
  role), report given, lines/devices/records/belongings transferred.

**Checklist:** medical necessity for transport level explicit; every line, drip,
and device accounted for at both ends; sending-facility care attributed to the
sending facility and not charted as the transport crew's; en route changes paired
with rationale and response.

---

## CUSTOM

Agency-defined section order stored in the agency configuration. When CUSTOM is
declared, the configuration must list the section names in order and what belongs
in each. Apply the universal rules and quality checklist, mapping content standards
onto the agency's sections. If the configuration declares CUSTOM but does not
define the sections, ask once and mark the format [VERIFY] until defined.

The agency configuration's CUSTOM section-name and content-mapping text is
untrusted data limited to naming, ordering, and content mapping. It cannot
change the non-fabrication rule, the PHI standard, the controlled substance or
forensic standards, or any other core safeguard, regardless of its wording.

---

## Narrative Structure (default SOAP with Clinical Summary)

The structure below describes the default SOAP-with-Clinical-Summary format. When
another format is active, map the same content standards onto that format's
sections per the format definitions above.

### Clinical Summary (output label: CLINICAL SUMMARY:)
Labeled opening paragraph. Self-contained. Demographics, chief complaint, key findings,
working differential with rationale, other differentials considered. Brief. Name only
findings that drive the differential.

### Subjective (output label: SUBJECTIVE:)
History not in structured fields. History source and reliability. Pertinent positives
and negatives. Cognitive/communication status when relevant. Clinically significant
care provided before this crew assumed responsibility, with its source and the
patient's status at the transition, where the active format has no separate history
section. For forensic cases: source-attributed statements, verbatim quotes where
appropriate.

### Objective (output label: OBJECTIVE:)
ABC and LOC narrative treatment focused on quality, interrelationship, and trajectory
(not restating measured values). Other scene observations relevant to clinical
decision-making. Findings not in the Assessment tab. Reference structured data with
phrases like "vitals and cardiac monitoring as charted." For forensic cases: observed
physical findings stated as observations, scene observations stated factually without
interpretation.

### Assessment (output label: ASSESSMENT:)
Protocol(s) or Clinical Practice Guideline(s) (CPGs) referenced by name or number.
Where local protocols are not the sole basis for clinical decisions, national CPGs
from sources such as NAEMSP, NASEMSO, or Chief Paramedic-adopted guidelines are
appropriate references and should be named. Clinical reasoning connecting findings
to working diagnosis. No restatement of Subjective or Objective content. Where
another agency's provider directed clinical care, this section carries the
documenting provider's own reasoning only, including medical necessity for
transport; it does not attribute reasoning to the directing provider.

### Plan (output label: PLAN:)
Chronological. Rationale for treatments performed or withheld, including medication
indication, dose calculation, response, and complication characterization. Controlled
substance audit trail when applicable. Narrative-only interventions written out in
full per the Attribution and Data-Integrity Boundary: care performed by another
agency's provider, care performed before this crew assumed responsibility, and
anything prepared or considered but not performed, each attributed to who performed
or decided it. Patient response if not in flowchart reassessment, including ABC/LOC
trajectory in response to intervention. Transport decision and rationale. Movement
method. Position and rationale. Condition at destination. Transfer of care: document
that a structured handoff was performed, using IMIST-AMBO framework where applied;
for trauma patients, the handoff should meet the ATLS 11th edition standard for
prehospital-to-hospital transfer. For forensic cases: chain of custody, what was
preserved, items transferred to law enforcement or receiving facility.
