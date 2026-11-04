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

`🟩🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜` **82% complete (9/11 modules)**

⬜ Not started · 🟨 In progress · 🟩 Completed

| # | Module | Data | Status | Completed On |
|---|--------|------|--------|---------------|
| 1 | Potential Outcomes Framework | NSW job training (shared) | 🟩 Completed | 2026-10-25 |
| 2 | DAGs: Confounders, Colliders, Mediators | NSW job training (shared) + made-up numbers | 🟩 Completed | 2026-10-25 |
| 3 | Confounding & Regression Adjustment | NSW job training (shared) | 🟩 Completed | 2026-10-26 |
| 4 | Matching, incl. Propensity Score Matching | NSW job training (shared) | 🟩 Completed | 2026-10-27 |
| 5 | Weighting: IPW (Inverse Probability Weighting) and Doubly Robust | NSW job training (shared) | 🟩 Completed | 2026-10-27 |
| 6 | Difference-in-Differences | NSW job training (shared) + castle-doctrine panel | 🟩 Completed | 2026-11-01 |
| 7 | Instrumental Variables | Card (1995) college proximity | 🟩 Completed | 2026-11-03 |
| 8 | Regression Discontinuity Design | Minimum legal drinking age | 🟩 Completed | 2026-11-03 |
| 9 | Synthetic Control | California Proposition 99 | 🟩 Completed | 2026-11-04 |
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

## <u>Module 4 — Matching, incl. Propensity Score Matching</u>

**Concepts**
- Matching: for each treated man (a man who took the program in 1976–77),
  find his match: the comparison man who looked most like him before the
  program. His match's 1978 earnings stand in for his earnings without the
  program.
- The propensity score: among all the men, treated and comparison, with
  "before" columns like his, the share who were treated. It's computed from
  his columns alone, not from which group he's actually in. Matching on this one number instead of on all
  the columns is propensity score matching.
- Balance check: after matching, compare the mean of every "before" column
  for the treated men and for their matches.
- Overlap: matching only works for treated men who have comparison men with
  a similar score.

**Why it matters**
Matching uses only the comparison men chosen as matches, and the analyst can
see each match. So it shows plainly how alike the groups were made, and which
treated men had nobody like them.

**Worked example**
1. NSW (National Supported Work) job-training data vs the PSID (Panel Study
   of Income Dynamics) men: the score, the matches, the balance check and
   the effect estimate, with a 95% confidence interval.
2. Matching vs regression adjustment on the same data, and why they
   differ.

**Resources**
- [Causal Inference: The Mixtape, ch. 5 "Unconfoundedness"](https://mixtape.scunning.com/05-causal_cross_sectional_designs)
  (Scott Cunningham, ~60 min for sections 5.5–5.8, verified): exact
  matching, nearest-neighbour matching and the propensity score.
- [The Effect, ch. 14 "Matching"](https://theeffectbook.net/ch-Matching.html)
  (Nick Huntington-Klein, ~60 min, verified): matching, the propensity
  score, overlap and balance checks.

**Exercise type:** redo the propensity score matching with the CPS (Current
Population Survey, a monthly US labour survey) comparison group, and check
the matches. Fully worked.

**Interview angle:** "We matched users who used feature X to similar users
who didn't, using a propensity score. The matched users with X spend 10%
more. Is that the effect of X?"

## <u>Module 5 — Weighting: IPW (Inverse Probability Weighting) and Doubly Robust</u>

**Concepts**
- A man's propensity score, as in Module 4: take the men, treated and
  comparison, whose "before" columns are like his. His score is the share
  of treated men among them.
- IPW (inverse probability weighting) for the ATT (average treatment effect
  on the treated): every comparison man stays in, with a weight, (his score)
  ÷ (1 − his score): the number of treated men he stands in for. Each
  treated man counts once.
- The weighted mean of the comparison men's 1978 earnings (after the
  program) stands in for the
  treated men's mean without the program.
- Balance check: after weighting, compare the mean of every "before" column
  for the treated men and for the weighted comparison men. Also, how much of
  the weight a few men carry.
- Doubly robust uses two formulas:
  1. The score formula: the fitted formula that gives each man's
     propensity score.
  2. The earnings formula: regression adjustment's straight-line formula,
     fitted on the comparison men, which predicts each treated man's 1978
     earnings without the program (Module 3).

  The doubly robust estimate is regression adjustment's estimate minus
  the earnings formula's weighted mean miss (actual − predicted earnings)
  on the comparison men. It gets the right answer, apart from chance, if
  either formula is right.

**Why it matters**
Weighting keeps every comparison man. Unlike matching (Module 4), it
doesn't pair each treated man with one closest comparison man. It also
gives almost no weight to the comparison men unlike every treated man,
without a cut-off chosen by hand (such as "drop every comparison man below a
given score"). Doubly robust is right if
either of its two formulas is right, and its correction shows when the
earnings formula is wrong.

**Worked example**
1. NSW (National Supported Work) job-training data vs the PSID (Panel Study
   of Income Dynamics) men: the weights, where they go, the balance check
   and the effect estimate, with a 95% confidence interval.
2. Doubly robust on the same data, next to regression adjustment and
   weighting.

**Resources**
- [Causal Inference: The Mixtape, ch. 5 "Unconfoundedness"](https://mixtape.scunning.com/05-causal_cross_sectional_designs)
  (Scott Cunningham, ~30 min for section 5.8 "Estimation with Inverse
  Probability Weighting", verified): IPW on the same NSW data.
- [The Effect, ch. 14 "Matching"](https://theeffectbook.net/ch-Matching.html)
  (Nick Huntington-Klein, ~40 min for sections 14.5 and 14.7.2, verified):
  propensity score weighting, and doubly robust estimation.

**Exercise type:** redo weighting and doubly robust with the CPS (Current
Population Survey, a monthly US labour survey) comparison group. Fully
worked.

**Interview angle:** "Users who turned on feature X spend 10% more. We
weighted the users without X to look like the users with X, using a
propensity score, and the gap is still 10%. Is that the effect of X?"

## <u>Module 6 — Difference-in-Differences</u>

**Overlap with the A/B Testing Playbook:** the basic DiD idea is recapped
in this module, with a pointer to the Playbook's Module 8.
The basic two-group, two-period comparison on
made-up numbers with a known effect is in
[A/B Testing Playbook, Module 8, Part 2](https://github.com/omri-sabag83/A-B-Testing-Playbook/blob/main/08_quasi_experiments.ipynb).
This module adds real data, a check of the key assumption against a known
answer, DiD combined with weighting, and changes that start in different
years.

**Concepts**
- DiD (difference-in-differences): compare how much each group's mean
  outcome changed from before to after, not the outcome itself.
  DiD ATT (average treatment effect on the treated: the program's effect on
  the men who took it) = (treated men's mean change) − (comparison men's
  mean change).
- What DiD removes: a gap between the two groups' earnings that is the same
  size before the program and after the program. The gap is still there in
  each period, but DiD measures only how much the gap changed. The analyst
  doesn't need to know why the gap is there.
- Parallel trends: without the program, the treated men's mean earnings
  would have changed by the same number of dollars as the comparison men's.
- The before-program check: did the two groups' earnings change alike
  between two years before the program? Passing it doesn't prove
  parallel trends.
- DiD with weighting: DiD on comparison men given weights (Module 5), so that
  as a group they look like the treated men before the program.
- Changes that start in different years (staggered adoption): one DiD per
  start-year group against the groups that never changed, the event study
  (the per-group DiD, computed year by year), and the one-regression shortcut (a
  single regression with one column per state and one per year, the usual
  tool).

**Why it matters**
DiD is the usual tool when a change reaches some groups and not others,
and there is data from before and after the change. DiD removes a gap
between the groups that is the same size before and after, and the analyst
doesn't need to know why the gap is there. DiD rests on parallel trends,
which usually can't be checked directly after the change. So the analyst
has to know when parallel trends is likely to fail.

**Worked example**
1. NSW (National Supported Work) job-training data vs the PSID (Panel Study
   of Income Dynamics) men: DiD from 1975 to 1978, the before-program check,
   and a check of parallel trends against the applicants a lottery kept out
   of the program.
2. DiD with weighting on the same data, next to DiD and weighting alone.
3. Castle-doctrine laws (laws that remove the duty to retreat before using
   deadly force in self-defence outside the home), passed by 21 US states in
   different years (2005–2009): one DiD per group, an event study, and the one-regression
   shortcut.

**Resources**
- [Causal Inference: The Mixtape, ch. 9 "Difference-in-Differences"](https://mixtape.scunning.com/09-difference_in_differences)
  (Scott Cunningham, ~60 min for sections 9.2–9.5, verified): the basic
  DiD calculation, parallel trends, event studies, and the
  same castle-doctrine data.
- [The Effect, ch. 18 "Difference-in-Differences"](https://theeffectbook.net/ch-DifferenceinDifference.html)
  (Nick Huntington-Klein, ~60 min, verified): parallel trends, rollout
  designs with several start years (18.2.6, 18.3.1) and picking the
  comparison group by matching: pairing each treated unit with the most
  similar untreated one, as in Module 4 (18.3.2).

**Exercise type:** redo DiD, the before-program check, the lottery check and
DiD with weighting with the CPS (Current Population Survey, a monthly US labour
survey) comparison group. Fully worked.

**Interview angle:** "We launched feature X in the markets where spend had
dipped. Spend there rose 8% the next month, against 3% in the other
markets. Is X worth 5 points?"

## <u>Module 7 — Instrumental Variables</u>

**Concepts**
- Instrument: something that changes how much of a treatment people get, and
  affects the outcome only through that treatment. Here, the treatment is
  schooling, the outcome is pay, and the instrument is living near a college.
- The schooling rule: the instrument must change how much schooling men get.
  The data can check this rule.
- The no-other-way rule: the instrument must affect pay only through schooling.
  The data can look for other routes, but can't prove this rule.
- 2SLS (two-stage least squares): two regressions that give one pay number for
  a year of schooling. 2SLS estimate = (pay gap) ÷ (schooling gap), both between
  men with the instrument and men without the instrument.
- The F-statistic: how many standard errors the schooling gap is above 0,
  squared. The usual pass mark is 10.
- Which men the 2SLS estimate describes: only men who stay in school longer when a
  college is close, assuming a close college never shortens schooling.

**Why it matters**
Comparing men with more and less schooling mixes the effect of schooling with
the effect of ability, and the data measures ability only in part. An instrument
gives a number without an ability column. The price is a rule that can't be
proved, an interval wider than the plain regression's, and a 2SLS estimate that
describes only some men.

**Worked example**
Data from David Card's 1995 study: 3,010 US men in 1976, with living near a
four-year college in 1966 as the instrument. A regression of pay on
schooling, the instrument's calculation, 2SLS with the city column in both
regressions, the F-statistic, and a check of the no-other-way rule using region.

**Resources**
- [Causal Inference: The Mixtape, ch. 7 "Instrumental Variables"](https://mixtape.scunning.com/07-instrumental_variables)
  (Scott Cunningham, ~120 min, verified): two-stage least squares (7.3), weak
  instruments (7.4), and which people the number describes (7.5).
- [The Effect, ch. 19 "Instrumental Variables"](https://theeffectbook.net/ch-InstrumentalVariables.html)
  (Nick Huntington-Klein, ~60 min, verified): the two rules (19.1.2) and how
  2SLS is run (19.2).

**Exercise type:** redo 2SLS with a different instrument from the same data,
living near a two-year college. Fully worked.

**Interview angle:** "We can't force users to adopt feature X, but we randomly
sent half of them an email promoting feature X. The email group spent $2 more
per user, and 10 percentage points more of the email group used feature X. What
does feature X add to spend?"

## <u>Module 8 — Regression Discontinuity Design</u>

**Concepts**
- Cutoff: the value of a column at which a rule switches on for everyone.
  Here, the column is age and the cutoff is 21, the minimum legal drinking age
  in the US.
- RDD (regression discontinuity design): a regression line on each side of the
  cutoff. The jump = (line above the cutoff) − (line below the cutoff), both
  read at the cutoff. The jump is the effect of the rule.
- The no-other-change rule: nothing else that affects the outcome may change at
  the cutoff. The data can look for other changes, but can't prove this rule.
- Bandwidth: how far from the cutoff the data reaches. A narrower bandwidth
  relies less on straight lines, and usually gives a wider confidence interval.
- Fake cutoffs: the same calculation at a value where no rule changes. A jump
  there that chance can't explain would mean the method finds jumps that
  aren't real.
- The density check: when people can choose their side of a cutoff, count the
  people just below and just above the cutoff. "Density" means how many people
  sit at each value. Many more people on one side than on the other shows that
  people chose.

**Why it matters**
Many rules switch on at a threshold: an age, a test score, an order size.
People just below and just above a threshold are alike, so a gap in the
outcome at the threshold comes from the rule. The price: the jump describes
only people near the cutoff, and the no-other-change rule can't be proved.

**Worked example**
US death rates by age, from 19 to 23, from a 2009 study by Christopher
Carpenter and Carlos Dobkin. The jump in deaths at 21, the jump's 95% confidence
interval, three bandwidths, fake cutoffs at 20 and 22, and deaths from disease
against deaths from outside causes.

**Resources**
- [Causal Inference: The Mixtape, ch. 6 "Regression Discontinuity"](https://mixtape.scunning.com/06-regression_discontinuity)
  (Scott Cunningham, ~90 min, verified): the method's rules (6.2), estimation
  and bandwidths (6.3), and the density check (6.4).
- [The Effect, ch. 20 "Regression Discontinuity"](https://theeffectbook.net/ch-RegressionDiscontinuity.html)
  (Nick Huntington-Klein, ~60 min, verified): RDD with a regression (20.2.1),
  fake cutoffs (20.2.3), the density check (20.2.4), and bandwidths (20.3.4).
- [A/B Testing Playbook, Module 8, Part 4](https://github.com/omri-sabag83/A-B-Testing-Playbook/blob/main/08_quasi_experiments.ipynb):
  a short version of the same idea on made-up data.

**Exercise type:** the jump at 21 in deaths from motor vehicle accidents.
Fully worked.

**Interview angle:** "Orders of $50 or more get free shipping. Did free
shipping make customers order again?"

## <u>Module 9 — Synthetic Control</u>

**Concepts**
- Treated state: the one state a law covers. Here, California and its tobacco
  law, Proposition 99.
- Donor states: states without such a law, from which the stand-in for the
  treated state is built. Here, 38 US states.
- Synthetic control: a weighted mean of the donor states' sales. The weights
  are 0 or more, add up to 1, and give the smallest gaps to the treated state's
  sales before the law. After the law, gap = (treated state's sales) −
  (synthetic control's sales) estimates the law's effect.
- Size of the gap before the law: one number for how close the synthetic
  control's sales stay to the treated state's sales before the law. A synthetic
  control that doesn't stay close before the law can't stand in for the
  treated state after the law.
- Placebo states: the same calculation for each donor state, as if that state
  had passed the law. Each state's ratio = (size of the gap after the law) ÷
  (size of the gap before the law). If the law did nothing, the treated state
  is one state among all of them, so the treated state's rank among all the
  ratios shows how likely chance alone is to produce a ratio that high.
- Leave-one-out: rebuild the synthetic control without each donor state that
  has a weight, one state at a time. The estimate shouldn't rest on one state.
- Fake law year: the same calculation with a law year at which nothing
  happened, fitted only on the years before that fake year. A large gap after
  the fake year would mean the method finds gaps that don't come from the law.

**Why it matters**
Many changes hit one unit only: a law in one state, a price change in one
country, a launch in one city. No similar unit is left untouched for a plain
comparison. Synthetic control builds the comparison from a mix of untouched
units. The price: with one treated unit, chance is judged only by ranking it
among the placebo units, and the number of units limits how small the chance
of a gap that large with no law can get.

**Worked example**
Cigarette sales per person in 39 US states, 1970–2000, from a 2010 study by
Alberto Abadie, Alexis Diamond and Jens Hainmueller. Synthetic California, its
fit before 1989, the gap from 1989 to 2000, placebo states, leave-one-out,
and a fake law year in 1980.

**Resources**
- [Causal Inference: The Mixtape, ch. 11 "Synthetic Control"](https://mixtape.scunning.com/11-synthetic_control)
  (Scott Cunningham, ~90 min for section 11.1, verified): the method
  ("Formalization"), the Proposition 99 example, and placebo states
  ("Inference with Synthetic Control").
- [The Effect, ch. 22 "A Gallery of Rogues: Other Methods"](https://theeffectbook.net/ch-TheEdge.html)
  (Nick Huntington-Klein, ~20 min for section 22.2.1 "Synthetic Control",
  verified): the method and placebo tests in short.
- [A/B Testing Playbook, Module 8, Part 2](https://github.com/omri-sabag83/A-B-Testing-Playbook/blob/main/08_quasi_experiments.ipynb):
  a shipping-fee change in 5 states compared with 5 similar states by
  difference-in-differences, on made-up numbers. Synthetic control replaces
  that comparison group when no group of untouched states moves like the
  treated one.

**Exercise type:** Virginia, a placebo state that ranked above California: its
gap by hand, and what a ranking of 39 states can show at best. Fully worked.

**Interview angle:** "A food-delivery app raised its delivery fee in one city
only. Did the fee cut orders in that city?"
