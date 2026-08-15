# Paramedic-Narrative Skill — Provider Profile Template

**The Paramedic Foundation**
paramedicfoundation.org · Version 2.1.1

---

## Instructions

This is your personal provider profile for the Paramedic-Narrative skill. It
tells the skill who you are, where you work, what roles you operate in, and any
standing documentation preferences you have. It is specific to you and should
not be shared.

**How to create your profile:**
The easiest way is to say "I want to set up my provider profile" in a conversation
with the skill. It will ask you questions and generate this file automatically.

Alternatively, fill in this template manually in any text editor and save it as
`provider-profile.md`.

**Where to keep it:**
Upload it to your Claude Project alongside the skill. It will be active for every
conversation in that Project without you having to re-enter your information.
For ChatGPT or Gemini, paste its contents below the system prompt in your Custom
GPT or Gem.

**Updating your profile:**
When something changes -- new agency, new credential, new role -- say "update my
provider profile" and describe what changed. The skill will produce an updated file.

---

## Section 1: Provider Identity

**Full Name:**
[Your name as it should appear in documentation]

**Credential:**
[e.g., NRP, EMT-B, AEMT, CP-C, FP-C, CCP-C, CCEMT-P, or equivalent. Include
all active credentials if more than one.]

**License Number and State:**
[Optional -- e.g., Colorado NRP 12345. Include if you want it available for
transfer-of-care documentation.]

**Years of Experience:**
[Optional -- helps the skill calibrate explanations and assumptions]

---

## Section 2: Agencies

List every agency you work for. The short name is what you use in org-switch
commands -- keep it brief and recognizable.

**Agency 1:**
- Full name: [Agency full legal name]
- Short name: [e.g., "County EMS," "Regional Health," "County Fire"]
- Role(s) at this agency: [e.g., Emergency Paramedic, Community Paramedic]
- Config file: [e.g., agency-config-county-ems.md]

**Agency 2:**
- Full name:
- Short name:
- Role(s) at this agency:
- Config file:

**Agency 3:**
- Full name:
- Short name:
- Role(s) at this agency:
- Config file:

[Add more as needed]

**Default agency:**
[Which agency should be assumed active at session start if you do not specify --
e.g., "County EMS." Leave blank if you always specify.]

---

## Section 3: Role Contexts

Check all that apply and add any notes relevant to your practice in each role.

**Emergency Paramedic:**
[ ] Active
Notes: [e.g., "Primary role. 911 ALS response. High volume trauma and behavioral
health." Leave blank if no special notes.]

**Rescue Paramedic:**
[ ] Active
Notes: [e.g., "Swift water rescue certification. Wilderness EMS protocols apply
for backcountry calls." Leave blank if not applicable.]

**Community Paramedic:**
[ ] Active
Notes: [e.g., "CP-C certified. MIH program at Agency 2. Home visit and clinic
model." Leave blank if not applicable.]

**Hospital Paramedic:**
[ ] Active
Notes: [e.g., "CCT role at Agency 1. Vent-dependent transport common. IABP and
LVAD transport authorized." Leave blank if not applicable.]

---

## Section 4: Standing Documentation Preferences

These preferences apply across all sessions unless overridden by a specific session
instruction.

**Abbreviation style:**
[e.g., "Standard prehospital abbreviations preferred" or "Spell out medication
names fully" or "No abbreviations -- agency QI requirement"]

**Vital sign reference preference:**
[e.g., "Reference vitals as charted -- do not include values in narrative" or
"Include initial vital set in narrative when it drives clinical reasoning"]

**Tense and voice:**
[e.g., "Past tense, active voice throughout" -- this is the default and does not
need to be specified unless you want something different]

**Any recurring clinical context:**
[e.g., "I carry ketamine and push-dose epinephrine. Always prompt for ketamine
dose calculation." Or: "My agency does not carry nitrates. Do not prompt for
nitroglycerin." Or: "I frequently work extended transport intervals (45+ min) --
document this context when relevant to treatment decisions."]

**Transfer of care preference:**
[e.g., "I use IMIST-AMBO for all ALS handoffs" or "My receiving facility uses
SBAR -- use that framing for the handoff section"]

**Other standing preferences:**
[Anything else the skill should always know about how you document]

---

## Section 5: Profile Version History

| Version | Date | Summary of Changes |
|---------|------|--------------------|
| 1.0 | [date] | Initial profile |
| | | |

---

*This profile is personal to [Provider Name] and should not be shared.*

*Template published by The Paramedic Foundation under CC BY 4.0.*
*paramedicfoundation.org*
