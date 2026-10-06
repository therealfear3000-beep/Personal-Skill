# Red-Team and Judge Rubric

## 1. Score the solution out of 100

### Diagnosis — 15
Does it identify the actual root cause rather than repeat the prompt?

### Insight — 10
Are there non-obvious, decision-changing insights?

### Case specificity — 10
Could the solution exist without this particular case?

### Differentiation — 10
Is the mechanism meaningfully distinct from generic HR practice?

### Mechanism quality — 10
Is it clear why the intervention should change behavior?

### Evidence — 10
Are important claims supported and assumptions labeled?

### Feasibility — 10
Can the organization realistically execute it?

### Economics/impact — 10
Is value quantified credibly where appropriate?

### Implementation/adoption — 5
Are owners, sequencing, and user friction addressed?

### Storyline/deck — 10
Is the recommendation immediately understandable and persuasive?

Target:
85+ = competition-grade.
75–84 = strong but vulnerable.
65–74 = plausible but generic/incomplete.
Below 65 = redesign.

A high total cannot rescue a fatal flaw.

## 2. Fatal-flaw gates

Flag RED if any is true:

- solution does not address the diagnosed root cause,
- core claim is fabricated,
- economics depend on hidden assumptions,
- intervention violates obvious privacy/fairness constraints,
- adoption depends on substantial extra work with no incentive,
- technology is treated as magic,
- implementation owner is absent,
- recommendation contradicts an explicit case constraint,
- solution is merely a renamed generic HR program.

## 3. Judge attack

Generate the 10 hardest questions.

At minimum include:

1. Why is this the real problem?
2. What evidence rules out the obvious alternative explanation?
3. Why is this better than doing nothing?
4. Why not use a simpler/cheaper intervention?
5. What specifically is novel?
6. What would make employees/managers use it?
7. What assumption drives the ROI?
8. What is the largest implementation risk?
9. What happens if the pilot fails?
10. What exactly do you want us to approve?

Draft concise evidence-based answers.

## 4. CFO attack

Ask:
- cost?
- recurring cost?
- implementation burden?
- opportunity cost?
- break-even?
- sensitivity?
- double counting?
- what value is actually cashable?

## 5. CHRO attack

Ask:
- employee experience?
- manager burden?
- capability?
- fairness?
- privacy?
- governance?
- culture?
- change fatigue?
- HR operating model?

## 6. Business-leader attack

Ask:
- does this solve my operational problem?
- how much time does it consume?
- who owns delivery?
- what changes Monday morning?
- how quickly do I see value?

## 7. Employee attack

Ask:
- what is in it for me?
- what data is used?
- can the system harm me?
- can I challenge a decision?
- does this create more bureaucracy?
- do I trust it?

## 8. Pre-mortem

Write:

"It is 18 months later and this initiative failed."

Generate at least five plausible causes.

For each:
Failure mode:
Early warning:
Preventive action:
Contingency:
Owner:

## 9. Genericity attack

Remove all company names and branded solution names.

If the recommendation still reads naturally for almost any company,
it is insufficiently case-specific.

## 10. Simplification attack

Ask:

"If we could fund only one mechanism, which one creates most of the value?"

This reveals whether the architecture has a true strategic core.

## 11. Slide attack

For each slide ask:

- What decision does this help the judge make?
- What is the one takeaway?
- Is the title the takeaway?
- Is every element necessary?
- Is the evidence legible?
- Is the source clear?
- Could this slide be understood in 20 seconds?

Delete or merge weak slides.
