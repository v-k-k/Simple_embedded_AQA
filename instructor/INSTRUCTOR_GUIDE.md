# Instructor Manual — Webinar 8
## Master Test Plan and Portfolio Defense

This is the final webinar of the course. Its goal is not to introduce another testing technique,
but to bring together all previous work into a single engineering story:

Product → Risks → Strategy → Tests → Evidence → Findings → Decision.

---

# 0. Instructor Preparation

Before the session, it is recommended to have examples of artifacts 
from previous webinars readily available:
- Wokwi firmware/lab;
- Serial logs;
- protocol trace;
- Pytest output;
- Watchdog/recovery evidence;
- Network Stress Test;
- Memory Stability Log.

Open:
- `MASTER_TEST_PLAN_TEMPLATE.md`
- `FINAL_TEST_MATRIX.md`
- `EVIDENCE_INDEX.md`
- `CASE_STUDY_TEMPLATE.md`

Do not start the session by filling out the template.
Start with the question: **what decision should QA help make?**

---

# 1. What We Created During the Course

Show students the collection of artifacts from previous webinars. 
Ask: “If I simply put all of this into GitHub, would it already be a strong portfolio?” 
Expected answer: no. 
Explanation: individual test cases, logs, screenshots, and scripts do not demonstrate 
engineering reasoning if there is no connection between them. 
On the board: Artifacts ≠ Portfolio 
 
--- 
 
# 2. What a Tech Lead Wants to See 
 
Build the following chain: 
Product ↓ Risk ↓ Test Strategy ↓ Evidence ↓ Finding ↓ Decision 
Explain: a tech lead evaluates not only whether a person knows Pytest, but also whether 
they can identify a risk and justify a testing decision. 
 
--- 
 
# 3. From Test Case to Strategy 

Take a familiar scenario: `hang → WDT reset → recovery`. 
A Test Case answers: how to verify the scenario. 
A Strategy answers: - why it is important; - where to test it; - at what level; - what evidence 
is required; - when this test becomes part of regression; - what result blocks the release. 

---

# 4. Master Test Plan

Open master_test_plan/MASTER_TEST_PLAN_TEMPLATE.md.
Do not read all the headings one by one. Explain the Master Test Plan as a map:
Product + Risks + Methods + Environment + Evidence + Acceptance.
Main idea: The Master Test Plan should not be a large document for the sake of having a document.

---

# 5. System Overview

Open case_study/SYSTEM_OVERVIEW.md. 

The student should be able to explain in 1-2 minutes:
- what the device is;
- inputs;
- outputs;
- interfaces;
- dependencies;
- critical data;
- critical actuators.

Question:
«What could realistically harm the user or break the product behavior here?»

This is where risks begin.

---

# 6. Scope / Out of Scope

Give an example:

IN SCOPE:
- firmware logic;
- UART;
- protocol behavior;
- recovery;
- network state machine;
- automation.

OUT OF SCOPE in the simulation:
- real RF performance;
- electrical brown-out threshold;
- EMI/EMC;
- real flash wear;
- temperature/environment qualification.

Explain:
Out of Scope — is not «we forgot».
It is a deliberate limitation of the strategy.

---

# 7. Risk-Based Testing

Ask students to identify 5 critical risks.

Do not accept: 
"test the button" as a risk.

Better: 
"due to bounce, a single physical press may trigger multiple actuator actions." 

Formula: 
Failure mode → Impact. 

Then add probability/priority.

---

# 8. Test Matrix

Open test_matrix/FINAL_TEST_MATRIX.md.

Show how a single row connects: 
Risk → Level → Test → Environment → Expected → Evidence → Regression. 

Give students 5-10 minutes to complete 2 of their own rows.

Then review one strong example and one weak example.

---

# 9. Test Levels

Explain using a single risk: 

For example, network loss:
- component: retry/backoff function;
- interface: MQTT/network behavior;
- system: node offline/recovery;
- regression: automated reconnect scenario.

Not every risk requires testing at all levels.

---

# 10. Test Environment

Build the table:

Wokwi → logic/state/fault injection
PulseView/analyzer → protocol evidence
Python/Pytest → repeatable regression
Real hardware → electrical/physical reality
 
Key question:
"What can this environment prove, and what can it not prove?"

---

# 11. Entry Criteria

Ask: 
"When does it make sense to start testing at all?" 

Examples:
- build is available;
- requirements/version are known;
- environment is ready;
- critical interfaces are available;
- logging is sufficient. 

Entry Criteria should protect the team from meaningless testing of an unstable baseline.

---

# 12. Exit Criteria

Poor Exit Criterion: "Everything has been tested."

Good examples:
- 100% critical tests executed;
- 0 open Critical defects;
- recovery scenarios PASS;
- regression PASS;
- required evidence collected.

Exit Criteria should enable decision-making.

---

# 13. Evidence

Open `evidence/EVIDENCE_INDEX.md`.

Show examples:
- a Wokwi screenshot by itself is weak;
- a timestamped Serial log is stronger for state transitions;
- a protocol trace is strong evidence for I2C/SPI;
- a pytest report is strong evidence for repeatable regression;
- a memory trend is stronger than a single heap value. 

Key point: 
Evidence should be selected to support the claim.

---

# 14. Evidence → Decision

On the board:

Evidence
↓
Finding
↓
Impact
↓
Residual Risk
↓
Decision

Ask: 
"We have 98% of tests PASS. Can we release?" 

Correct answer: 
without context, we don't know. 

The remaining 2% may be cosmetic or safety-critical.

---

# 15. Regression Strategy

Open Test Matrix.

Ask students to mark Regression? for critical scenarios.

Explain: regression is not "run everything." 

After a network stack change:
- reconnect;
- buffer;
- duplicates;
- memory stability;
may have a higher priority than unrelated UI/input tests.

---

# 16. Evidence Package

Ask students to select the 5 strongest evidence items from the entire course.

For each one: 
1. What is the claim?
2. What is the risk?
3. Why is this evidence sufficient?
4. Can another person verify it?

---

# 17. Portfolio Case Study

Open `portfolio/CASE_STUDY_TEMPLATE.md`.

Explain the structure as a story:

Problem
→ System
→ Risks
→ Strategy
→ Execution
→ Evidence
→ Findings
→ Decision
→ Limitations.

This is far stronger than: 
"I worked with Wokwi, Python, MQTT, Pytest..."

---

# 18. GitHub README

Open `portfolio/README_TEMPLATE.md`.

The README should answer the following within 30-60 seconds:
- what it is;
- what problem it addresses;
- what exactly the QA did;
- what the main risks are;
- where the evidence is;
- what the conclusion is. 

Do not make a recruiter or tech lead open 20 files just to understand the project.

---

# 19. Poor vs Strong Portfolio 

Poor:
- screenshots without explanation;
- 50 test cases;
- scripts;
- “here is my Pytest”;
- no conclusion. 

Strong:
- engineering problem;
- risk prioritization;
- traceable strategy;
- evidence;
- findings;
- limitations;
- decision.

---

# 20. Release Decision

Open `templates/RELEASE_DECISION.md`.

Give the following case:
- all functional tests PASS;
- recovery after a WDT reset occasionally leaves the actuator ON.

Ask for a GO/NO-GO decision.

The student should justify the decision based on impact/risk, not on the pass percentage.

---

# 21. Career Brief 

Open `templates/INTERVIEW_BRIEF.md`.

Give the student 90 seconds.

Structure: 
Product → Risk → Strategy → Evidence → Finding → Decision. 

Stop them if the answer turns into a list of tools.

---

# 22. Tricky Questions 

Ask:

- Why is this test automated?
- Why is this test not automated?
- What can Wokwi not prove?
- Why do you consider this a firmware bug?
- What will be included in regression after the fix?
- Why is this defect Critical/Major?
- What residual risk remains? 

Evaluate reasoning, not "correct terminology"

---

# 23. Final Assignment 

The student creates:
1. Master Test Plan.
2. Final Test Matrix.
3. Evidence Index.
4. Portfolio README.
5. Case Study.
6. Release Decision.
7. A 5-7 minute defence presentation.

---

# 24. Defense Format: 5-7 minutes 

Recommended timing:

0:00–0:45 — Product/System
0:45–1:45 — Critical Risks
1:45–3:00 — Test Strategy
3:00–4:15 — Evidence + Findings
4:15–5:15 — Regression / Limitations
5:15–6:00 — Release Decision
6:00–7:00 — Questions

Do not allow students to spend 5 minutes demonstrating code.

---

# 25. Final Project Assessment

| Criterion | Weight |
|---|---:|
| System understanding | 10% |
| Scope / limitations | 10% |
| Risk prioritization | 15% |
| Test Strategy / Matrix | 20% |
| Evidence quality | 15% |
| Regression / Exit Criteria | 10% |
| Engineering conclusion | 10% |
| Portfolio defense | 10% |

---

# 26. Final Course Takeaway 

Return to:
Risk → Test → Evidence → Decision 

Explain:
A test case verifies a scenario. 
A Test Plan organizes testing activities. 
A Master Test Plan connects the product, risks, methods, evidence, and readiness criteria. 

QA work does not end with the word PASS or FAIL. 
It ends with sufficient information for an engineering decision. 

And a portfolio should show not what the student has learned, 
but how they solve an engineering problem.
