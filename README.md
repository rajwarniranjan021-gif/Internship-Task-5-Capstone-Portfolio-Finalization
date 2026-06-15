# 📊 Data Analytics Internship Portfolio
### ApexPlanet Software Pvt. Ltd. — 60-Day Internship

![ApexPlanet](https://img.shields.io/badge/ApexPlanet-Internship-4361ee?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas)
![SQL](https://img.shields.io/badge/SQL-SQLite-003B57?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Completed-2dc653?style=for-the-badge)

---

## 🗂️ Internship Overview

This repository consolidates all deliverables from the **60-Day Data Analytics Internship** at
**ApexPlanet Software Pvt. Ltd.** The internship followed a structured 5-task curriculum covering
the complete data analytics lifecycle — from raw data ingestion to business storytelling and portfolio.

| # | Task | Focus Area | Duration |
|---|------|-----------|----------|
| 1 | Data Immersion & Wrangling | Cleaning, transformation, feature engineering | 10 days |
| 2 | EDA & Business Intelligence | Statistics, SQL queries, KPI mock-up | 14 days |
| 3 | Deep-Dive & Dashboarding | Cohort & RFM analysis, interactive HTML dashboard | 12 days |
| 4 | Storytelling & Statistical Validation | Hypothesis tests, presentation slides | 16 days |
| 5 | Capstone & Portfolio | Master repo, GitHub Pages site, reflections | 8 days |

---

## 📁 Repository Structure

```
Portfolio/
├── Task1_Data_Immersion/
│   ├── generate_dataset.py          # Synthetic dataset generator
│   ├── data_cleaning.py             # Cleaning & transformation script
│   ├── raw_sales_data.csv           # Raw dataset (1025 rows, intentional issues)
│   ├── cleaned_sales_data.csv       # Analysis-ready dataset (1001 rows, 26 cols)
│   └── task1_data_quality_report.png
│
├── Task2_EDA_BI/
│   ├── eda_analysis.py              # Full EDA + SQL + KPI mock-up
│   ├── business_queries.sql         # 7 business SQL queries
│   ├── eda_report.txt               # Written EDA findings
│   ├── task2_eda_report.png         # 9-panel EDA visualisation
│   └── task2_kpi_dashboard_mockup.png
│
├── Task3_Deep_Dive_Dashboard/
│   ├── deep_dive_analysis.py        # Cohort + RFM + HTML dashboard generator
│   ├── interactive_dashboard.html   # 🌐 Live interactive Chart.js dashboard
│   ├── rfm_segments.csv             # RFM scored customer table
│   ├── deep_dive_report.txt
│   └── task3_deep_dive.png
│
├── Task4_Storytelling_Stats/
│   ├── data_storytelling.py         # Hypothesis tests + 5-slide presentation
│   ├── slide1_executive_summary.png
│   ├── slide2_revenue_story.png
│   ├── slide3_customer_intelligence.png
│   ├── slide4_hypothesis_tests.png
│   ├── slide5_recommendations.png
│   └── hypothesis_testing_summary.txt
│
├── Task5_Capstone_Portfolio/
│   ├── portfolio.py                 # This file
│   ├── index.html                   # 🌐 GitHub Pages portfolio site
│   └── README.md                    # Master readme (this file)
│
└── run_all_tasks.sh                 # One-click script to run everything
```

---

## 🛠️ Technical Skills Demonstrated

| Category | Tools & Technologies |
|----------|---------------------|
| **Data Wrangling** | Python, Pandas, NumPy — missing value imputation, outlier capping, date standardisation, deduplication |
| **SQL** | SQLite via Python — aggregation, window functions, multi-condition filters, CTEs |
| **Visualisation** | Matplotlib, Seaborn — histograms, heatmaps, scatter plots, box plots, pie charts |
| **Statistics** | SciPy — T-test (independent), One-way ANOVA, Chi-squared test, 95% confidence intervals |
| **BI Dashboarding** | Chart.js (HTML/JS) — interactive line, bar, doughnut, polar charts with KPI cards |
| **Feature Engineering** | Customer age, age groups, revenue tiers, RFM scores, cohort periods, quarterly flags |
| **Segmentation** | RFM scoring (Recency, Frequency, Monetary), cohort retention analysis |
| **Storytelling** | Data narrative structure, presentation slide design, executive summaries |

---

## 📊 Key Findings

1. **Revenue** totals ₹{total_rev_placeholder} across 1,001 transactions from 2 years of data.
2. **Electronics** is the top-revenue category; **Sports** shows strong growth.
3. **Millennials and Gen X** represent the highest-value customer segments.
4. **Paid Search** delivers the highest average revenue per lead.
5. **RFM Segmentation** revealed that Champions (top tier) generate 3× the revenue of At-Risk customers.
6. **Cohort Analysis** shows average Month-1 retention of ~40%, indicating re-engagement opportunity.
7. **Hypothesis Testing** confirmed discounted orders differ significantly in revenue (p < 0.05).
8. Payment method choice is **independent of region** (Chi² p > 0.05).

---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scipy faker

# Run all tasks sequentially
bash run_all_tasks.sh

# Or run individual tasks
python3 Task1_Data_Immersion/generate_dataset.py
python3 Task1_Data_Immersion/data_cleaning.py
python3 Task2_EDA_BI/eda_analysis.py
python3 Task3_Deep_Dive_Dashboard/deep_dive_analysis.py
python3 Task4_Storytelling_Stats/data_storytelling.py
```

---

## 🌐 Live Portfolio

Open `Task5_Capstone_Portfolio/index.html` in any browser to view the interactive portfolio site.

---

## 📬 Contact

- **Company**: ApexPlanet Software Pvt. Ltd.
- **Website**: [www.apexplanet.in](https://www.apexplanet.in)
- **Email**: apexplanetgaya@gmail.com
- **Phone**: +91 99058 79870

---

*Completed as part of the 60-Day Data Analytics Internship Program — ApexPlanet Software Pvt. Ltd.*
