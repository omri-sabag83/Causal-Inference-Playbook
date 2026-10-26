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

`🟩🟩🟩⬜⬜⬜⬜⬜⬜⬜⬜` **27% complete (3/11 modules)**

⬜ Not started · 🟨 In progress · 🟩 Completed

| # | Module | Data | Status | Completed On |
|---|--------|------|--------|---------------|
| 1 | Potential Outcomes Framework | NSW job training (shared) | 🟩 Completed | 2026-10-25 |
| 2 | DAGs: Confounders, Colliders, Mediators | NSW job training (shared) + made-up numbers | 🟩 Completed | 2026-10-25 |
| 3 | Confounding & Regression Adjustment | NSW job training (shared) | 🟩 Completed | 2026-10-26 |
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

## <u>Module 2 — DAGs: Confounders, Colliders, Mediators</u>

**Concepts**
- A DAG (directed acyclic graph): a drawing of what causes what. Arrows point
  from cause to effect, and following the arrows never leads back to where
  you started.
- Three shapes:
  1. Confounder: one thing affects both who gets the treatment and the outcome.
  2. Mediator: the treatment works through it.
  3. Collider: both the treatment and the outcome affect it.
- Adjusting for a column: comparing like with like on it (only men with the
  same value are compared). Good and bad controls (columns to adjust for or
  not): adjust for confounders. Don't adjust for a mediator when you want the
  whole effect, and never for a collider or anything the treatment changed.
- An unmeasured confounder: a box in the drawing with no column in the data.

**Why it matters**
"Adjust for everything" is wrong advice. Adjusting for the wrong column can
create an effect that isn't there, or hide one that is. The drawing decides
which columns to adjust for, before any number is computed.

**Worked example**
1. Three small examples on made-up numbers with a known true effect, one
   per shape: adjusting helps for the confounder and hurts for the mediator
   and the collider.
2. NSW (National Supported Work) job-training data vs the PSID (Panel Study
   of Income Dynamics) survey men, real data: adjusting for more and more
   confounders moves the naive gap (a plain comparison of the two groups),
   (−$15,204.8), toward the experiment's $1,794.3,
   until the groups get too small to go further.
3. A bad control on the real experiment: keeping only the men who had a job
   in 1978 shrinks $1,794.3 to $1,340.8.

**Resources**
- [Causal Inference: The Mixtape, ch. 3 "Directed Acyclic Graphs"](https://mixtape.scunning.com/03-Directed_Acyclical_Graphs.html)
  (Scott Cunningham, ~45 min, verified): drawing DAGs, confounders, colliders.
- [The Effect, ch. 8 "Causal Paths and Closing Back Doors"](https://theeffectbook.net/ch-CausalPaths.html)
  (Nick Huntington-Klein, ~40 min, verified): which columns to adjust for,
  colliders.
- [A Crash Course in Good and Bad Controls](https://ftp.cs.ucla.edu/pub/stat_ser/r493.pdf)
  (Cinelli, Forney & Pearl, ~45 min, verified): which columns to adjust for,
  case by case.

**Exercise type:** which single column removes the most bias, and is a column
measured during the program a good control? Fully worked.

**Interview angle:** "Should we control for the number of sessions last week
when measuring the effect of feature X?"

## <u>Module 3 — Confounding & Regression Adjustment</u>

**Concepts**
- Regression: a formula, fitted to data, that predicts one column (1978
  earnings) from other columns. Each column gets a coefficient: how much the
  prediction moves when that column goes up by 1 and the others stay the same.
- Regression adjustment for the ATT (average treatment effect on the
  treated), in three steps:
  1. Fit the formula on the comparison men only, who never took the program.
  2. Use it to predict each treated man's 1978 earnings without the program.
  3. The effect estimate is the mean of (actual with the program − predicted without it) over the treated men.
- The common shortcut: one regression on all men, with "took the program"
  as one more column.
- What regression assumes: every confounder has a column, and the formula's
  shape is right.
- Extrapolation: where no comparison man looks like a treated man, the
  formula still gives a prediction, by continuing its shape past the data.
  Nothing in the data checks that guess.

**Why it matters**
Splitting men into groups runs out of men after a few columns. Regression
uses every column at once, which is why it's the default tool. But it always
returns a number, even where the groups don't overlap, so the analyst has to
check where its answer comes from.

**Worked example**
1. Seven men on made-up numbers: the three steps by hand, and how the answer
   changes when the formula's guess beyond the data is wrong.
2. NSW (National Supported Work) job-training data vs the PSID (Panel Study
   of Income Dynamics) men: regression adjustment with all 8 "before"
   columns, with a 95% confidence interval.
3. The same 8 columns in four reasonable formula shapes, a check of each
   shape on the PSID men who look most like the treated men, and a direct
   test on the men kept out by the lottery.

**Resources**
- [Causal Inference: The Mixtape, ch. 5 "Unconfoundedness"](https://mixtape.scunning.com/05-causal_cross_sectional_designs)
  (Scott Cunningham, ~45 min for sections 5.9–5.10, verified): regression
  adjustment, and the same NSW data.
- [The Effect, ch. 13 "Regression"](https://theeffectbook.net/ch-StatisticalAdjustment.html)
  (Nick Huntington-Klein, ~60 min, verified): what a coefficient means, and
  adjusting for columns with regression.

**Exercise type:** redo the regression adjustment with the CPS (Current
Population Survey, a monthly US labour survey) comparison group, in two
shapes, and check each shape. Fully worked.

**Interview angle:** "Our regression says users with feature X are 5 points
more likely to keep using the app, with controls. Is that the effect of X?"
