# Paramedic-Narrative Skill

**AI-assisted PCR narrative documentation for paramedics and EMTs**

Published by [The Paramedic Foundation](https://paramedicfoundation.org)
Licensed under [CC BY 4.0](LICENSE.md) · Version 1.0.0

---

## Overview

**Paramedic-Narrative** is an AI skill for patient care report (PCR) narrative
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

## What is in this repository

If you have never used GitHub before, this page may look confusing. Here is what
everything is:

```
paramedic-narrative-skill/          ← the repository (this whole page)
├── README.md                       ← this file -- start here
├── ETHICS.md                       ← ethical framework -- read before use
├── LICENSE.md                      ← CC BY 4.0 license terms
├── system-prompt.md                ← the tool instructions for ChatGPT, Gemini,
│                                     or any other AI platform
├── paramedic-narrative.skill       ← the install file for Claude specifically
├── agency-config-template.md       ← standardized configuration template for
│                                     agencies and medical directors to complete
├── provider-profile-template.md    ← personal provider profile template --
│                                     one per provider, never shared
└── paramedic-narrative/            ← folder containing the source files
    ├── SKILL.md                    ← full clinical instructions (human-readable)
    └── references/
        └── documentation-standards-primer.md  ← detailed documentation
                                                  standards reference
```

**You only need one or two of these depending on who you are:**
- **Line provider using Claude**: download `paramedic-narrative.skill`
- **Line provider using ChatGPT or Gemini**: open `system-prompt.md` and copy its contents
- **New provider setting up their profile**: open `provider-profile-template.md`
  (or say "build my provider profile" to the skill and it will guide you)
- **Agency administrator or medical director**: open `agency-config-template.md`
  (or say "set up agency configuration" to the skill and it will guide you)
- **Read the full clinical standards**: open `paramedic-narrative/SKILL.md`
- **Read the ethical framework**: open `ETHICS.md`

---

## Start here if you are new to all of this

**You do not need to understand GitHub to use this tool.** GitHub is just where the
files are stored so anyone can find and download them for free. You only need to
visit this page once to get set up. After that, you use the tool entirely inside
Claude, ChatGPT, Gemini, or whatever AI platform you already use.

Here is the simplest possible path to get started:

**If you use Claude (claude.ai):**

1. Go to the [Releases page](../../releases/latest) on this site. Click
   `paramedic-narrative.skill` to download it. It will land in your Downloads folder.
2. Go to [claude.ai](https://claude.ai) and sign in.
3. Click **Projects** in the left sidebar, then **New Project**. Give it a short,
   recognizable name -- something like **PCR Narratives** or **My Documentation
   Assistant**. You will come back to this Project every time you document a call,
   so name it something you will recognize instantly.
4. Inside the Project, click the settings gear icon, find the **Skills** section,
   click **Upload Skill**, and select the `paramedic-narrative.skill` file you
   downloaded.
5. That is it. Start a new conversation inside that Project whenever you need to
   document a call.

**If you use ChatGPT:**

1. On this page, click the file called `system-prompt.md`.
2. Click the copy icon (two overlapping squares) in the top right of the file.
   This copies all the text.
3. In ChatGPT, go to **Explore GPTs > Create > Configure** and paste the copied
   text into the **Instructions** field.
4. Give it a recognizable name -- something like **Paramedic Narratives** or
   **PCR Assistant** -- so you can find it quickly from your ChatGPT home screen.
5. Click **Save**. Use that Custom GPT for every documentation session.

**If you use Google Gemini:**

1. Copy the contents of `system-prompt.md` as described above.
2. In Gemini, go to **Gems > New Gem**.
3. Paste the copied text into the instructions field.
4. Name it something recognizable -- **PCR Narratives** or **Paramedic Documentation**.
5. Save. Use that Gem for every documentation session.

**If none of that makes sense yet:** go to
[paramedicfoundation.org/resources/ai-documentation](https://paramedicfoundation.org/resources/ai-documentation/)
for plain-language instructions.

---

## Using this tool on your phone or without a work computer

**Paramedic-Narrative works fully on a phone.** Claude, ChatGPT, and Gemini all
have free mobile apps for iOS and Android and all work in a phone browser without
an app. Once the tool is set up on your phone, you can use it anywhere.

**Important policy notice:** The Paramedic Foundation does not condone, encourage,
or authorize the violation of any agency policy, jurisdictional regulation, employer
requirement, or regulatory prohibition on the use of AI tools in clinical settings.
Providers are solely responsible for knowing and complying with all applicable
policies before using this or any AI tool. If your agency, medical director, or
jurisdiction prohibits AI-assisted documentation tools, do not use this tool in
that context. If you are unsure whether your use is permitted, ask your supervisor
or medical director before proceeding.

**Describing your call -- voice input:**

You do not have to type anything. Every AI platform has a microphone button you
can tap to speak your call description out loud -- exactly the way physicians have
used transcription services for decades. Tap the microphone, describe the call the
way you would tell it to a colleague, and the AI will work from what you said. This
is often faster and more natural than typing, especially at the end of a shift.

**Adding clinical data -- camera input:**

You can take a photo and add it to the conversation using the camera button in the
AI app. This works well for:

- Vital signs printouts from your monitor
- 12-lead ECG strips
- Medication lists or medication administration records
- Discharge summaries from a transferring facility
- Printed protocol or procedure reference cards
- Handwritten run sheet notes

**PHI warning -- read this before using the camera:**
Before photographing anything, check that the image does not contain the patient's
name, date of birth, address, medical record number, Social Security number, or any
other information that identifies a specific person. Crop or cover those fields if
present. Camera images also contain hidden metadata including GPS coordinates that
may itself constitute PHI -- be aware of where you are when you take clinical photos.
The Paramedic Foundation is not responsible for privacy breaches resulting from
provider conduct. See Section 6 of [ETHICS.md](ETHICS.md) for the full standard.

**Copying a draft to your ePCR:**

Once you have reviewed and approved the narrative draft:
1. Select all the narrative text and copy it.
2. Paste it directly into your ePCR platform -- most platforms (ESO, ImageTrend,
   Zoll, and others) have mobile apps where you can paste narrative text.

**Email workaround for constrained work environments:**

If you complete documentation on a personal device and need to transfer it to a
work computer:
1. Review and fully approve the narrative on your phone.
2. Copy the narrative text and paste it into an email to your work address.
3. Open the email on your work computer and paste the narrative into your ePCR.

If you use this workflow, do not include any patient identifiers in the AI session.
Use a case number, initials, or generic descriptors ("the patient," "a 68-year-old
female") rather than names, dates of birth, or other direct identifiers. You are
responsible for ensuring this workflow complies with your agency's privacy and
data handling policies.

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

### For individual providers

This skill works out of the box using universal paramedicine documentation standards.
If your agency has completed an agency configuration file (see below), download it
from wherever your agency hosts it and upload it to your Claude Project alongside
the skill. For ChatGPT or Gemini, paste its contents below the system prompt.

If your agency has not yet created a configuration file, you can provide basic
context at the start of any session:

> "I work for [Agency] in [State]. We use [PCR platform]. Our protocols are
> [protocol system name]. My medical director is [name]."

The skill will apply that context for the session.

### For agencies and medical directors

The repository includes a standardized **agency configuration template** that medical
directors and agency administrators can complete once and distribute to all providers.
When every provider uses the same configuration file, every narrative produced in
your system reflects your protocols, your ePCR platform, your documentation standard,
and your medical director's clinical expectations automatically.

**The template file is:** `agency-config-template.md`

It covers:
- Agency identity and service area context
- Medical director endorsement and scope of authorization
- ePCR platform and narrative field specifications
- Documentation standard and minimum narrative requirements
- Protocol system name, version, and CPG sources adopted by medical director
- Specific protocol titles for common call types
- Controlled substance policy including witness, waste, and reconciliation requirements
- Optional prompt settings -- turn specific skill prompts on, off, or required
- Transfer of care standards and receiving facility list
- Alternate destination authorization
- Privacy and data handling policy
- Version history for configuration updates

**How to set it up:**

1. Download `agency-config-template.md` from this repository
2. Open it in any text editor (Notepad, TextEdit, Word set to plain text)
3. Fill in each section -- incomplete sections are fine, the skill applies
   universal standards for anything left blank
4. Have your medical director review and complete Section 2 (endorsement)
5. Save the completed file as `agency-config.md`
6. Post it somewhere all your providers can download it -- your agency intranet,
   shared drive, ePCR document library, or a protected page on your website
7. Tell providers to download it and upload it to their Claude Project, or paste
   its contents below the system prompt in ChatGPT or Gemini
8. When your protocols or policies change, update the file, increment the version
   number in Section 11, and notify providers to download the new version

**Contact The Paramedic Foundation** if you need assistance configuring the skill
for your agency or would like consultation on AI documentation governance:
info@paramedicfoundation.org

---

## Setting Up Your Provider Profile

Your provider profile is a personal file that tells the skill who you are, which
agencies you work for, which roles you operate in, and any standing documentation
preferences. You create it once and it is active for every session without having
to re-enter your information.

**To build it:** say "I want to set up my provider profile" and the skill will
guide you through a short conversation and produce the file automatically.

Alternatively, download `provider-profile-template.md` from this repository,
fill it in, and save it as `provider-profile.md`.

**To use it:** upload `provider-profile.md` to your Claude Project alongside the
skill. For ChatGPT or Gemini, paste its contents below the system prompt.

---

## Working for Multiple Agencies

If you work for more than one agency, upload all your agency configuration files
to your Claude Project at once. The skill detects all loaded configurations and
knows which agencies are available to you.

**At the start of a session**, say which agency you are working for:
> "I'm working an emergency shift for [Agency Name] today."

**To switch agencies mid-session:**
> "Switch to [agency short name]" or "I'm working for [Agency B] today."

The skill confirms the switch, preserves your provider profile and preferences
completely, and applies the new agency's protocols and documentation standards.

---

## Role Contexts

If you work in more than one clinical role, tell the skill which role is active
at the start of each session. This changes which documentation framework,
prompts, and disposition options apply.

**Available roles:**

- **Emergency paramedic** -- 911 response. Full SOAP with all scoring tools,
  forensic standard, IMIST-AMBO handoff, ATLS trauma standard. Care pathway
  documentation for low-acuity calls and refusals.

- **Rescue paramedic** -- Technical or special operations. Adds scene safety
  and hazard documentation, rescue mechanism, extrication detail, specialized
  equipment, and multi-agency role attribution.

- **Community paramedic** -- CP/MIH visits. Shifts to longitudinal care
  framework: visit reason, functional status, medication adherence, resource
  connections, care plan. Alternative disposition is the primary outcome.
  Barriers to care always active.

- **Hospital paramedic** -- CCT, interfacility transport, in-hospital response,
  or procedure support. Emphasizes transport indication and medical necessity,
  pre-transport stability, monitoring and interventions en route, and structured
  handoff to receiving team.

**To activate a role:**
> "I'm doing community paramedicine today."
> "This is a CCT run."
> "I'm on rescue."
> "Emergency shift."

**To switch roles mid-session:**
> "Switch to emergency mode for this call."

The skill applies the emergency framework for that narrative and returns to
your prior role context when complete.

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

> Nudell, N. G. (2026). *paramedic-narrative-skill: AI-assisted PCR narrative*
> *documentation for paramedics and EMTs* (Version 1.0.0) [Software]. The Paramedic
> Foundation. https://github.com/The-Paramedic-Foundation/paramedic-narrative-skill

---

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE.md)

You may share and adapt this material for any purpose, including commercial use,
provided you give appropriate credit to The Paramedic Foundation and link to
paramedicfoundation.org.

---

**The Paramedic Foundation** · 23 W Central Entrance PMB 321 · Duluth, MN 55811
paramedicfoundation.org · info@paramedicfoundation.org · EIN 46-3271401 · 501(c)(3)
