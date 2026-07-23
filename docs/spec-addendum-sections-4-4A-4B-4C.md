# Narrative Documentation Assistant — Specification Addendum

This addendum replaces Section 4 of the prior specification and adds Sections 4A, 4B, and 4C, plus an addition to the Section 6 acceptance criteria. All other sections of the prior version stand.

---

## Revised Section 4. Multi-Format Support (Expanded)

Add native support for the following narrative formats, each with its own structural template, section definitions, and quality checklist in `docs/`. Format is declared in the agency profile with per-call override.

a. **SOAPE** — Clinical Summary plus Subjective, Objective, Assessment, Plan, Evaluation
b. **SOAP** — standard four-section variant
c. **SOAPIER** — Subjective, Objective, Assessment, Plan, Intervention, Evaluation, Revision
d. **DCHART-E** — Dispatch, Chief complaint, History, Assessment, Rx/Treatment, Transport, Exceptions
e. **CHART** — Chief complaint, History, Assessment, Rx/Treatment, Transport
f. **CHARTE** — CHART plus Exceptions
g. **CHRONOLOGICAL** — timeline narrative from dispatch to transfer of care
h. **HEAD-TO-TOE** — systems-based exam-driven narrative, common for trauma
i. **DRAATT** — Dispatch, Response, Arrival, Assessment, Treatment, Transport
j. **AT CHART** — Arrival, Treatment, Chief complaint, History, Assessment, Rx, Transport
k. **FACT** — Findings, Assessment, Care, Transport; a lean format for BLS and low-acuity calls
l. **REFUSAL/NON-TRANSPORT** template — capacity assessment, risks explained, alternatives offered, who witnessed, per the agency's refusal protocol as cited in the agency configuration
m. **IFT** template — interfacility transfer: sending/receiving providers, reason for transfer, care during transport, records and lines/devices accompanying patient
n. **CUSTOM** — agency-defined section order stored in the profile

The clinical summary statement remains an optional labeled opening paragraph compatible with any format above.

---

## New Section 4A. Photo Plus Dictation Intake Workflow

Add a first-class intake mode combining images and voice/verbal transcription, designed for use in the truck, at the hospital, or hours later.

Accepted photo inputs, each with its own transcription-and-verify handler:

a. Monitor screen (vitals, trends, 12-lead)
b. ePCR screen photos (vitals, flowchart, assessments, demographics)
c. Medication vials/packaging (name, concentration, lot if visible; dose given still comes from provider)
d. Facility paperwork (med lists, facesheets, transfer forms, POLST/DNR)
e. Scene photos where agency policy permits (mechanism, pill bottles, living conditions relevant to disposition)
f. Handwritten field notes or glove notes

**Photo handling rules:** transcribe exactly what is visible, present the transcription back for verification before use, never infer values from blur or partial visibility (mark [ILLEGIBLE] instead), and flag any conflict between photo content and dictated content as a discrepancy requiring resolution. Photos supplement dictation; they never substitute for provider confirmation.

**HIPAA reminder:** photographs containing individually identifiable health information must not be uploaded without redaction. Crop or cover patient names, dates of birth, medical record numbers, faces, and other identifiers before photographing. Camera metadata may embed location data that itself constitutes PHI.

---

## New Section 4B. Suggested Verbal Report Format for Dictation

Provide this dictation skeleton in `docs/` as a printable pocket card and in-app reference. It is a prompt order, not a rigid script; the assistant accepts it in any order and in fragments. The goal is that a provider talking through this list once produces enough raw material for a complete narrative in any target format.

1. **CALL FRAME:** unit, dispatch complaint, response mode, scene type, other agencies on scene and their role, any delays and why.
2. **ARRIVAL PICTURE:** where the patient was found, position, first impression, who was present, scene observations that shaped decisions.
3. **PATIENT:** age, sex, weight if estimated, baseline status if known.
4. **STORY:** chief complaint in patient's words, onset, duration, mechanism, what makes it better or worse, what happened before EMS arrived, who gave the history and how reliable.
5. **PERTINENT NEGATIVES:** what the patient specifically denied.
6. **EXAM HIGHLIGHTS:** only findings that drove decisions or aren't going in the Assessment tab.
7. **NUMBERS:** vitals if not on monitor upload, trends, anything abnormal and your read on why.
8. **THINKING:** working diagnosis, what else you considered, what ruled the others down, protocol used.
9. **DOING:** each treatment and why, anything withheld and why, patient response.
10. **MOVING:** transport decision and destination rationale, how the patient was moved, position and why, condition on arrival.
11. **HANDOFF:** who received report, what was transferred with the patient, belongings.
12. **EXCEPTIONS:** anything unusual, refusals of specific interventions, delays, equipment issues, anything you'd want a reviewer to understand.

---

## New Section 4C. Asynchronous and Delayed Recall Support

Busy providers document what they can when they can. Add these behaviors:

a. **Fragment accumulation:** accept partial input across multiple messages over hours. The assistant maintains a running structured worksheet for the call, tracks what's captured and what's missing, and never asks for anything already provided.

b. **Resume-anywhere:** on return, open with a one-line status ("Have scene, story, and vitals photo; still need thinking, doing, and handoff") rather than restarting the interview.

c. **Memory-jogging interview for delayed documentation:** when the provider indicates time has passed, switch from open-ended prompts to targeted recall questions built from what IS known, because recognition beats free recall hours later. Examples of technique: anchor to sequence ("What happened right after you got the first 12-lead?"), anchor to people ("What did the fire crew do while you were getting access?"), anchor to decisions ("You went emergent to the cath-capable facility; what tipped that decision?"), anchor to the senses ("What did you notice when you first walked in the door?"), and anchor to exceptions ("Anything about this call that didn't go the usual way?").

d. **Gap surfacing by call type:** run the applicable call-type flag checklist against accumulated fragments and ask only about unaddressed flags (e.g., for a fall: anticoagulants, LOC, SMR decision, NAT consideration).

e. **Honest gaps:** if the provider genuinely cannot recall a detail, the narrative omits it or marks it [VERIFY]; the assistant never fills memory gaps with plausible content. Recall prompts uncover memories, they do not suggest answers.

f. **Timestamp honesty:** if documentation occurs significantly after the call and the agency requires it, support a late-entry notation per agency profile.

---

## Addition to Section 6. Acceptance Criteria

Add: each new format template produces a compliant sample narrative from the shared test scenario; the dictation pocket card renders in `docs/`; and a simulated fragmented-input test (three sessions, out of order, with one photo) produces a complete narrative with correct [VERIFY] tagging and no invented content.
