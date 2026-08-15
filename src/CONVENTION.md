# File convention for the canonical knowledge set (3.0.0)

Sources, read-only:
  /root/pns2/paramedic-narrative/SKILL.md
  /root/pns2/paramedic-narrative/references/documentation-standards-primer.md
  /root/pns2/paramedic-narrative/references/narrative-formats.md
Always-loaded block (already written, do not duplicate its content):
  /root/build/ALWAYS-BLOCK.md
Output directory:
  /root/build/knowledge/

## Absolute rule

This is a clinical documentation standard. Do NOT invent, rewrite, or "improve" any
clinical content, threshold, criterion, or rule. You are REORGANIZING existing text.
Every sentence in your output must trace to one of the three source files. If two
sources say the same thing differently, follow the deduplication instruction you were
given. If you find a genuine conflict you were not told about, keep the SKILL.md
version and note the conflict at the end of your final message.

## Every file starts with exactly these two lines, then a blank line

CONSULT THIS FILE WHEN: <the trigger, copied verbatim from the router entry you were given>
DO NOT CONSULT OTHERWISE.

## Contents

- Directives only. Strip background, history, rationale that does not change what the
  model does, and human-navigation scaffolding.
- Keep clinical rationale ONLY where it changes behavior (e.g. why a 12-month
  postpartum window exists, why troponin makes a HEART score partial).
- Do not restate anything already in ALWAYS-BLOCK.md. Read it first. If a rule is
  there, it is not repeated here.
- No cross-references to other WHEN- files. Each file must be actionable alone.
  If content is genuinely needed by two files, tell me rather than duplicating it.
- Keep [VERIFY] tagging instructions wherever the source has them.

## Style, non-negotiable

- No em dashes. Use "--" with a space either side.
- Plain ASCII punctuation except degree symbols in temperatures, which are preserved.
- Markdown headings and lists are fine in these files (they are reference files, not
  narrative output).
- Preserve exact numeric thresholds, scale values, and criterion wording.
- "Chief Paramedic", never "medical director". "ePCR platform", never "PCR platform".

## Final message

State: files written, approximate size of each, any content you could not place, any
conflict found. Do not paste file contents back.
