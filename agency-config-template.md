# Paramedic-Narrative Skill — Agency Configuration Template

**The Paramedic Foundation**
paramedicfoundation.org · Version 1.4.0

---

## Instructions for Agency Administrators and Medical Directors

This file is the standardized configuration template for the Paramedic-Narrative
documentation skill. When completed, it tells the skill exactly how your agency
operates so that every narrative produced by a provider in your system reflects
your protocols, your ePCR platform, your documentation standard, and your
medical director's clinical expectations.

**Who completes this file:**
This file should be completed by the agency medical director, EMS director, or a
designated documentation coordinator in consultation with the medical director.
It is not intended to be completed by individual providers.

**How providers use it:**
Once completed, post this file somewhere all providers can access it -- your agency
intranet, shared drive, ePCR document library, or a protected page on your agency
website. Providers download it and upload it to their Claude Project alongside the
skill, or paste its contents below the system prompt in ChatGPT or Gemini. Every
provider using the same configuration file will document to the same standard
automatically.

**How to edit this file:**
Open it in any text editor (Notepad on Windows, TextEdit on Mac, or any word
processor set to plain text). Fill in each field between the brackets. Delete the
bracket and placeholder text and replace with your agency's information. Leave any
field blank if it does not apply to your agency -- the skill will apply universal
standards for any unconfigured field.

**Version control:**
When you update this file, increment the Configuration Version field below and
note what changed. Notify providers to download the updated version.

---

## Section 1: Agency Identity

**Agency Name:**
[Full legal name of the agency]

**Agency Type:**
[e.g., County EMS, Fire-based EMS, Hospital-based, Private, Air Medical, Community
Paramedicine Program, Multi-agency regional system]

**Service Area:**
[Geographic description -- e.g., rural, frontier, urban, suburban, mixed. Include
county/region name.]

**State:**
[Two-letter state code]

**Medical Director:**
[Full name, credential, and contact for documentation questions -- e.g.,
Jane Smith, MD, FAEMS -- jsmith@agencyemail.org]

**Configuration Completed By:**
[Name and title of person who completed this file]

**Date Completed:**
[MM/DD/YYYY]

**Configuration Version:**
[e.g., 1.0 -- initial release]

**Hosted at:**
[URL or network path where providers can download the current version of this file]

---

## Section 2: Medical Director Endorsement

By completing and distributing this configuration file, the medical director affirms
that:

1. The protocols, CPGs, and documentation standards referenced in this file have
   been reviewed and are approved for use by providers under this medical director's
   authority.
2. The use of the Paramedic-Narrative skill as configured here is consistent with
   agency policy and applicable regulatory requirements.
3. This configuration has been reviewed against the ethical framework published in
   ETHICS.md and the medical director affirms that use of the skill within these
   parameters is appropriate.
4. Providers remain fully responsible for every submitted patient care record
   regardless of AI assistance.

**Medical Director Name:**
[Full name and credential]

**Medical Director Signature / Digital Acknowledgment:**
[Typed name serves as acknowledgment -- e.g., "Jane Smith, MD -- reviewed and
approved MM/DD/YYYY"]

**Scope of Authorization:**
[Describe which providers and which use cases this endorsement covers -- e.g.,
"All ALS and BLS providers employed by or contracted with [Agency Name] for
routine documentation of 911 responses, community paramedicine visits, and
interfacility transfers."]

**Restrictions or Conditions:**
[Any conditions on use -- e.g., "Not authorized for use on pediatric calls pending
protocol review" or "Providers must complete the agency AI documentation orientation
before use." Leave blank if none.]

---

## Section 3: ePCR Platform

**Primary ePCR Platform:**
[e.g., ESO, ImageTrend Elite, Zoll RescueNet, EPCR, FirstWatch, Traumasoft, other]

**Platform Version or Module:**
[If known -- e.g., ESO v6, ImageTrend Elite 8.x]

**Narrative Field Name in Platform:**
[What the narrative field is called in your platform -- e.g., "Provider Narrative,"
"Clinical Narrative," "Run Narrative." This helps providers know where to paste
the draft.]

**Structured Fields That Do NOT Need Narrative Coverage:**
[List any fields your platform captures in structured form that providers sometimes
redundantly document in the narrative -- e.g., "Vitals are fully structured in ESO
and do not need to be restated in the narrative." The skill already follows this
principle by default; list any platform-specific fields you want to emphasize.]

**Mobile App Available:**
[Yes / No / Limited -- and platform name if different from desktop]

---

## Section 4: Documentation Standard

**Agency Documentation Policy Reference:**
[Title and date of your agency's documentation policy or standard operating
procedure -- e.g., "ABC EMS Documentation SOP v3.2, revised January 2025"]

**Minimum Narrative Requirements:**
[Paste or summarize your agency's minimum narrative requirements here. Be specific.
Example: "All ALS narratives must document: chief complaint in patient's own words,
pertinent positives and negatives, working impression with differential, all
treatments with indication and response, and transfer of care with receiving
provider name."]

**Narrative Format Required:**
[Declare the narrative format your agency requires. The skill natively supports:
SOAP (default), SOAPE, SOAPIER, CHART, CHARTE, DCHART-E, CHRONOLOGICAL,
HEAD-TO-TOE, DRAATT, AT CHART, FACT, plus dedicated REFUSAL/NON-TRANSPORT and
IFT templates and a CUSTOM agency-defined section order. Example: "DCHART-E
required for all 911 responses; IFT template for interfacility transfers."
Providers may override per call when clinically appropriate unless you state
otherwise here.]

**Custom Format Definition (only if CUSTOM declared above):**
[List your section names in order and what belongs in each.]

**Refusal / Non-Transport Protocol Reference:**
[The agency protocol governing refusals and non-transports, cited by name or
number, so refusal narratives reference it correctly -- e.g., "Protocol 12 --
Refusal of Care."]

**Special Documentation Requirements:**
[Any agency-specific requirements not covered above -- e.g., mandatory supervisor
notification documentation, quality improvement flags, specific language required
for billing purposes, mandatory scene time documentation, etc.]

**Billing and Medical Necessity Notes:**
[Any specific language or documentation elements your billing department requires
for clean claims -- e.g., "All non-emergency transports must include documentation
of why the patient could not be transported by other means."]

---

## Section 5: Protocols and Clinical Practice Guidelines

This section tells the skill which protocols and CPGs govern clinical decisions at
your agency. When a provider references a protocol in a narrative, the skill will
use the name and format you specify here rather than a generic reference.

**Protocol System Name:**
[e.g., "Colorado SEMSA Region 1 Protocols," "ABC County EMS Medical Protocols,"
"[State] BLS/ALS Protocols"]

**Protocol Version and Date:**
[e.g., "Version 4.2, effective March 2025"]

**Protocol Reference Format:**
[How protocols are cited in your narratives -- e.g., "Protocol 3.14," "ALS Protocol
-- Chest Pain," "Standing Order 7B." Provide an example of how a protocol citation
should appear in a narrative.]

**Primary CPG Sources Adopted by Medical Director:**
[List the national CPG sources your medical director has formally adopted or
references -- check all that apply and add others:]

- [ ] NAEMSP (National Association of EMS Physicians) position statements and CPGs
- [ ] NASEMSO (National Association of State EMS Officials) model protocols
- [ ] ACEP (American College of Emergency Physicians) clinical policies
- [ ] AHA/ACC (cardiac resuscitation and STEMI guidelines)
- [ ] ATLS 11th edition (trauma handoff and management standards)
- [ ] SALT Triage (mass casualty triage standard)
- [ ] ACS Field Triage Decision Scheme (trauma destination criteria)
- [ ] Other: [specify]

**Specific Protocol Titles for Common Call Types:**
[Fill in the protocol name used at your agency for each. Leave blank if standard
national CPG applies or if not in your scope.]

- Chest pain / possible ACS: [protocol name]
- Stroke / TIA: [protocol name]
- Cardiac arrest: [protocol name]
- Airway management / RSI: [protocol name]
- Trauma / major trauma: [protocol name]
- Pediatric emergencies: [protocol name]
- Behavioral health / psychiatric: [protocol name]
- Opioid overdose / naloxone: [protocol name]
- Pain management: [protocol name]
- Seizure: [protocol name]
- Diabetic emergency: [protocol name]
- Obstetric emergency: [protocol name]
- Community paramedicine: [protocol name or program name]
- Other call types specific to your agency: [list]

---

## Section 6: Controlled Substance Policy

**Controlled Substance Kit Type:**
[e.g., sealed tamper-evident kit, agency safe, locked compartment. Describe the
standard source from which controlled substances are drawn.]

**Witness Requirement:**
[Who is required to witness draw, administration, and waste -- e.g., "Partner
paramedic required for all controlled substance draws and waste. Receiving RN
acceptable as waste witness at destination."]

**Waste Policy:**
[How waste is handled -- e.g., "Waste into sharps container with partner witness.
Document quantity wasted and witness name and credential in narrative."]

**Partial Dose / Remainder Policy:**
[What happens to unused medication -- e.g., "Unused controlled substances returned
to agency safe at end of shift. Document quantity returned and receiving supervisor."]

**Reconciliation Requirement:**
[When and how controlled substance counts are reconciled -- e.g., "Kit reconciled
at start and end of each shift with supervisor. Document supervisor name and time
in narrative when reconciliation is relevant to the call."]

**Controlled Substance Documentation Form:**
[If your agency uses a separate controlled substance form in addition to the PCR,
name it here -- e.g., "DEA-222 companion form required for all Schedule II
administrations."]

**Agency-Specific Controlled Substances in Scope:**
[List the controlled substances your providers carry and may administer, so the
skill can prompt correctly for each:]
- [e.g., Fentanyl -- Schedule II]
- [e.g., Midazolam -- Schedule IV]
- [e.g., Ketamine -- Schedule III]
- [e.g., Morphine -- Schedule II]
- [e.g., Diazepam -- Schedule IV]
- [Add others as applicable]

---

## Section 7: Optional Prompt Settings

This section lets you turn specific skill prompts on or off for your agency. The
skill will still document these elements if the provider mentions them -- these
settings only control whether the skill actively asks about them if the provider
does not bring them up first.

For each item, write **ON** (skill will prompt if not mentioned), **OFF** (skill
will not prompt), or **REQUIRED** (skill will always prompt and flag [VERIFY] if
not addressed).

**Community paramedicine and mobile integrated health documentation:**
[ON / OFF / REQUIRED]

**Crisis response and co-response model documentation:**
[ON / OFF / REQUIRED]

**Care pathway documentation for low-acuity calls and refusals:**
[ON / OFF / REQUIRED]

**Barriers to care prompts:**
[ON / OFF / REQUIRED]

**Recent pregnancy history prompt (women of childbearing age):**
[ON / OFF / REQUIRED]

**Substance use history prompt:**
[ON / OFF / REQUIRED]

**De-escalation documentation:**
[ON / OFF / REQUIRED]

**SALT triage documentation:**
[ON / OFF / REQUIRED -- set OFF if your agency does not respond to MCIs]

**Frailty scoring (CFS) for elderly patients:**
[ON / OFF / REQUIRED]

**Scoring tools prompt (HEART, Cincinnati, CIWA-Ar, etc.):**
[ON / OFF / REQUIRED]

**Retrospective IMIST-AMBO handoff example (training stimulus appended after
each completed draft):**
[ON / OFF -- default ON. Providers may skip it per call either way.]

**Live handoff prep command (on-request IMIST-AMBO assembly during transport):**
[ON / OFF -- default ON. Assembles only facts the provider has already
provided; it never suggests assessment, treatment, or destination. Set OFF if
your agency prohibits AI tool interaction during patient care.]

**Notes on prompt settings:**
[Any additional context for providers about why specific prompts are set the way
they are -- e.g., "Barriers to care is REQUIRED because our QI program tracks
access issues for grant reporting."]

---

## Section 8: Transfer of Care Standards

**Preferred Handoff Framework:**
[e.g., "IMIST-AMBO required for all ALS transfers" or "Verbal SBAR acceptable
for BLS transfers, IMIST-AMBO required for ALS"]

**Primary Receiving Facilities:**
[List the hospitals and specialty centers your agency typically transports to,
so the skill can reference them correctly in destination rationale:]
- [Facility name, level, and specialty if applicable -- e.g., "St. Mary's Medical
  Center -- Level II Trauma Center, STEMI receiving, stroke center"]
- [Add as many as needed]

**Trauma Center Designation:**
[Which trauma center level(s) are available in your service area and at what
transport interval -- e.g., "Level I trauma center at 45 minutes, Level III at
12 minutes"]

**Stroke Center:**
[Primary stroke center name and transport interval]

**Cardiac Catheterization:**
[STEMI receiving center name and transport interval]

**Psychiatric and Crisis Receiving:**
[Crisis stabilization unit, psychiatric emergency service, or behavioral health
urgent care available in your service area -- name and availability hours]

**Alternate Destination Authorization:**
[Which alternate destinations are authorized under your protocols -- e.g., urgent
care, primary care, detox facility, crisis stabilization unit -- and under what
conditions. This is critical for the skill's care pathway documentation.]

---

## Section 9: Service Area Context

**Geographic Characteristics:**
[Describe the service area in terms relevant to documentation -- e.g., "Frontier
county, average transport time to definitive care 45-90 minutes. Helicopter
available weather permitting. No urgent care within county."]

**Population Characteristics:**
[Any population factors relevant to documentation standards -- e.g., "Significant
agricultural workforce, high proportion of uninsured patients, large elderly
population in assisted living facilities, significant non-English speaking
population (primary languages: Spanish, Somali)."]

**Common Call Types:**
[List the call types that make up the majority of your volume, so the skill can
prioritize relevant prompts -- e.g., "High volume: behavioral health, falls in
elderly, diabetic emergencies, chest pain. Seasonal: agricultural injuries
(summer), hypothermia (winter)."]

**Community Paramedicine Program:**
[If your agency operates a CP or MIH program, describe it briefly -- program name,
scope, referral sources, and any documentation requirements specific to the program.]

**Mutual Aid Agencies:**
[Primary mutual aid partners, if relevant to documentation -- e.g., "Frequent
co-response with County Sheriff's Office crisis intervention team and Mobile
Crisis Unit operated by [behavioral health agency]."]

---

## Section 10: Privacy and Data Handling

**Agency AI Use Policy:**
[Reference your agency's policy on AI tool use, if one exists -- title, version,
and date. If no policy exists yet, note that here.]

**Approved AI Platforms:**
[Which AI platforms are approved for use with this skill under agency policy --
e.g., "Claude (Anthropic) approved. ChatGPT approved for providers without Claude
access. All use must be on personal devices with personal accounts." Or: "Agency
has not yet issued approval -- individual use is at provider discretion pending
policy development."]

**PHI Handling Instructions:**
[Any agency-specific instructions beyond the default PHI standard in ETHICS.md --
e.g., "Providers must use case number only (not patient name) in all AI sessions.
Use of patient name in any AI tool is a policy violation subject to disciplinary
action."]

**Data Retention Notice:**
[If your agency has reviewed the data retention practices of approved AI platforms
and has specific guidance for providers, note it here.]

---

## Section 11: Version History

| Version | Date | Changed By | Summary of Changes |
|---------|------|------------|-------------------|
| 1.0 | [date] | [name] | Initial configuration |
| | | | |
| | | | |

---

*This configuration file is specific to [Agency Name] and is intended for use
by authorized providers under the medical direction of [Medical Director Name].*

*Template published by The Paramedic Foundation under CC BY 4.0.*
*paramedicfoundation.org · info@paramedicfoundation.org*

*Cite as: Nudell, N. G. (2026). Paramedic-Narrative skill — agency configuration*
*template (Version 1.4.0) [Software configuration template]. The Paramedic*
*Foundation. https://github.com/The-Paramedic-Foundation/paramedic-narrative-skill*
