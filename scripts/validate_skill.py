#!/usr/bin/env python3

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/case-diagnosis.md",
    "references/solution-design.md",
    "references/evidence-quant.md",
    "references/research-protocol.md",
    "references/hr-lenses.md",
    "references/storyline-deck.md",
    "references/deck-qa.md",
    "references/red-team.md",
    "scripts/score_options.py",
    "examples/option-scoring.sample.json",
]

def fail(message):
    print(f"ERROR: {message}")
    sys.exit(1)

for rel in REQUIRED_FILES:
    if not (ROOT / rel).is_file():
        fail(f"Missing required file: {rel}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

if not skill.startswith("---\n"):
    fail("SKILL.md must start with YAML frontmatter.")

frontmatter_match = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not frontmatter_match:
    fail("Could not parse SKILL.md frontmatter.")

frontmatter = frontmatter_match.group(1)

if not re.search(r"^name:\s*hr-case-competition-strategist\s*$", frontmatter, re.M):
    fail("SKILL.md frontmatter is missing the expected name.")

if not re.search(r"^description:\s*.+$", frontmatter, re.M):
    fail("SKILL.md frontmatter is missing a description.")

if len(skill.strip()) < 2000:
    fail("SKILL.md appears unexpectedly short.")

print("Skill validation passed.")
print(f"Checked {len(REQUIRED_FILES)} required files.")
