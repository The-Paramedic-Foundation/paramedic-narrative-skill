#!/usr/bin/env python3
"""
Build the four platform renderings from the canonical parts.

Sources of truth, edited by hand:
    src/ALWAYS-BLOCK.md      the always-loaded layer, identical on every platform
    src/knowledge/WHEN-*.md  retrieved on trigger
    src/static/*.md          README, ETHICS, LICENSE, templates

Sources live in src/. Everything else is generated. Do not hand-edit generated files.
Run:  python3 build.py && python3 build.py --verify
"""
import os, re, sys, zipfile, glob

VERSION = "3.0.0"
ROOT = os.path.dirname(os.path.abspath(__file__))
DIST = ROOT                              # generated files land at repo root
SRC    = os.path.join(ROOT, "src")       # hand-edited sources
STATIC = os.path.join(SRC, "static")
CHATGPT_LIMIT = 6500                     # target ceiling, not the observed 8000

def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)

ALWAYS = read(os.path.join(SRC, "ALWAYS-BLOCK.md")).strip()
FILES = sorted(glob.glob(os.path.join(SRC, "knowledge", "WHEN-*.md")))

FRONTMATTER = """---
name: paramedic-narrative
description: >
  PCR narrative documentation assistant for paramedics and EMTs. Produces compliant,
  non-hallucinated narratives in the agency's declared format (SOAP, SOAPE, CHART,
  DCHART-E, and others) that capture clinical reasoning, scene context, differential
  rationale, medication indication and response, controlled substance audit trails,
  multi-agency and prior-to-arrival care attribution, and forensic evidentiary detail
  -- without duplicating structured PCR fields.
  Accepts photo plus dictation intake and fragmented input across sessions,
  including during transport, with an on-request IMIST-AMBO handoff prep and a
  retrospective handoff training example appended to completed drafts.
  This is an editorial tool only. It does not make clinical decisions and must never be
  used for that purpose. Use this skill whenever a provider asks to document a call,
  write a narrative, draft a patient care report, or document any paramedicine patient
  encounter. Trigger on: "write up this call," "help me document," "draft a narrative,"
  "PCR narrative," "patient care report," "SOAP note," "run sheet," or any description
  of a paramedicine patient encounter seeking documentation help. Also trigger when a
  provider pastes vitals, a call summary, or a medication list and asks for help writing
  it up.
---

<!-- GENERATED FILE. Edit src/, then run build.py. -->

# Paramedic-Narrative Documentation Assistant

Version {v}. The rules below are always in effect. Detailed standards live in
`references/`, retrieved on the triggers listed in the router.

""".replace("{v}", VERSION)

GEN = "<!-- GENERATED FILE. Edit src/, then run build.py. -->"


def build_skill():
    write(os.path.join(DIST, "paramedic-narrative", "SKILL.md"), FRONTMATTER + ALWAYS + "\n")
    for p in FILES:
        write(os.path.join(DIST, "paramedic-narrative", "references", os.path.basename(p)), read(p))


def build_claude_project():
    head = f"""# Paramedic-Narrative -- Claude Project Instructions
## The Paramedic Foundation - CC BY 4.0 - Version {VERSION}
## Claude Project "Instructions" field. Upload every references/WHEN-*.md as a project file.
## Paste only what is below the line. These header lines are not part of it.

{GEN}

---

"""
    write(os.path.join(DIST, "claude-project-instructions.md"), head + ALWAYS + "\n")


def build_chatgpt():
    head = f"""# Paramedic-Narrative -- ChatGPT Instructions
## The Paramedic Foundation - CC BY 4.0 - Version {VERSION}
## ChatGPT Custom GPT Instructions field. Upload every references/WHEN-*.md as a Knowledge File.
## Paste only what is below the line. These header lines are not part of it.

{GEN}

---

"""
    write(os.path.join(DIST, "chatgpt-instructions.md"), head + ALWAYS + "\n")


def build_system_prompt():
    """Gemini and direct API have no retrieval. Concatenate everything."""
    parts = [f"""# Paramedic-Narrative Documentation Assistant
## System Prompt -- Full Version (Gemini, API, and platforms without retrieval)
## The Paramedic Foundation - CC BY 4.0 - Version {VERSION}

{GEN}

This file is the always-loaded block followed by every reference file inline, because
this platform has no retrieval mechanism. The router below still applies: read the
named section when its condition is met.

---

""", ALWAYS, "\n\n---\n\n# REFERENCE SECTIONS\n"]
    for p in FILES:
        body = read(p).split("\n")
        trigger = body[0].replace("CONSULT THIS FILE WHEN:", "").strip()
        rest = "\n".join(body[2:]).strip()
        parts.append(f"\n\n---\n\n## {os.path.basename(p)}\n\nApplies when: {trigger}\n\n{rest}\n")
    write(os.path.join(DIST, "system-prompt.md"), "".join(parts))


def build_package():
    """.skill zip: one top-level dir, stored uncompressed."""
    out = os.path.join(DIST, "paramedic-narrative.skill")
    roots = ["LICENSE.md", "ETHICS.md", "README.md", "agency-config-template.md",
             "provider-profile-template.md"]
    for r in roots:                                  # static docs are part of dist too
        src = os.path.join(STATIC, r)
        if os.path.exists(src):
            write(os.path.join(DIST, r), read(src))
    if os.path.exists(out):
        os.remove(out)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_STORED) as z:
        z.write(os.path.join(DIST, "paramedic-narrative", "SKILL.md"),
                "paramedic-narrative/SKILL.md")
        for p in FILES:
            z.write(p, "paramedic-narrative/references/" + os.path.basename(p))
        for r in roots:
            src = os.path.join(STATIC, r)
            if os.path.exists(src):
                z.write(src, "paramedic-narrative/" + r)
        for gen in ["system-prompt.md", "chatgpt-instructions.md",
                    "claude-project-instructions.md"]:
            z.write(os.path.join(DIST, gen), "paramedic-narrative/" + gen)


def verify():
    fails = []

    # 1. the always-block is byte-identical in every rendering
    targets = {
        "SKILL.md": os.path.join(DIST, "paramedic-narrative", "SKILL.md"),
        "claude-project-instructions.md": os.path.join(DIST, "claude-project-instructions.md"),
        "chatgpt-instructions.md": os.path.join(DIST, "chatgpt-instructions.md"),
        "system-prompt.md": os.path.join(DIST, "system-prompt.md"),
    }
    for name, p in targets.items():
        if ALWAYS not in read(p):
            fails.append(f"always-block not verbatim in {name}")

    # 2. chatgpt instructions fit the budget
    s = read(targets["chatgpt-instructions.md"])
    body = s.split("\n---\n", 1)[1].strip()
    if len(body) > CHATGPT_LIMIT:
        fails.append(f"chatgpt body {len(body)} > {CHATGPT_LIMIT}")

    # 3. every knowledge file is routed, and every router entry has a file
    router = set(re.findall(r"^- (WHEN-[A-Z0-9-]+\.md):", ALWAYS, re.M))
    present = {os.path.basename(p) for p in FILES}
    for m in sorted(present - router):
        fails.append(f"file not in router: {m}")
    for m in sorted(router - present):
        fails.append(f"router points at missing file: {m}")

    # 4. file convention
    for p in FILES:
        L = read(p).split("\n")
        if not L[0].startswith("CONSULT THIS FILE WHEN:") or L[1].strip() != "DO NOT CONSULT OTHERWISE.":
            fails.append(f"bad header: {os.path.basename(p)}")

    # 5. house style, including the hand-edited static docs
    static = glob.glob(os.path.join(STATIC, '*.md'))
    for p in FILES + list(targets.values()) + static:
        t = read(p)
        # a term inside double quotes is being quoted, not used: changelogs and the
        # contributor style guide legitimately name the forms they forbid
        u = re.sub(r'"[^"\n]*"', '""', t)
        if "\u2014" in u:
            fails.append(f"em dash in {os.path.basename(p)}")
        if re.search(r"\bmedical director\b", u, re.I):
            fails.append(f"'medical director' in {os.path.basename(p)}")
        if re.search(r"(?<!e)PCR platform", u):
            fails.append(f"bare 'PCR platform' in {os.path.basename(p)}")

    # 6. no stale version strings
    for p in list(targets.values()):
        if re.search(r"\b2\.\d+\.\d+\b", read(p)):
            fails.append(f"stale version string in {os.path.basename(p)}")

    print("\n".join("FAIL " + f for f in fails) if fails else "all checks pass")
    return 1 if fails else 0


if __name__ == "__main__":
    if "--verify" in sys.argv:
        sys.exit(verify())
    build_skill(); build_claude_project(); build_chatgpt()
    build_system_prompt(); build_package()
    print(f"built {len(FILES)} knowledge files + 4 renderings -> repo root")
