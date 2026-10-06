# HR Case Competition Strategist

A portable Agent Skill for building competition-grade HR and people-strategy case solutions.

The skill is designed for:
- MBA HR case competitions
- people strategy consulting cases
- talent and retention problems
- hiring and assessment redesign
- organization design
- workforce strategy
- employee experience
- people analytics
- learning and capability
- wellbeing
- HR technology / AI cases
- change and operating model cases

## What makes this different

This skill is intentionally anti-generic.

It does not accept "training + mentoring + engagement + AI dashboard" as a finished solution.

It forces a full chain:

**evidence → diagnosis → decisive insight → design principles → competing architectures → mechanism-level solution → economics → implementation → storyline → red-team**

Every major recommendation is expected to define:
- target user
- trigger
- workflow
- behavior change
- mechanism
- owner
- data
- technology
- guardrails
- KPI
- cost/effort
- pilot
- failure mode
- scale/kill criteria

## Repository structure

```text
Personal-Skill/
├── SKILL.md
├── README.md
├── .gitignore
├── references/
│   ├── case-diagnosis.md
│   ├── solution-design.md
│   ├── evidence-quant.md
│   ├── research-protocol.md
│   ├── hr-lenses.md
│   ├── storyline-deck.md
│   ├── deck-qa.md
│   └── red-team.md
├── scripts/
│   └── score_options.py
└── examples/
    └── option-scoring.sample.json
```

## Installation

Download this repository as a ZIP or clone it locally.

For an Agent Skills-compatible environment, upload or install the folder that contains `SKILL.md`.

Keep the full folder structure intact so the skill can access its reference files and script.

## Suggested prompts

### Solve a case
> Use the HR Case Competition Strategist skill. Read the entire case first. Diagnose the root cause before proposing solutions. Give me three differentiated architectures, select the strongest one, quantify it, and create a judge-ready deck storyline.

### Critique my solution
> Red-team this HR case solution using the skill. Tell me where it is generic, weakly evidenced, financially questionable, difficult to implement, or vulnerable to judge questions. Then redesign the weak parts.

### Reverse-engineer winning decks
> Study these case competition decks. Extract the recurring patterns in diagnosis, solution design, quantification, storyline, and visual structure. Then use those principles—not their content—to improve my current case.

### Build a deck
> Convert the approved solution into a 10-slide competition deck. Use answer-first titles, one principal conclusion per slide, mechanism diagrams, credible economics, and explicit implementation gates.

## Recommended workflow

1. Upload the case and exhibits.
2. Ask for a Case Spine + issue tree only.
3. Validate the diagnosis.
4. Ask for 3 competing solution architectures.
5. Run the genericity test.
6. Select one architecture.
7. Build mechanism cards.
8. Quantify with scenarios.
9. Build the storyline.
10. Build the deck.
11. Run the red-team and deck QA before submission.

## Important

The skill should never fabricate research, survey results, benchmarks, or ROI assumptions.

Small-sample primary research should be described as directional unless the design justifies stronger inference.

A clever name is not a substitute for a mechanism.
