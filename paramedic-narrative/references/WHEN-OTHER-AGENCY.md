CONSULT THIS FILE WHEN: another agency present or directing care, facility-origin or interfacility transport, care in progress on arrival, waivered act, medication drawn and not given.
DO NOT CONSULT OTHERWISE.

Care delivered during a single patient encounter is frequently not delivered by a
single crew. First responders, partner agencies, sending facilities, law
enforcement, family, and bystanders all deliver care that the documenting crew
must account for without claiming.

## The attribution boundary

A structured ePCR entry -- a Flowchart line, a medication entry, a procedure
entry -- asserts that this crew performed this act, on this patient, at this
time. In most jurisdictions those entries also feed regulatory and public-health
reporting -- in the United States through NEMSIS and the state EMS data system,
and through equivalent registries elsewhere -- where they become the official
record of the care this agency provided. What goes in a structured field is not
only an internal clinical note; it is a claim about who did what.

A structured field may therefore contain only care this crew performed, after
assuming responsibility for the patient, that actually occurred. Three
categories of clinically significant information fall outside that boundary and
are narrative-only. For them, the narrative is the sole record:

a. Care performed by a provider from another agency, including one directing
   care in this crew's vehicle or during this crew's transport.
b. Care performed before this crew arrived and assumed responsibility -- by
   first responders, a sending facility, another agency, family, or bystanders.
c. Interventions prepared, drawn up, set up, or considered but not performed,
   including alerts, activations, or notifications considered but not called.

## The inversion rule

Where there is no structured entry to reference, "reference, do not duplicate"
would leave the act undocumented entirely. For narrative-only content, write the
operational detail out in full: what was done, by whom, dose and route where
applicable, time or relative sequence where known, and the patient's response.
This is the one place in the standard where the narrative properly carries what
and when as well as why.

Never write "as charted," "as documented in the Flowchart," or any equivalent
phrase for narrative-only content.

If it is unclear whether a given item was entered in a structured field, ask. Do
not assume either way.

## Care directed or performed by another agency's provider

When a patient is in this crew's care or transport and some or all clinical care
was directed or performed by a provider from another agency, the encounter is
documented to the same standard as any other patient. A cross-reference to the
other agency's record ("see the fire department report") is not documentation of
this encounter.

Document:

- Who was directing patient care, by role and agency.
- What this crew did, and under whose direction, where the crew was acting at
  another provider's direction.
- Each intervention the other agency's provider performed, attributed to them by
  role and agency, with the patient's response.
- The documenting provider's own clinical reasoning for the decisions that were
  theirs -- including medical necessity for transport, which remains this
  crew's obligation to establish regardless of who directed clinical care.

Do not characterize the other provider's clinical reasoning. Describe what
occurred and what was observed. Where the other provider stated a reason, quote
or attribute it to them; where they did not, the reasoning is simply not
available and the narrative says nothing about it. Reasoning belongs only to the
clinician who stated it.

### Waivered, variance, and specially authorized acts

Some jurisdictions authorize specific medications or procedures at the agency
level, by waiver, variance, pilot authorization, or equivalent mechanism, and
require those acts to be reported through structured ePCR data. Where two
agencies each hold such an authorization, entering the other agency's
administration into this agency's structured fields causes a single act to be
reported twice, and attributes it to an agency that did not perform it. The rule
is symmetric and does not depend on which jurisdiction's scheme applies:

- If this crew performed the act, it is a structured entry and the narrative
  carries only the reasoning.
- If another agency's provider performed the act, it is narrative-only, in full
  detail, attributed to them.

When the provider mentions a medication or procedure that may be waivered or
specially authorized and the performing agency is unclear, ask who performed it
before drafting. Mark it [VERIFY: performing agency] if the answer is not
available. The agency configuration is the authoritative source for which acts
this applies to locally.

### Scope of this rule

It applies to any encounter where the patient is in this crew's care or
transport. It does not apply to a call where another agency managed the patient
entirely and this crew provided no transport and no hands-on care; that is a
different encounter type and is documented per agency policy.

## Care provided prior to arrival

Care that occurred before this crew arrived and assumed responsibility for the
patient is not this crew's care, and it is not represented as timestamped
structured entries. Clinically significant prior care is still essential to the
record and belongs in the narrative, or in the history section where the format
provides one.

Document:

- What was done, by whom, and when or in what sequence, as reported or
  observed.
- The source of that information: direct observation, verbal report from the
  provider or facility staff, written transfer paperwork, or family.
  Reliability where it is in question.
- The patient's status at the moment this crew assumed responsibility, which is
  the clinical hinge between their care and this crew's care.

Example framing: a patient found in cardiac arrest with resuscitation already in
progress is documented with the arrest history, defibrillations, medications,
and approximate duration of resuscitation before arrival, and whether a pulse
was present when this crew assumed care -- summarized in the narrative rather
than recreated as individual structured entries.

This does not change how the patient's medical history, home medications, or
long-standing prescribed therapies are documented. Those belong in the
History/Medications structured fields as they always have. The distinction is
between the patient's standing medical record and acute interventions performed
by someone else during this episode of care.

When ABC/LOC status at the moment this crew assumed responsibility differs from
status on scene arrival because of care delivered by others, state both and mark
the transition point.

## Facility paperwork and other agency records

A photograph of a sending facility's paperwork or another agency's record
documents care that someone else provided. Treat its contents as prior-to-arrival
or other-agency care under this attribution boundary, and confirm with the
provider who performed each item before it enters the narrative.

## Interventions prepared or considered but not performed

Structured fields reflect what actually happened. A medication drawn up but
never administered, a procedure prepared for but never attempted, and an alert
or activation considered but never called are not structured entries. A
free-text note attached to a structured entry does not change how that entry is
counted in aggregate reporting.

Document in the narrative:

- What was prepared or considered, and on what clinical basis.
- What changed -- indication resolved, patient declined, contraindication
  identified, transfer of care intervened, medical direction advised
  otherwise.
- The disposition of anything prepared. For a controlled substance drawn and
  not administered, the full waste trail under the Medication Administration
  Standard applies even though nothing was given.

This aligns with the existing standard for withheld interventions: document what
was not done and why, when the omission is clinically meaningful.

## [VERIFY] handling

Attribution gaps are gaps like any other. If it is not established who performed
an intervention, whether it occurred before or after this crew assumed
responsibility, or whether a prepared medication was administered or wasted,
mark it [VERIFY] and surface it in the pre-draft verification list. Never
resolve an attribution question by assuming the documenting crew performed the
act.
