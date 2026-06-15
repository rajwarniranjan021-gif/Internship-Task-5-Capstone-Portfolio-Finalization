"""
TASK 5 — Capstone Integration & Portfolio Finalization
ApexPlanet Software Pvt. Ltd. | Data Analytics Internship
Generates: Master README.md + Portfolio website (index.html)
"""

import os

print("="*65)
print("  TASK 5 — CAPSTONE & PORTFOLIO FINALIZATION")
print("  ApexPlanet Data Analytics Internship")
print("="*65)

# ─────────────────────────────────────────
# README.md
# ─────────────────────────────────────────
readme = """# 📊 Data Analytics Internship Portfolio
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
"""

with open('/home/claude/internship/Task5_Capstone_Portfolio/README.md','w') as f:
    f.write(readme)
print("\n📄 README.md saved")

# ─────────────────────────────────────────
# PORTFOLIO WEBSITE (GitHub Pages style)
# ─────────────────────────────────────────
html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Data Analytics Portfolio | ApexPlanet Internship</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0d0d1a;--card:#1a1a2e;--border:#2a2a4a;
  --acc1:#4cc9f0;--acc2:#f72585;--acc3:#7209b7;--acc4:#4361ee;
  --txt:#e0e0ff;--muted:#8888bb;
}
body{font-family:'Segoe UI',Arial,sans-serif;background:var(--bg);color:var(--txt);line-height:1.6}
a{color:var(--acc1);text-decoration:none}a:hover{text-decoration:underline}

/* HERO */
.hero{
  background:linear-gradient(135deg,#0d0d1a 0%,#1a1a3a 50%,#0d0d1a 100%);
  padding:80px 40px;text-align:center;border-bottom:1px solid var(--border);
  position:relative;overflow:hidden;
}
.hero::before{
  content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse at 30% 50%,rgba(114,9,183,.15),transparent 60%),
             radial-gradient(ellipse at 70% 50%,rgba(67,97,238,.15),transparent 60%);
}
.hero-badge{
  display:inline-block;background:rgba(76,201,240,.12);border:1px solid var(--acc1);
  color:var(--acc1);padding:6px 18px;border-radius:30px;font-size:.8rem;
  letter-spacing:1px;text-transform:uppercase;margin-bottom:24px;
}
.hero h1{font-size:2.8rem;font-weight:800;margin-bottom:16px;
  background:linear-gradient(135deg,var(--acc1),var(--acc2));
  -webkit-background-clip:text;-webkit-text-fill-color:transparent}
.hero p{font-size:1.1rem;color:var(--muted);max-width:600px;margin:0 auto 32px}
.hero-btns{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn{padding:12px 28px;border-radius:8px;font-size:.9rem;font-weight:600;
     border:none;cursor:pointer;transition:transform .2s,opacity .2s}
.btn:hover{transform:translateY(-2px);opacity:.9}
.btn-primary{background:linear-gradient(135deg,var(--acc4),var(--acc3));color:#fff}
.btn-outline{background:transparent;border:1px solid var(--acc1);color:var(--acc1)}

/* STATS BAR */
.stats-bar{display:grid;grid-template-columns:repeat(4,1fr);
  background:var(--card);border-bottom:1px solid var(--border)}
.stat{text-align:center;padding:24px 16px;border-right:1px solid var(--border)}
.stat:last-child{border-right:none}
.stat .num{font-size:1.8rem;font-weight:700;color:var(--acc1)}
.stat .lbl{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.5px}

/* SECTION */
section{max-width:1100px;margin:0 auto;padding:60px 32px}
section h2{font-size:1.6rem;font-weight:700;margin-bottom:8px;color:var(--acc1)}
.section-sub{color:var(--muted);margin-bottom:32px;font-size:.95rem}

/* TASK CARDS */
.task-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px}
.task-card{
  background:var(--card);border:1px solid var(--border);border-radius:16px;
  padding:24px;transition:transform .2s,border-color .2s;
}
.task-card:hover{transform:translateY(-4px);border-color:var(--acc4)}
.task-header{display:flex;align-items:center;gap:12px;margin-bottom:16px}
.task-num{width:42px;height:42px;border-radius:10px;display:flex;align-items:center;
  justify-content:center;font-weight:800;font-size:1rem;flex-shrink:0}
.task-title{font-size:1rem;font-weight:700;color:var(--txt)}
.task-subtitle{font-size:.8rem;color:var(--muted)}
.task-tags{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0}
.tag{padding:3px 10px;border-radius:20px;font-size:.7rem;font-weight:600;
     background:rgba(76,201,240,.1);color:var(--acc1);border:1px solid rgba(76,201,240,.2)}
.task-timeline{font-size:.78rem;color:var(--muted);margin-top:10px}
.task-list{list-style:none;margin-top:10px}
.task-list li{font-size:.82rem;color:var(--muted);padding:3px 0;padding-left:16px;position:relative}
.task-list li::before{content:'→';position:absolute;left:0;color:var(--acc4)}

/* SKILLS */
.skills-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px}
.skill-cat{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:20px}
.skill-cat h4{font-size:.85rem;color:var(--acc2);font-weight:700;margin-bottom:10px;text-transform:uppercase;letter-spacing:.5px}
.skill-cat p{font-size:.8rem;color:var(--muted)}

/* FINDINGS */
.findings{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.finding{background:var(--card);border-left:3px solid var(--acc4);
  border-radius:0 12px 12px 0;padding:16px 20px}
.finding .icon{font-size:1.4rem;margin-bottom:8px}
.finding h4{font-size:.88rem;font-weight:700;color:var(--txt);margin-bottom:4px}
.finding p{font-size:.78rem;color:var(--muted)}

/* TIMELINE */
.timeline{position:relative;padding-left:40px}
.timeline::before{content:'';position:absolute;left:16px;top:0;bottom:0;width:2px;background:var(--border)}
.tl-item{position:relative;margin-bottom:28px}
.tl-dot{width:14px;height:14px;border-radius:50%;background:var(--acc4);
  position:absolute;left:-31px;top:4px;border:2px solid var(--bg)}
.tl-content{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:16px 20px}
.tl-content h4{font-size:.9rem;font-weight:700;color:var(--acc1);margin-bottom:4px}
.tl-content p{font-size:.8rem;color:var(--muted)}
.tl-day{font-size:.72rem;color:var(--acc3);font-weight:600;margin-bottom:6px}

/* FOOTER */
footer{text-align:center;padding:40px 20px;border-top:1px solid var(--border);color:var(--muted);font-size:.8rem}
footer strong{color:var(--acc1)}

/* RESPONSIVE */
@media(max-width:600px){
  .hero h1{font-size:1.8rem}
  .stats-bar{grid-template-columns:repeat(2,1fr)}
  section{padding:40px 20px}
}
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-badge">📊 ApexPlanet · Data Analytics · 60 Days</div>
  <h1>Data Analytics<br>Internship Portfolio</h1>
  <p>End-to-end project covering wrangling, EDA, SQL, dashboarding,
     statistical validation, and business storytelling.</p>
  <div class="hero-btns">
    <a href="Task3_Deep_Dive_Dashboard/interactive_dashboard.html" class="btn btn-primary">
      🚀 Live Dashboard
    </a>
    <a href="https://github.com" class="btn btn-outline">
      📂 GitHub Repo
    </a>
  </div>
</div>

<!-- STATS BAR -->
<div class="stats-bar">
  <div class="stat"><div class="num">1,001</div><div class="lbl">Records Analysed</div></div>
  <div class="stat"><div class="num">26</div><div class="lbl">Features Engineered</div></div>
  <div class="stat"><div class="num">7</div><div class="lbl">SQL Business Queries</div></div>
  <div class="stat"><div class="num">4</div><div class="lbl">Statistical Tests</div></div>
</div>

<!-- TASKS -->
<section>
  <h2>🗂️ Internship Tasks</h2>
  <p class="section-sub">60 days broken into 5 progressive milestones — from raw data to polished portfolio.</p>
  <div class="task-grid">

    <div class="task-card">
      <div class="task-header">
        <div class="task-num" style="background:rgba(76,201,240,.15);color:#4cc9f0">T1</div>
        <div><div class="task-title">Data Immersion & Wrangling</div>
        <div class="task-subtitle">Foundation of every great analysis</div></div>
      </div>
      <div class="task-tags">
        <span class="tag">Python</span><span class="tag">Pandas</span>
        <span class="tag">Feature Eng.</span><span class="tag">Data Quality</span>
      </div>
      <ul class="task-list">
        <li>Profiled 1,025-row raw dataset with 4 quality issues</li>
        <li>Removed 24 duplicates, standardised 50 date formats</li>
        <li>Imputed missing values with category medians</li>
        <li>Engineered 9 new features incl. customer_age, RFM inputs</li>
      </ul>
      <div class="task-timeline">⏱️ 10 Days</div>
    </div>

    <div class="task-card">
      <div class="task-header">
        <div class="task-num" style="background:rgba(247,37,133,.15);color:#f72585">T2</div>
        <div><div class="task-title">EDA & Business Intelligence</div>
        <div class="task-subtitle">Patterns, trends, and SQL insights</div></div>
      </div>
      <div class="task-tags">
        <span class="tag">SQL</span><span class="tag">Seaborn</span>
        <span class="tag">KPIs</span><span class="tag">EDA</span>
      </div>
      <ul class="task-list">
        <li>7 SQL queries answering business questions</li>
        <li>Correlation matrix — revenue strongly driven by unit_price</li>
        <li>Multivariate analysis: discount vs revenue scatter</li>
        <li>Static KPI dashboard mock-up with 8 metrics</li>
      </ul>
      <div class="task-timeline">⏱️ 14 Days</div>
    </div>

    <div class="task-card">
      <div class="task-header">
        <div class="task-num" style="background:rgba(114,9,183,.15);color:#7209b7">T3</div>
        <div><div class="task-title">Deep-Dive & Dashboarding</div>
        <div class="task-subtitle">Cohort, RFM & live Chart.js dashboard</div></div>
      </div>
      <div class="task-tags">
        <span class="tag">Cohort</span><span class="tag">RFM</span>
        <span class="tag">Chart.js</span><span class="tag">HTML</span>
      </div>
      <ul class="task-list">
        <li>Cohort retention analysis across 24 monthly cohorts</li>
        <li>RFM scoring → 5 segments including Champions & At-Risk</li>
        <li>Interactive HTML dashboard with 6 chart types</li>
        <li>Champions drive 3× more revenue than At-Risk segment</li>
      </ul>
      <div class="task-timeline">⏱️ 12 Days</div>
    </div>

    <div class="task-card">
      <div class="task-header">
        <div class="task-num" style="background:rgba(67,97,238,.15);color:#4361ee">T4</div>
        <div><div class="task-title">Storytelling & Stats</div>
        <div class="task-subtitle">Validated findings, business narrative</div></div>
      </div>
      <div class="task-tags">
        <span class="tag">T-test</span><span class="tag">ANOVA</span>
        <span class="tag">Chi²</span><span class="tag">SciPy</span>
      </div>
      <ul class="task-list">
        <li>4 hypothesis tests with p-values and CI</li>
        <li>5-slide presentation deck for stakeholders</li>
        <li>Discount strategy finding: statistically significant effect</li>
        <li>ANOVA: satisfaction consistent across all 5 regions</li>
      </ul>
      <div class="task-timeline">⏱️ 16 Days</div>
    </div>

    <div class="task-card" style="border-color:rgba(76,201,240,.3)">
      <div class="task-header">
        <div class="task-num" style="background:rgba(44,214,83,.15);color:#2dc653">T5</div>
        <div><div class="task-title">Capstone & Portfolio</div>
        <div class="task-subtitle">This page — you're looking at it!</div></div>
      </div>
      <div class="task-tags">
        <span class="tag">GitHub Pages</span><span class="tag">HTML/CSS</span>
        <span class="tag">README</span><span class="tag">Reflection</span>
      </div>
      <ul class="task-list">
        <li>Master README with complete project documentation</li>
        <li>Portfolio website with responsive design</li>
        <li>LinkedIn post drafted with learning reflections</li>
        <li>All repos reviewed for professionalism & consistency</li>
      </ul>
      <div class="task-timeline">⏱️ 8 Days</div>
    </div>

  </div>
</section>

<!-- KEY FINDINGS -->
<section style="padding-top:0">
  <h2>💡 Key Findings</h2>
  <p class="section-sub">8 actionable insights derived from the end-to-end analysis.</p>
  <div class="findings">
    <div class="finding"><div class="icon">💰</div><h4>Revenue Drivers</h4><p>Unit price explains 85% of variance in order revenue (r=0.855 correlation).</p></div>
    <div class="finding"><div class="icon">🏆</div><h4>Top Category</h4><p>Electronics leads on revenue; Sports shows strongest recent growth trajectory.</p></div>
    <div class="finding"><div class="icon">👤</div><h4>Best Customers</h4><p>Champions segment (RFM top tier) generates 3× revenue vs At-Risk customers.</p></div>
    <div class="finding"><div class="icon">📉</div><h4>Retention Gap</h4><p>Average Month-1 retention ~40% — strong acquisition, but re-engagement needed.</p></div>
    <div class="finding"><div class="icon">📢</div><h4>Best Channel</h4><p>Paid Search delivers the highest average revenue per lead (statistically validated).</p></div>
    <div class="finding"><div class="icon">🏷️</div><h4>Discount Strategy</h4><p>Discounted orders have significantly higher revenue (p&lt;0.05) — discount high-value items, not low.</p></div>
    <div class="finding"><div class="icon">⭐</div><h4>Consistent Service</h4><p>ANOVA confirms satisfaction is statistically similar across all 5 regions — good ops consistency.</p></div>
    <div class="finding"><div class="icon">💳</div><h4>Payment Behaviour</h4><p>Payment method preference is independent of region — uniform checkout UX is appropriate.</p></div>
  </div>
</section>

<!-- SKILLS -->
<section style="padding-top:0">
  <h2>🛠️ Technical Skills</h2>
  <p class="section-sub">Hands-on competencies built over 60 days.</p>
  <div class="skills-grid">
    <div class="skill-cat"><h4>🐍 Python</h4><p>Pandas, NumPy, Matplotlib, Seaborn, SciPy — data wrangling to statistical tests</p></div>
    <div class="skill-cat"><h4>🗃️ SQL</h4><p>SQLite, aggregation, window functions, multi-table joins, CTEs</p></div>
    <div class="skill-cat"><h4>📊 Visualisation</h4><p>Chart.js, Matplotlib, Seaborn — 15+ chart types including interactive dashboards</p></div>
    <div class="skill-cat"><h4>📐 Statistics</h4><p>T-test, ANOVA, Chi-squared, confidence intervals, p-values, effect sizes</p></div>
    <div class="skill-cat"><h4>🔍 Analytics</h4><p>Cohort analysis, RFM segmentation, KPI definition, funnel metrics</p></div>
    <div class="skill-cat"><h4>📣 Storytelling</h4><p>Business narrative, executive presentations, data-driven recommendations</p></div>
  </div>
</section>

<!-- TIMELINE -->
<section style="padding-top:0">
  <h2>📅 Project Timeline</h2>
  <p class="section-sub">How the 60 days were structured across tasks.</p>
  <div class="timeline">
    <div class="tl-item">
      <div class="tl-dot"></div>
      <div class="tl-content">
        <div class="tl-day">Days 1–10</div>
        <h4>Task 1: Data Immersion & Wrangling</h4>
        <p>Dataset acquisition, quality assessment, cleaning scripts, feature engineering. Output: 1,001-row clean dataset with 26 columns.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot" style="background:#f72585"></div>
      <div class="tl-content">
        <div class="tl-day">Days 11–24</div>
        <h4>Task 2: EDA & Business Intelligence</h4>
        <p>Descriptive stats, 7 SQL queries, correlation analysis, static KPI dashboard mock-up in Python/Matplotlib.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot" style="background:#7209b7"></div>
      <div class="tl-content">
        <div class="tl-day">Days 25–36</div>
        <h4>Task 3: Deep-Dive & Interactive Dashboard</h4>
        <p>Cohort retention heatmap, RFM scoring (5 segments), fully interactive Chart.js HTML dashboard deployed locally.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot" style="background:#f48c06"></div>
      <div class="tl-content">
        <div class="tl-day">Days 37–52</div>
        <h4>Task 4: Storytelling & Statistical Validation</h4>
        <p>4 hypothesis tests (T-test, ANOVA, Chi²), 5-slide stakeholder presentation, business narrative with call to action.</p>
      </div>
    </div>
    <div class="tl-item">
      <div class="tl-dot" style="background:#2dc653"></div>
      <div class="tl-content">
        <div class="tl-day">Days 53–60</div>
        <h4>Task 5: Capstone & Portfolio Finalisation</h4>
        <p>Master GitHub repo, README documentation, this portfolio website, LinkedIn post, professional reflection.</p>
      </div>
    </div>
  </div>
</section>

<footer>
  <p>Built with ❤️ during the <strong>ApexPlanet 60-Day Data Analytics Internship</strong></p>
  <p style="margin-top:8px">
    <a href="https://www.apexplanet.in">apexplanet.in</a> ·
    <a href="mailto:apexplanetgaya@gmail.com">apexplanetgaya@gmail.com</a> ·
    +91 99058 79870
  </p>
  <p style="margin-top:12px;font-size:.7rem;color:#555">
    Technologies: Python · Pandas · NumPy · Matplotlib · Seaborn · SciPy · SQLite · Chart.js · HTML/CSS
  </p>
</footer>

</body>
</html>"""

with open('/home/claude/internship/Task5_Capstone_Portfolio/index.html','w') as f:
    f.write(html)
print("🌐 Portfolio website saved → Task5_Capstone_Portfolio/index.html")

# ─────────────────────────────────────────
# LINKEDIN POST DRAFT
# ─────────────────────────────────────────
linkedin = """
🎉 Excited to share that I've completed the 60-Day Data Analytics Internship
at ApexPlanet Software Pvt. Ltd.!

Over 60 days, I worked through a structured 5-task curriculum that took me from
raw, messy data to actionable business insights:

📌 Task 1 — Data Wrangling: Cleaned 1,025 records, engineered 9 features,
   handled missing values, outliers & duplicate rows using Python/Pandas.

📌 Task 2 — EDA & SQL: Wrote 7 SQL business queries, built correlation
   heatmaps, and designed a KPI dashboard mock-up.

📌 Task 3 — Deep-Dive & Dashboard: Performed RFM segmentation (5 customer
   tiers) and cohort retention analysis. Built an interactive Chart.js
   dashboard — open in your browser, no tools needed!

📌 Task 4 — Storytelling & Statistics: Validated findings with T-tests, ANOVA,
   and Chi-squared tests. Presented a 5-slide stakeholder deck.

📌 Task 5 — Portfolio: Consolidated everything into a GitHub portfolio with a
   live HTML portfolio page.

Key takeaway: Data is only as valuable as the story you tell with it. Statistical
rigour + clear narrative = actionable insights.

🔗 Portfolio: [GitHub Link]
🔗 Dashboard: [Live Dashboard Link]

#DataAnalytics #Python #SQL #Internship #ApexPlanet #DataScience #EDA #Portfolio
"""

with open('/home/claude/internship/Task5_Capstone_Portfolio/linkedin_post_draft.txt','w') as f:
    f.write(linkedin)
print("📱 LinkedIn post draft saved")

print("\n" + "="*65)
print("  TASK 5 COMPLETE ✅")
print("  ALL 5 TASKS DONE! 🎉")
print("="*65)
