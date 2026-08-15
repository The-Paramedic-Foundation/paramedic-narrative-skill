CONSULT THIS FILE WHEN: handoff prep, IMIST-AMBO, prearrival note, transfer of care, retrospective handoff example.
DO NOT CONSULT OTHERWISE.

## IMIST-AMBO elements

IMIST-AMBO is a validated structured handoff framework developed specifically for
paramedicine-to-hospital transfer of care. It is the recommended structure for verbal
reports and the documentation standard for what the handoff report contained.

- **I -- Identification**: Age, sex, and weight if clinically relevant (pediatric or
  weight-based medication dosing). No patient name (PHI rule) -- use "John Doe" or
  "Jane Doe" only if a placeholder reference is needed.
- **M -- Mechanism/Medical complaint**: Mechanism of injury for trauma (including
  kinematics and energy transfer); chief complaint and onset for medical.
- **I -- Injuries/Information**: Injuries identified for trauma, listed anatomically;
  relevant clinical information for medical (pertinent positives and negatives,
  clinical findings that drove assessment).
- **S -- Signs**: Vital signs and level of consciousness at initial contact and trend
  during the encounter. GCS components for altered mental status. RASS if relevant.
- **T -- Treatment and trends**: Interventions performed chronologically, patient
  response to each, and trend in condition. This is the core clinical reasoning
  section of the handoff. Include interventions delivered by another agency's provider
  or before this crew assumed responsibility, identified as such.
- **A -- Allergies**: Known allergies and reaction type.
- **M -- Medications**: Current medications relevant to the presenting problem. MAT,
  anticoagulants, antihypertensives, insulin, and psychotropic medications are the
  categories most likely to affect receiving provider decision-making.
- **B -- Background history**: Pertinent past medical and surgical history.
- **O -- Other information**: Anything not captured above that the receiving provider
  needs: social context relevant to disposition, patient preferences or advance
  directives, family present and their role, forensic considerations, follow-up
  already arranged.

## Concurrent handoff prep (during a call)

Fragment accumulation is not limited to after the call. A provider may feed fragments
during transport -- dictation between interventions, a monitor photo, a medication
given. The running worksheet builds the same way.

Concurrent-use guardrails (never solicit input mid-call, never suggest assessment,
treatment, or destination, no patient name or date of birth) are in ALWAYS-BLOCK.md
and are not restated here.

**Handoff prep command.** At any point, the provider may say "handoff prep," "give me
the handoff," or "IMIST-AMBO now." Assemble a spoken-style IMIST-AMBO report, using
the elements defined above, from the facts collected so far. Format for speech: short
declarative lines a provider can read or glance at in under a minute. Elements not yet
collected are listed at the end as "not yet collected" -- one line, no padding. Never
fill a missing element with a plausible value.

**Prearrival notification note.** On request ("notification prep," "prearrival note,"
or the platform name, e.g., "Pulsara note"), produce a compact block matched to the
fields of prearrival notification platforms:

- **Patient type**: the provider's stated working impression, mapped to the platform's
  category list when the provider has named one (e.g., STEMI, stroke, sepsis, trauma,
  cardiac arrest, obstetrics, behavioral health, toxicology/overdose, general). Never
  assign a category the provider has not stated; if unstated, write "per your
  selection."
- **Chief complaint**: one line, patient's words where provided.
- **Narrative/Notes**: a brief copy-paste note of a few sentences: age and sex,
  presentation, key findings, latest vitals as provided (many platforms auto-extract
  vitals and demographics from this field), treatments and response, and ETA if
  provided.
- **Destination**: as stated by the provider.

Identifiers are entered directly into the notification platform by the provider and
never pass through the AI session.

**Provider verification.** The provider verifies every element before speaking it to a
receiving clinician. The assembled report is a prompt sheet, not an authority.

**Continuity.** After the handoff, the same worksheet feeds the narrative. Document the
handoff actually given -- who received it, condition at transfer, items transferred --
in the Plan section as usual.

## Retrospective Handoff Example (Training Stimulus)

Because the chart is written after transfer of care, every completed draft can close
with a model of what a structured handoff for this call would sound like. This is a
rehearsal aid: providers who see a well-formed IMIST-AMBO built from their own call
data internalize the structure for the next live handoff.

**When it appears:** appended after the standing provider review disclaimer on every
completed narrative draft, unless the agency configuration sets it OFF or the provider
says "skip the handoff example." A provider may also request it alone: "show me the
handoff example."

**Construction rules:**

1. Built only from information the provider supplied for this call. Elements the
   provider did not supply appear as [VERIFY], exactly as in the narrative. Never
   invent a value to make the example complete.
2. Spoken-style, concise, in the IMIST-AMBO order above -- the length of a real
   transfer-of-care report, not a second narrative.
3. It models structure; it does not critique. Never characterize the handoff the
   provider actually gave as deficient. This is a training stimulus, not a performance
   review.
4. For trauma patients, note when the ATLS 11th edition handoff standard (below) adds
   elements to the standard IMIST-AMBO sequence.

**Required label.** The block always begins with the following, verbatim, using two
hyphens ("--") as the separator -- not an em dash:

> **RETROSPECTIVE HANDOFF EXAMPLE -- TRAINING USE ONLY.** This is a model of a
> structured IMIST-AMBO handoff built from the information you provided. It is not
> part of the PCR narrative. Do not paste it into the ePCR.

## Transfer of Care (documentation standard)

The transfer of care section in the Plan must include:
- Identity of the receiving provider (name and credential/role, or "receiving RN" if
  name not obtained)
- Location of transfer (unit, bay, room number if applicable)
- Method of report (verbal, written, phone patch)
- Condition of patient at time of transfer (brief, not a full re-assessment)
- Any items transferred with the patient (medications, belongings, oxygen, equipment)
- Any items given to law enforcement or other agencies (forensic cases)
- Care delivered by another agency's provider or before this crew assumed
  responsibility, where the receiving team needs it. The receiving clinician needs to
  know what the patient received, not which agency will chart it.

Do not leave the transfer of care implied. "Report given to ED staff" is insufficient.
"Verbal report given to receiving RN [name if obtained] in ED bay [number if known];
patient transferred to ED stretcher in [position] with IV intact" is the standard.

**Trauma handoff -- ATLS standard**

For trauma patients transferred to a trauma center or emergency department, the
handoff should meet the standard articulated in the Advanced Trauma Life Support
(ATLS) program, 11th edition. The ATLS trauma handoff standard emphasizes: mechanism
and kinematics communicated with precision sufficient for the receiving team to
reconstruct the injury environment, prehospital vital sign trend (not just arrival
values), interventions and response documented in sequence, and identification of any
clinical concern the receiving team should evaluate that was not fully assessed in the
prehospital setting.

The narrative documents that a structured trauma handoff was performed and captures
any elements of clinical significance that the structured report conveyed -- in
particular, mechanism detail, vital sign trajectory, and any deterioration or
unexpected response to treatment that the receiving team must know.
