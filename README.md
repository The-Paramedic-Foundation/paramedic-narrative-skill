# paramedic-narrative-skill

**AI-assisted PCR narrative documentation for paramedics and EMTs**

Published by [The Paramedic Foundation](https://paramedicfoundation.org)
Licensed under [CC BY 4.0](LICENSE.md) · Version 1.0.0

---

## Overview

`paramedic-narrative` is an AI skill for patient care report (PCR) narrative
documentation. It is an editorial tool designed for paramedics and EMTs who use AI
language model tools and want a structured, clinically rigorous, non-hallucinating
documentation assistant.

It produces SOAP-format PCR narratives grounded in one principle: **the narrative
explains the WHY. Structured PCR fields capture the WHAT and WHEN.**

The skill does not restate vital signs, medication doses, or exam findings already
captured in your PCR platform. It captures what structured fields cannot: clinical
reasoning, differential rationale, history source and reliability, medication
indication and response, controlled substance audit trails, forensic evidentiary
detail, and transfer-of-care narrative.

It never invents, assumes, or infers clinical detail. If you did not provide it, it
does not appear in the draft. Missing items are flagged [VERIFY].

---

## Critical Limitations -- Read Before Use

**This is an editorial tool only. It must never be used to make clinical decisions.**

Using AI-generated content to inform clinical decisions in paramedicine is unethical,
unsupported by evidence, and may be illegal under applicable professional licensing
and scope-of-practice law. This tool has not been tested or validated for clinical
decision support and is not intended for that purpose.

The Paramedic Foundation makes no warranty regarding the accuracy or completeness of
any output. The provider bears full professional and legal responsibility for every
submitted document.

**PHI warning**: Never photograph or upload patient-identifying information, including
patient faces, license plates, or documents containing names, dates of birth, or other
protected health information (PHI). Camera metadata may also transmit location data
that constitutes PHI. The Paramedic Foundation is not responsible for privacy breaches
resulting from provider conduct.

Read [ETHICS.md](ETHICS.md) before use.

---

## What This Tool Does

- Produces SOAP-format PCR narrative drafts from provider-supplied information
- Captures clinical reasoning, differential rationale, and history source attribution
  that structured fields cannot hold
- Applies an elevated evidentiary standard for forensic and high-acuity calls
- Documents controlled substance audit trail elements the provider supplies
- Flags missing information as [VERIFY] rather than inventing it
- Applies universal paramedicine documentation standards when no agency policy is
  provided

## What This Tool Does Not Do

- Does not make or support clinical decisions of any kind
- Does not access PCR platforms or submit documents
- Does not invent, assume, or infer clinical detail
- Does not reproduce information already in structured fields
- Does not fabricate controlled substance audit trail elements
- Does not provide clinical advice

---

## Installation

### Claude (native skill format)

1. Download `paramedic-narrative.skill` from the
   [Releases](../../releases/latest) page
2. In Claude.ai, open or create a Project
3. Go to Project Settings > Skills > Upload Skill
4. Upload the `.skill` file
5. Optionally upload your agency documentation standard as a Project file
   (see [Configuration](#configuration))

### ChatGPT (Custom GPT)

1. Copy the full contents of `system-prompt.md` from this repository
2. In ChatGPT, go to Explore GPTs > Create > Configure
3. Paste the contents into the Instructions field
4. Optionally paste your agency documentation standard below the pasted instructions
5. Save your Custom GPT

### Google Gemini (Gem)

1. Copy the full contents of `system-prompt.md` from this repository
2. In Gemini, go to Gems > New Gem
3. Paste the contents into the instructions field
4. Optionally paste your agency documentation standard below
5. Save the Gem

### Any Other LLM Platform

`system-prompt.md` is formatted as a plain system prompt compatible with any AI
platform that accepts system-level or custom instructions. Paste it into the
appropriate field for your platform.

---

## Configuration

This skill works out of the box using universal paramedicine documentation standards.
For best results, supply your agency-specific context.

### Option 1: Upload a configuration file (recommended for Claude Projects)

Create a file called `agency-config.md` and upload it to your Claude Project alongside
the skill. Include any relevant fields:

```markdown
## Agency Configuration

PCR Platform: [e.g., ESO, ImageTrend, Zoll RescueNet, EPCR, FirstWatch]

Documentation Standard: [paste your agency's narrative requirements or key points]

Protocol Reference: [state/medical director protocol name or number format used]

Controlled Substance Policy: [agency-specific requirements, if any, beyond the
skill default]

Medical Director: [name, if you want it referenced in transfer-of-care narrative]

Service Area: [rural/urban/suburban, if relevant to transport rationale documentation]
```

### Option 2: Provide context at the start of a session

At the beginning of any session, state: "I work for [Agency] in [State]. We use
[PCR platform]. Our documentation standard requires [key requirements]." The skill
applies that context for the session.

### Option 3: Use the defaults

If no agency configuration is provided, the skill applies universal paramedicine
documentation standards as documented in
`paramedic-narrative/references/documentation-standards-primer.md`.

---

## How to Use It

Begin a session and describe your call. You can provide information in any format:

- A brief verbal summary: "55M, chest pain, 10/10, diaphoretic, pressure-like..."
- A structured list of findings and interventions
- A detailed walkthrough of the encounter

**Do not photograph or upload patient records, vital sign strips with patient
identifiers, or any image containing PHI.** See Section 6 of [ETHICS.md](ETHICS.md).

The skill will identify what additional information is needed for a complete narrative,
ask only for what is missing and narrative-relevant (not for information already
captured in your structured PCR fields), and produce a draft in Clinical Summary /
S / O / A / P format.

Every draft ends with a mandatory provider review disclaimer. Review the draft
carefully, correct any errors, verify all [VERIFY] items, and approve before
submitting.

### Example session

> "Help me write a narrative. 68F, found unresponsive by family, last known well
> approximately 2 hours ago per family at bedside. GCS 8 on arrival. Cincinnati
> positive. BGL 112. Transported priority to Regional Stroke Center."

The skill will ask targeted follow-up questions about ABC/LOC quality, clinical
reasoning, transport rationale, and transfer of care, then produce the draft.

---

## Controlled Substance Documentation

When a call involves controlled substance administration, the skill applies a strict
audit trail standard. It will ask for:

- Medication source and container identifier
- Witness identity and credential
- Amount drawn vs. amount administered
- Waste amount, method, and witness to waste
- Chain of custody for any remainder
- Reconciliation if performed

It will not fabricate any of these elements. Missing audit trail items are always
flagged [VERIFY]. See Section 7.4 of [ETHICS.md](ETHICS.md) for the governing
ethical standard.

---

## Forensic Documentation

When a call involves suspected criminal activity, victimization, or harm, the skill
automatically applies an elevated evidentiary standard:

- Source attribution for every factual statement about who did what to whom
- Verbatim patient and witness quotes where possible
- Observation distinguished from inference throughout
- Law enforcement presence and identifiers documented
- Chain of custody for any items transferred
- Neutral, non-legal-conclusion language throughout

Call types that trigger this standard include: assault, domestic violence, sexual
assault, child or vulnerable adult abuse, suspicious death, gunshot or stab wound,
suspected non-accidental trauma, motor vehicle collision with potential impairment
or fatality, and any scene where law enforcement is investigating.

---

## Multi-Platform Files

| File | Purpose | Platform |
|---|---|---|
| `paramedic-narrative.skill` | Native skill package | Claude |
| `system-prompt.md` | Plain system prompt | ChatGPT, Gemini, any LLM |
| `paramedic-narrative/SKILL.md` | Source instructions | All (human-readable) |
| `paramedic-narrative/references/documentation-standards-primer.md` | Standards reference | Loaded on demand |

All versions contain identical clinical logic. Only the packaging differs.

---

## Ethical Framework

Read [ETHICS.md](ETHICS.md) before clinical use. It covers:

- The governing principle (augmentation, not delegation)
- Disclaimer of warranty and limitation of liability
- Absolute prohibition on clinical decision use
- Privacy and PHI requirements in detail
- Provider ethical commitments
- Equity obligations
- Organizational governance guidance
- Version control and contribution process

This framework is grounded in Nudell, N.G. (2026). Clinical governance in the age
of artificial intelligence: A profession-wide imperative for paramedicine. *Governing
Care.* The Paramedic Foundation / American College of Paramedics.

---

## Version Control

Current version: **1.0.0**

Version history and release notes are maintained in this repository. Check
[Releases](../../releases) for updates. Providers and agencies using this tool in
ongoing documentation workflows should review updates periodically.

Significant updates affecting clinical content, privacy standards, or the ethical
framework will be clearly noted in release notes.

---

## Contributing

Contributions are welcome from providers, agencies, educators, medical directors,
and researchers. See Section 11 of [ETHICS.md](ETHICS.md) for full guidance.

Ways to contribute:

- **Clinical corrections**: Open a GitHub Issue with your proposed correction and
  reasoning
- **Agency configurations**: Share de-identified `agency-config.md` examples for
  specific PCR platforms
- **Platform support**: Configuration guidance for additional AI platforms
- **International adaptations**: Non-US paramedicine frameworks and documentation
  standards
- **Research and evaluation**: Systematic evaluations of tool outputs

All contributions are reviewed by The Paramedic Foundation before incorporation.

---

## Citation

If you use or adapt this skill in research, policy work, or publications:

> The Paramedic Foundation. (2026). *paramedic-narrative-skill: AI-assisted PCR*
> *narrative documentation for paramedics and EMTs* (v1.0.0). CC BY 4.0.
> https://github.com/The-Paramedic-Foundation/paramedic-narrative-skill 

---

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE.md)

You may share and adapt this material for any purpose, including commercial use,
provided you give appropriate credit to The Paramedic Foundation and link to
paramedicfoundation.org.

---

**The Paramedic Foundation** · 23 W Central Entrance PMB 321 · Duluth, MN 55811
paramedicfoundation.org · info@paramedicfoundation.org · EIN 46-3271401 · 501(c)(3)
