# Corporate Credit Survival Analysis

> Survival models and machine learning for Korean corporate credit risk assessment

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![scikit-survival](https://img.shields.io/badge/scikit--survival-0.22+-orange?style=flat-square)](https://scikit-survival.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## Problem

Traditional credit scoring (logistic regression) treats default as a binary outcome, ignoring **time-to-event dynamics**. Korean SMEs exhibit distinct survival patterns driven by industry cycles, regional economic conditions, and chaebol supply-chain dependencies.

## Solution

A hybrid survival analysis framework:

1. **Kaplan-Meier** estimation for non-parametric survival curves by industry/region
2. **Cox Proportional Hazards** model with time-varying covariates
3. **Random Survival Forests** for non-linear risk factor interactions
4. **Spatial frailty model** incorporating regional economic heterogeneity

## Tech Stack

- **Survival Models:** lifelines, scikit-survival, PySAL (spatial frailty)
- **ML Pipeline:** scikit-learn, XGBoost, LightGBM
- **Data:** DART (전자공시), NICE/KCB credit data, KOSIS regional indicators
- **Visualization:** Matplotlib, Plotly (survival curves, hazard functions)

## Repository Structure

```
credit-survival-analysis/
├── src/
│   ├── data_loader.py          # DART API + credit bureau connectors
│   ├── feature_engineering.py  # Financial ratios, macro indicators
│   ├── survival_models.py      # KM, Cox PH, RSF implementations
│   ├── spatial_frailty.py      # Regional heterogeneity model
│   └── evaluation.py           # C-index, Brier score, calibration
├── notebooks/
│   ├── 01_eda_financial_ratios.ipynb
│   ├── 02_kaplan_meier_by_sector.ipynb
│   ├── 03_cox_model_selection.ipynb
│   └── 04_ml_survival_comparison.ipynb
├── data/
│   └── README.md
├── tests/
├── requirements.txt
└── LICENSE
```

## Quick Start

```bash
git clone https://github.com/DongsooJung/credit-survival-analysis.git
cd credit-survival-analysis
pip install -r requirements.txt
jupyter notebook notebooks/01_eda_financial_ratios.ipynb
```

## Model Comparison

| Model | C-index | Brier Score | AUC (1yr) | AUC (3yr) |
|-------|---------|-------------|-----------|-----------|
| Cox PH | — | — | — | — |
| Cox PH + Spatial Frailty | — | — | — | — |
| Random Survival Forest | — | — | — | — |
| XGBoost Survival | — | — | — | — |

*Results populated with anonymized test data.*

## References

- Hosmer, D.W., Lemeshow, S., & May, S. (2008). *Applied Survival Analysis*. Wiley.
- Ishwaran, H. et al. (2008). Random Survival Forests. *Annals of Applied Statistics*.

## License

MIT License

## Author

**Dongsoo Jung** — SNU Ph.D. Candidate · Spatial Econometrics & Financial Risk
