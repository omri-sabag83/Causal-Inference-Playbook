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
