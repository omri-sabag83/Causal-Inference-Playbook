# Causal Inference Playbook

A hands-on playbook for estimating causal effects when you can't run an
experiment: DAGs (directed acyclic graphs), matching, DiD
(difference-in-differences), IV (instrumental variables), RDD (regression
discontinuity design), synthetic control, and how to validate the claim.
Every technique is worked through on real numbers.

The program, progress table and per-module detail are in
[CURRICULUM.md](CURRICULUM.md).

| # | Notebook | Topic | Data |
|---|----------|-------|------|
| 1 | `01_potential_outcomes.ipynb` | Potential outcomes, ATE / ATT / ATC, naive difference = effect + selection bias | NSW + PSID |
| 2 | `02_dags.ipynb` | DAGs: confounders, mediators, colliders, good and bad controls | Made-up numbers + NSW + PSID |
| 3 | `03_regression_adjustment.ipynb` | Regression adjustment for the ATT, formula shape, extrapolation | Made-up numbers + NSW + PSID + CPS |
| 4 | `04_matching.ipynb` | Propensity score matching, overlap, balance checks, matching vs regression | NSW + PSID + CPS |
| 5 | `05_weighting.ipynb` | Inverse probability weighting, where the weight goes, doubly robust | NSW + PSID + CPS |
| 6 | `06_difference_in_differences.ipynb` | DiD, parallel trends checked against the lottery, DiD with weighting, laws passed in different years | NSW + PSID + CPS + castle-doctrine state panel |
| 7 | `07_instrumental_variables.ipynb` | Instrumental variables, 2SLS, the F-statistic for instrument strength, the no-other-way rule | Card (1995) college proximity |
| 8 | `08_regression_discontinuity.ipynb` | Regression discontinuity, the jump at a cutoff, bandwidths, fake cutoffs, the no-other-change rule | Minimum legal drinking age (Carpenter and Dobkin, 2009) |
| 9 | `09_synthetic_control.ipynb` | Synthetic control, fit before the law, placebo states, leave-one-out, a fake law year | California Proposition 99 cigarette sales (Abadie, Diamond and Hainmueller, 2010) |
| 10 | `10_sensitivity_placebo_falsification.ipynb` | Checks that need no right answer: a placebo outcome, a stand-in group, the move from leaving out a column | NSW + PSID + CPS |

Related repos: [A/B Testing Playbook](https://github.com/omri-sabag83/A-B-Testing-Playbook),
[Product Analytics Playbook](https://github.com/omri-sabag83/Product-Analytics-Playbook),
[Scikit-Learn Playbook](https://github.com/omri-sabag83/Scikit-Learn-Playbook),
[Root-Cause Analysis Playbook](https://github.com/omri-sabag83/Root-Cause-Analysis-Playbook).

## Data

All data is public research data, downloaded at its source by
`data/get_data.py` and checked against fixed SHA-256 checksums. The licences
do not clearly allow redistribution, so **the files are not in this repo**.
The notebooks keep their outputs, so every number can be read without them.
Simulated data is generated in code with a fixed seed and always labelled as
simulated.

## Reproduce

```bash
conda activate base                 # tested env: Python 3.13.5, versions in requirements.txt
python data/get_data.py             # downloads and checksum-verifies the public datasets
jupyter nbconvert --to notebook --execute --inplace *.ipynb
```
