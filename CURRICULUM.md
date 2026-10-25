# Causal Inference Playbook — Learning Program

**Goal:** a hands-on command of the observational causal-inference toolkit, so
that an analysis can be described as "I used technique X, because the data
looked like Y" rather than "I ran a regression". Every technique is worked
through on real numbers.

**Starting point:** a Product Analyst background (B2C marketplace, B2B
security) and an A/B testing playbook. That playbook covers the cases where an
experiment can be run. This one covers the cases where it can't: the event
already happened, randomizing is unethical, too expensive or impossible.

**Scope boundary:** the causal foundations and the quasi-experiments that sit
next to A/B tests are covered in Modules 1 and 8 of the
[A/B Testing Playbook](https://github.com/omri-sabag83/A-B-Testing-Playbook).
Where a module here overlaps them, it recaps and links instead of rebuilding.

---

## Progress

`🟩⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜` **9% complete (1/11 modules)**

⬜ Not started · 🟨 In progress · 🟩 Completed

| # | Module | Data | Status | Completed On |
|---|--------|------|--------|---------------|
| 1 | Potential Outcomes Framework | NSW job training (shared) | 🟩 Completed | 2026-10-25 |
| 2 | DAGs: Confounders, Colliders, Mediators | NSW job training (shared) + simulation | ⬜ Not started | |
| 3 | Confounding & Regression Adjustment | NSW job training (shared) | ⬜ Not started | |
| 4 | Matching, incl. Propensity Score Matching | NSW job training (shared) | ⬜ Not started | |
| 5 | Weighting: IPW and Doubly Robust | NSW job training (shared) | ⬜ Not started | |
| 6 | Difference-in-Differences | NSW job training (shared) + castle-doctrine panel | ⬜ Not started | |
| 7 | Instrumental Variables | Card (1995) college proximity | ⬜ Not started | |
| 8 | Regression Discontinuity Design | Minimum legal drinking age | ⬜ Not started | |
| 9 | Synthetic Control | California Proposition 99 | ⬜ Not started | |
| 10 | Sensitivity, Placebo & Falsification Tests | Simulation + reused datasets | ⬜ Not started | |
| 11 | Capstone: Which Method When | All modules | ⬜ Not started | |

---

## How this program works

**One shared question for Modules 1–6:** *did the NSW (National Supported
Work) job-training program raise its participants' 1978 earnings?* NSW was a
real randomized experiment, so the true answer is known: treated minus control
mean 1978 earnings = $1,794.3. Each module then throws the randomized controls
away, uses a non-experimental comparison group from the PSID (Panel Study of
Income Dynamics) instead, and asks how close its technique gets back to
$1,794.3. The naive comparison against the PSID group gives (−$15,204.8).

**Fit-for-purpose data for Modules 7–9:** each of these techniques needs a
data shape a generic dataset does not have (a genuine instrument, a running
variable with a cutoff, one treated unit plus a pool of untreated ones), so
each uses a classic dataset built for it. Each module states the one-line
reason.

**Each module has:** concepts, why it matters, at least one worked example on
real numbers, and key takeaways. Findings are tagged Observation / Hypothesis
/ Conclusion.

---

## Modules

Each module's detail is set when it is built.

## <u>Module 1 — Potential Outcomes Framework</u>

**Overlap:** recap + pointer. The counterfactual idea and a confounded vs
randomized simulation are in
[A/B Testing Playbook, Module 1](https://github.com/omri-sabag83/A-B-Testing-Playbook/blob/main/01_foundations_causal_inference.ipynb).
This module adds the formal notation and puts real numbers on it.

**Concepts**
- Potential outcomes Y(1) and Y(0), the individual effect, and the
  fundamental problem: only one of the two is ever observed
- Estimands: ATE (average treatment effect), ATT (average treatment effect on
  the treated), ATC (average treatment effect on the controls), and why they
  differ when effects vary
- The decomposition: naive difference = ATT + selection bias, derived line by
  line
- Why randomization sets selection bias to zero on average
- Without randomization, two assumptions take its place:
  1. Unconfoundedness: men who looked the same before the program would have
     earned the same without it, whether they took it or not.
  2. Overlap: for every man who took the program, there are men who did not
     take it and who looked like him before.
- SUTVA (stable unit treatment value assumption): no interference, one version
  of the treatment

**Why it matters**
Every later module is a different way to estimate the one missing potential
outcome. Without this notation, "the effect" has no fixed meaning, and a
method's assumptions cannot be stated.

**Worked example**
1. A six-person table where both outcomes are known (chosen example): ATE,
   ATT, ATC and the decomposition computed exactly.
2. The NSW (National Supported Work) job-training data: the experiment
   estimates the ATT at $1,794.3. The naive comparison against the PSID
   (Panel Study of Income Dynamics) group gives (−$15,204.8). The difference,
   (−$16,999.1), is selection bias, estimated directly.
3. Overlap for the ATT: 14 PSID men share the profile of 82 treated men
   (zero 1975 earnings, unmarried, black).

**Resources**
- [Causal Inference: The Mixtape, ch. 4 "Potential Outcomes Causal Model"](https://mixtape.scunning.com/04-Potential_Outcomes_and_Randomization.html)
  (Scott Cunningham, ~45 min, verified): the notation, the decomposition and SUTVA.
- [The Effect, ch. 10 "Treatment Effects"](https://theeffectbook.net/ch-TreatmentEffects.html)
  (Nick Huntington-Klein, ~30 min, verified): ATE vs ATT and heterogeneous effects.
- [NSW data page](https://users.nber.org/~rdehejia/nswdata2.html) (Rajeev
  Dehejia, verified): the data source, its licence and the papers to cite.

**Exercise type:** redo the decomposition with the CPS (Current Population Survey,
a monthly US labour survey) comparison group.
Fully worked.

**Interview angle:** "Users who adopted feature X retain better. Did X cause
it?"
