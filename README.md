<div align="center">

![Paramedic-Narrative by The Paramedic Foundation](https://raw.githubusercontent.com/The-Paramedic-Foundation/paramedic-narrative-skill/main/assets/pn-header.png)

</div>

<div align="center">

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/Version-2.1.1-blue.svg)](../../releases/latest)
[![Platform](https://img.shields.io/badge/Platform-Claude%20%7C%20ChatGPT%20%7C%20Gemini-teal.svg)](../../releases/latest)
[![Free](https://img.shields.io/badge/Cost-Free-green.svg)](../../releases/latest)

</div>

**AI-assisted PCR narrative documentation for paramedics and EMTs**

Published by [The Paramedic Foundation](https://paramedicfoundation.org)
Licensed under [CC BY 4.0](LICENSE.md) · Version 2.1.1

---

## Overview

**Paramedic-Narrative** is an AI skill for patient care report (PCR) narrative
documentation. It is an editorial tool designed for paramedics and EMTs who use AI
language model tools and want a structured, clinically rigorous, non-hallucinating
documentation assistant.

It produces PCR narratives in your agency's declared format -- SOAP with Clinical
Summary by default, with native support for SOAPE, SOAPIER, CHART, CHARTE,
DCHART-E, CHRONOLOGICAL, HEAD-TO-TOE, DRAATT, AT CHART, FACT, dedicated
REFUSAL/NON-TRANSPORT and IFT templates, and CUSTOM agency-defined section
orders -- all grounded in one principle: **the narrative explains the WHY.
Structured PCR fields capture the WHAT and WHEN.**

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

- Produces PCR narrative drafts from provider-supplied information in your
  agency's declared narrative format (14 formats supported, per-call override)
- Accepts photo plus dictation intake: monitor screens, med vials, facility
  paperwork, and handwritten notes, transcribed exactly and verified -- never
  inferred from blur
- Supports fragmented documentation across sessions and targeted memory-jogging
  recall questions when documenting hours after a call
- Assembles an on-request IMIST-AMBO handoff prep during transport from facts
  already collected, and appends a retrospective IMIST-AMBO training example
  to each completed draft
- Produces an on-request prearrival notification note: a copy-paste block
  matched to notification platform fields (patient type as you stated it,
  chief complaint, brief note with vitals, destination), with no patient
  identifiers
- Captures clinical reasoning, differential rationale, and history source attribution
  that structured fields cannot hold
- Applies an elevated evidentiary standard for forensic and high-acuity calls
- Documents controlled substance audit trail elements the provider supplies
- Flags missing information as [VERIFY] rather than inventing it
- Keeps care performed by another agency, care performed before arrival, and
  interventions prepared but not performed out of structured fields and written
  out in full in the narrative, attributed to whoever performed them
- Keeps each patient's facts separate from every other patient's in a
  multi-patient incident
- Applies universal paramedicine documentation standards when no agency policy is
  provided

## What This Tool Does Not Do

- Does not make or support clinical decisions of any kind
- Does not access ePCR platforms or submit documents
- Does not invent, assume, or infer clinical detail
- Does not reproduce information already in structured fields
- Does not reference a structured field entry that does not exist
- Does not assume the documenting crew performed an act whose performer is unstated
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
├── claude-project-instructions.md  ← compact Instructions field for a Claude Project
├── system-prompt.md                ← full system prompt for Gemini, direct API,
│                                     and any platform without a character limit
├── chatgpt-instructions.md         ← condensed instructions for ChatGPT Custom
│                                     GPTs (fits the 8,000 character limit)
├── paramedic-narrative.skill       ← the install file for Claude specifically
├── agency-config-template.md       ← standardized configuration template for
│                                     agencies and Chief Paramedics to complete
├── provider-profile-template.md    ← personal provider profile template --
│                                     one per provider, never shared
├── assets/                         ← brand and design assets
│   ├── pn-header.png               ← horizontal header lockup (PNG, used in README)
│   ├── pn-header.svg               ← horizontal header lockup (SVG source)
│   ├── pn-badge.png                ← square badge mark (PNG)
│   ├── pn-badge.svg                ← square badge mark (SVG source)
│   ├── pn-ecg.png                  ← ECG stylistic element (PNG)
│   ├── pn-ecg.svg                  ← ECG stylistic element (SVG source)
│   ├── pn-social-preview.png       ← GitHub social preview card (1280x640)
│   └── pn-social-preview.svg       ← social preview card (SVG source)
├── docs/                           ← provider-facing documents
│   ├── TPF_ParamedicNarrative_DictationPocketCard_2026_v1.txt
│   │                               ← 12-point dictation skeleton (text)
│   ├── TPF_ParamedicNarrative_DictationPocketCard_2026_v1.pdf
│   │                               ← printable pocket-size card (5in x 6.55in)
│   ├── TPF_ParamedicNarrative_DictationBusinessCard_2026_v1.pdf
│   │                               ← wallet-size card, category names only
│   ├── TPF_ParamedicNarrative_MobileReferenceCard_2026_v1.png
│   │                               ← tall reference image for a phone screen
│   └── spec-addendum-sections-4-4A-4B-4C.md  ← v1.3.0 design addendum
└── paramedic-narrative/            ← folder containing the source files
    ├── SKILL.md                    ← full clinical reference standard -- upload
    │                                 this as a Knowledge File in ChatGPT
    └── references/
        ├── documentation-standards-primer.md  ← detailed documentation
        │                                         standards reference
        └── narrative-formats.md    ← section definitions and quality
                                      checklists for all supported formats
```

**You only need one or two of these depending on who you are:**
- **Line provider using Claude**: download `paramedic-narrative.skill`
- **Line provider using ChatGPT**: see the ChatGPT two-file setup below
- **Line provider using Gemini or another platform**: open `system-prompt.md` and copy its contents
- **Line provider using Microsoft Copilot**: see the Copilot section below
- **Setting up on a phone**: see the Mobile section below
- **New provider setting up their profile**: open `provider-profile-template.md`
  (or say "build my provider profile" to the skill and it will guide you)
- **Agency administrator or Chief Paramedic**: open `agency-config-template.md`
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

1. Go to [claude.ai](https://claude.ai) and sign in.
2. Click **Projects** in the left sidebar, then **New Project**. Give it a short,
   recognizable name -- something like **PCR Narratives** or **My Documentation
   Assistant**. You will come back to this Project every time you document a call,
   so name it something you will recognize instantly.
3. In the Project, open **Settings** and paste the full contents of
   `claude-project-instructions.md` (everything below the horizontal rule) into
   the **Instructions** field.
4. In the Project's **Files** section, upload `paramedic-narrative/SKILL.md` and
   both files in `paramedic-narrative/references/` (choose UTF-8 if you're asked
   about encoding).

   Do not paste `system-prompt.md` into a Claude Project. It contains everything
   SKILL.md already contains, and the Instructions field is re-sent with every
   message, so you would pay for the whole standard on every turn and the two
   copies would drift apart when one is updated. `claude-project-instructions.md`
   carries only the rules that must be in context at all times and points to the
   project files for the rest. `system-prompt.md` is for platforms with no file
   retrieval.
5. Start a new conversation in the Project and say "I want to set up my provider
   profile" -- the skill asks a few questions and remembers your name, credential,
   and agency for every future session.
6. That is it. Come back to this same Project whenever you need to document a call.

This works identically whether you're on the Claude iOS app, the Android app, or
a browser. Some accounts also have a separate **Skills** feature under Project
Settings -- if yours does, you can instead download `paramedic-narrative.skill`
from the [Releases page](../../releases/latest) and upload it there. If there is
no Skills option, or the uploaded file shows up as unreadable text instead of an
installed skill, your account doesn't have that feature -- use the steps above.

**If you use ChatGPT:**

ChatGPT Custom GPTs have a character limit on the Instructions field. Paramedic-Narrative
uses a two-file setup to work around this -- a condensed instructions file and a
Knowledge File containing the full clinical reference standard.

1. On this page, click the file called `chatgpt-instructions.md`. Click the copy icon.
2. In ChatGPT, go to **Explore GPTs > Create > Configure** and paste the copied text
   into the **Instructions** field.
3. Still in the Configure panel, scroll down to **Knowledge** and click **Upload files**.
4. Download `paramedic-narrative/SKILL.md` from this repository and upload it as a
   Knowledge File. This gives the GPT access to the full clinical documentation standard.
5. Give it a recognizable name -- **Paramedic Narratives** or **PCR Assistant**.
6. Click **Save**. Use that Custom GPT for every documentation session.
7. In your first conversation, say "I want to set up my provider profile" -- paste
   the resulting file below the Instructions field or upload it as an additional
   Knowledge File.

**If you use Google Gemini:**

1. Copy the contents of `system-prompt.md` as described above.
2. In Gemini, go to **Gems > New Gem**.
3. Paste the copied text into the instructions field.
4. Name it something recognizable -- **PCR Narratives** or **Paramedic Documentation**.
5. Save. Use that Gem for every documentation session.
6. In your first conversation, say "I want to set up my provider profile" and
   paste the resulting file below your instructions.

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
policies before using this or any AI tool. If your agency, Chief Paramedic, or
jurisdiction prohibits AI-assisted documentation tools, do not use this tool in
that context. If you are unsure whether your use is permitted, ask your supervisor
or Chief Paramedic before proceeding.

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

### Claude

Claude.ai Projects support two setup methods. Which one is available depends on
your account and plan, not on your device -- use the Files + Instructions method
unless you've already confirmed your account has Skills.

**Files + Instructions (works on every account):**
1. In Claude.ai, open or create a Project, and go to Project **Settings**
2. Paste the full contents of `system-prompt.md` from this repository into
   the **Instructions** field
3. Download `paramedic-narrative/SKILL.md` and any reference files you need
   from `paramedic-narrative/references/` in this repository
4. Upload them to the Project's **Files** section (choose UTF-8 if asked
   about encoding)
5. Optionally upload your agency documentation standard as a Project file
   (see [Configuration](#configuration))

**Skill package (only if your account has this feature):**
1. Download `paramedic-narrative.skill` from the
   [Releases](../../releases/latest) page
2. In the Project, look for a **Skills** option under Project Settings
3. If you find it, upload the `.skill` file there
4. If there is no Skills option, or the uploaded file shows up as unreadable
   or garbled text instead of an installed skill, your account does not have
   this feature -- use the Files + Instructions method above instead

### ChatGPT (Custom GPT -- two-file setup)

ChatGPT Custom GPTs have a character limit on the Instructions field. Paramedic-Narrative
addresses this with a two-file setup: a condensed instructions file in the Instructions
field, and the full clinical reference standard uploaded as a Knowledge File.

**Instructions field:**
1. Open `chatgpt-instructions.md` in this repository and copy its full contents
2. In ChatGPT, go to Explore GPTs > Create > Configure
3. Paste the contents into the **Instructions** field

**Knowledge File:**
4. Download `paramedic-narrative/SKILL.md` from this repository
5. In the Configure panel, scroll to **Knowledge** and click **Upload files**
6. Upload `SKILL.md` -- this gives the GPT the full clinical documentation standard

**Finish setup:**
7. Optionally paste your agency configuration below the instructions, or upload it
   as an additional Knowledge File
8. Give the GPT a recognizable name and save

**Why two files?** The Instructions field holds the behavioral rules -- how the tool
thinks and what it refuses to do. The Knowledge File holds the clinical reference
content -- scoring tools, medication documentation standard, forensic standard,
vital thresholds, and handoff frameworks. The GPT consults the Knowledge File during
conversation without it counting against the Instructions character limit.

### Google Gemini (Gem)

1. Copy the full contents of `system-prompt.md` from this repository
2. In Gemini, go to Gems > New Gem
3. Paste the contents into the instructions field
4. Optionally paste your agency documentation standard below
5. Save the Gem

### Microsoft Copilot (M365)

Microsoft 365 Copilot supports partial setup through Custom Instructions. The
clinical reference standard must be pasted at the start of each session.

**One-time setup (Custom Instructions):**
1. Open `chatgpt-instructions.md` in this repository and copy its full contents
2. In Copilot, click the three-dot menu (top right) > **Settings** >
   **Personalization** > **Edit instructions**
3. Paste the contents and click **Save instructions**

**Per-session (clinical reference):**
4. Go to `paramedic-narrative/SKILL.md` in this repository, click **Raw**,
   select all (Ctrl+A / Cmd+A), and copy
5. At the start of each Copilot conversation, paste the text with the note:
   "This is your clinical reference standard for this session."
6. Then describe your call

The behavioral rules persist via Custom Instructions. The clinical reference
content is pasted each session because the Personalization > Custom Instructions
path used above has no persistent knowledge-upload feature equivalent to ChatGPT
Custom GPTs. Microsoft 365 Copilot separately supports declarative agents (built
via Copilot Studio / Agent Builder) that do support persistent knowledge sources
alongside instructions -- if your organization has that capability available and
wants a one-time setup instead of a per-session paste, a declarative agent may be
a better fit than the workflow above; that setup is not yet documented here.

**Note:** Some organizations restrict Copilot customization through IT policy.
If the Custom Instructions field is unavailable, paste both `chatgpt-instructions.md`
and `SKILL.md` at the start of each session.

### Mobile (iOS and Android)

Paramedic-Narrative works fully on a smartphone. Claude, ChatGPT, and Gemini
all have free mobile apps and also work in any phone browser without an app.

**Getting files from GitHub on your phone:**

The GitHub mobile app does not support raw file downloads. Use your phone's
browser (Safari on iOS, Chrome on Android) instead:

1. Go to `github.com/The-Paramedic-Foundation/paramedic-narrative-skill`
   in your phone browser
2. Navigate to the file you need
3. Tap the file name to open it
4. Tap **Raw** (top right of the file view) -- this opens the plain text
5. Tap and hold anywhere in the text > **Select All** > **Copy**
   (or use your browser's share sheet to save to Files/Downloads)

**Claude on mobile:**
Use the Files + Instructions method (see [Installation](#installation) above) --
it works identically on the Claude iOS app, the Android app, and any browser,
because Project Files and Instructions are both available from the phone app
itself. No desktop or browser detour is required for this method.
1. In the Claude app, open or create your Project and go to Project Settings
2. Paste `system-prompt.md` into **Instructions**
3. Download `paramedic-narrative/SKILL.md` (and any reference files you want)
   using the phone browser steps above, then upload them to the Project's
   **Files** section from the app
4. Your agency config uploads the same way, directly from the Claude app

The Skill-package method (`.skill` upload) is a separate, account-dependent
feature. If you've confirmed your account has it, the upload step itself
still needs a browser (see the note in [Installation](#installation)); the
Claude app can then use the Project normally afterward.

**ChatGPT on mobile:**
Creating and editing a Custom GPT's Instructions and Knowledge Files is a
web-only feature -- the ChatGPT mobile app can only *use* a GPT that already
exists, not create or edit one. Do the setup itself in your phone's browser,
then use the ChatGPT app afterward.
1. In your phone browser, go to `chatgpt.com`, sign in, and go to
   **Explore GPTs > Create > Configure**
2. In a second browser tab, open `chatgpt-instructions.md` in this repository,
   tap Raw, select all, copy, and paste it into the **Instructions** field
3. Scroll to **Knowledge**, tap **Upload files**, and upload
   `paramedic-narrative/SKILL.md` (download it from this repository first if
   your browser requires a local file)
4. Save the GPT. From then on, open the ChatGPT app and use this GPT normally --
   the app is only unable to *edit* it, not use it

**Gemini on mobile:**
Creating, editing, or deleting a Gem is a web-only feature -- the Gemini mobile
app can only *use* a Gem that was already created at gemini.google.com. Do the
setup itself in your phone's browser, then use the Gemini app afterward.
1. In your phone browser, go to `gemini.google.com`, sign in, and go to
   **Gems > New Gem**
2. In a second browser tab, open `system-prompt.md` in this repository, tap Raw,
   select all, copy, and paste it into the instructions field
3. Save the Gem. From then on, open the Gemini app and use this Gem normally --
   the app is only unable to *create or edit* it, not use it

**Copilot on mobile:**
1. In the Copilot app, tap your profile > **Settings** > **Personalization** >
   **Edit instructions** > paste contents of `chatgpt-instructions.md` > Save
2. At the start of each session: open `SKILL.md` in your phone browser, tap Raw,
   select all, copy, paste as your first message in Copilot

**Using the tool on shift:**
- Tap the microphone and describe the call out loud -- no typing required
- Use the camera to photograph clinical data (vital sign printouts, 12-lead
  strips, medication lists) -- confirm no PHI visible before photographing
- Copy the approved narrative and paste into your ePCR mobile app

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
> [protocol system name]. My Chief Paramedic is [name]."

The skill will apply that context for the session.

**For ChatGPT specifically:** paste your agency configuration below the instructions
in the Configure panel, or upload it as an additional Knowledge File alongside
`SKILL.md`. Both approaches work.

### For agencies and Chief Paramedics

The repository includes a standardized **agency configuration template** that medical
directors and agency administrators can complete once and distribute to all providers.
When every provider uses the same configuration file, every narrative produced in
your system reflects your protocols, your ePCR platform, your documentation standard,
and your Chief Paramedic's clinical expectations automatically.

**The template file is:** `agency-config-template.md`

It covers:
- Agency identity and service area context
- Chief Paramedic endorsement and scope of authorization
- ePCR platform and narrative field specifications
- Documentation standard and minimum narrative requirements
- Protocol system name, version, and CPG sources adopted by Chief Paramedic
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
4. Have your Chief Paramedic review and complete Section 2 (endorsement)
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

**Never photograph or upload an image in which any direct patient identifier is
visible.** A document may be photographed only once every identifier on it has
been cropped or covered before the shot; if it can't be fully redacted first,
dictate the content instead. See Section 6 of [ETHICS.md](ETHICS.md).

The skill will identify what additional information is needed for a complete narrative,
ask only for what is missing and narrative-relevant (not for information already
captured in your structured PCR fields), and produce a draft in your agency's
declared narrative format (Clinical Summary / S / O / A / P by default).

**Dictating a call:** talk through the 12-point verbal report skeleton in any
order -- call frame, arrival picture, patient, story, pertinent negatives, exam
highlights, numbers, thinking, doing, moving, handoff, exceptions. A printable
pocket card, a wallet-size business card, and a mobile-reference image sized for
a phone screen are all in [`docs/`](docs/). Fragments are fine: you can document across
multiple messages over hours, and the skill tracks what is still missing rather
than re-interviewing you. Documenting long after a call? Say so -- the skill
switches to targeted recall questions built from what it already knows.

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
suspected non-accidental trauma, intoxication-related harm, arson, motor vehicle
collision with potential impairment or fatality, threats, and any scene where law
enforcement is investigating.

---

## Multi-Platform Files

| File | Purpose | Platform |
|---|---|---|
| `paramedic-narrative.skill` | Native skill package | Claude |
| `chatgpt-instructions.md` | Condensed instructions (fits character limit) | ChatGPT, Copilot |
| `claude-project-instructions.md` | Compact Instructions field; points to project files | Claude Projects |
| `system-prompt.md` | Full system prompt | Gemini, direct API, any LLM |
| `paramedic-narrative/SKILL.md` | Full clinical reference standard | ChatGPT Knowledge File, Copilot per-session paste, all (human-readable) |
| `paramedic-narrative/references/documentation-standards-primer.md` | Standards reference | Loaded on demand |

All versions are written to express the same clinical logic, but ChatGPT's
Knowledge File is consulted through retrieval rather than read in full on every
turn, so behavior there is not guaranteed identical to Claude, Gemini, or a
direct-API session in every case -- the most safety-critical rules (privacy,
controlled substance, forensic, non-fabrication) are duplicated directly into
`chatgpt-instructions.md`'s Instructions field for this reason, rather than left
to Knowledge File retrieval alone.

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

Current version: **2.1.1**

**2.1.1 -- Cross-file parity corrections.** No change to clinical content, thresholds,
or standards, so agencies that have reviewed 2.1.0 carry no re-verification burden.
An audit of all instruction files found that safety-critical text had been paraphrased
into the platform-specific renderings rather than reproduced, and the paraphrases had
lost content. Corrected: `chatgpt-instructions.md` regains the full eleven-item
forensic trigger list (it had carried five, omitting domestic violence and sexual
assault among others), the complete standing disclaimer including the AI-tool and
no-clinical-advice sentences, the camera-metadata PHI rule, the container-identifier
and reconciliation elements of the controlled substance audit trail, the pre-draft
verification step as an explicit workflow step, and the rule against assuming your
crew performed an act whose performer is unstated. `system-prompt.md` regains
"threats" in the forensic trigger list and the neonate temperature threshold, and now
uses "Chief Paramedic" rather than "medical director."
`claude-project-instructions.md` now carries incident and patient workspace isolation
inline rather than only by reference to a project file, since retrieval is not
guaranteed. The dictation pocket card and its printable variants gain the attribution
prompts that 2.1.0 described but did not ship. Updating from 2.1.0 replaces the
instruction and reference files only.

**2.1.0 -- Attribution and data-integrity boundary.** Adds a core section covering
care performed by another agency's provider, care performed before the documenting
crew arrived and assumed responsibility, and interventions prepared or considered but
not performed. Structured ePCR entries are attributed entries and, where structured
data feeds external reporting, become the record of what an agency provided; the three
categories above therefore stay out of structured fields and are carried in full by
the narrative. Core Operating Principle 1 now extends the non-fabrication rule to
other clinicians' clinical reasoning. Core Operating Principle 5 now requires
confirming that a structured entry exists before referencing it, which closes a real
failure mode: a narrative that says "as charted" for an intervention the agency's own
standard forbids charting leaves that intervention documented nowhere. Related changes
in the medication administration standard, workflow prompts, dictation pocket card,
narrative formats, primer, and a new agency configuration Section 4A. Updating from
2.0.x replaces the instruction and reference files only; provider profiles and
existing agency configurations remain valid, though agencies should complete the new
Section 4A.

Version history and release notes are maintained in this repository. Check
[Releases](../../releases) for updates. Providers and agencies using this tool in
ongoing documentation workflows should review updates periodically.

Significant updates affecting clinical content, privacy standards, or the ethical
framework will be clearly noted in release notes.

### Updating an existing installation to a new version

Updates are not automatic on any platform. When a new version is released, each
provider updates their own installation:

**Claude:**
1. In your Project's **Instructions** field, paste the new
   `claude-project-instructions.md` over whatever is there now. If your Project
   currently holds the full `system-prompt.md` in Instructions, replacing it with
   this file is the upgrade: same standards, a fraction of the per-message cost.
2. In **Files**, remove the old `SKILL.md` and reference files and upload the new
   ones -- don't leave both, or the assistant may consult the outdated copy.
3. Your provider profile, agency configuration files, and past conversations
   are unaffected -- only the instructions and reference files are replaced.
4. This works the same on the Claude iOS app, the Android app, or a browser.

If your account uses the Skill package instead: download the new
`paramedic-narrative.skill` from the [Releases](../../releases/latest) page,
remove the old skill under **Settings > Skills**, and upload the new file.
This step requires a browser (web or desktop).

**ChatGPT (Custom GPT):**
1. Copy the new `chatgpt-instructions.md` and paste it over the old contents of
   the **Instructions** field in your GPT's Configure panel.
2. In **Knowledge**, delete the old `SKILL.md` and upload the new one. Do not
   leave both -- the GPT may consult the outdated copy.
3. Save the GPT.

**Gemini (Gem):**
1. Copy the new `system-prompt.md` and paste it over the old contents of your
   Gem's instructions field. Re-paste your agency configuration below it if you
   had one. Save.

**Microsoft Copilot:**
1. Update Custom Instructions with the new `chatgpt-instructions.md` contents.
2. Use the new `SKILL.md` for your per-session paste going forward.

**Agency administrators:** when you distribute a new agency configuration file
version, the same rule applies -- providers must replace the old file in their
Claude Project or re-paste it on other platforms. Increment the version in
Section 11 of the configuration and notify providers.

**How to tell which version you are running:** ask the assistant "what version
are you?" -- the version is stated in the skill and system prompt -- or compare
against the version shown at the top of this README.

---

## Contributing

Contributions are welcome from providers, agencies, educators, Chief Paramedics,
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
> *documentation for paramedics and EMTs* (Version 2.1.1) [Software]. The Paramedic
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
