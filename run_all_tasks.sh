#!/bin/bash
# ─────────────────────────────────────────────────────────────
#  run_all_tasks.sh
#  ApexPlanet Data Analytics Internship — One-click runner
#  Runs all 5 tasks in sequence
# ─────────────────────────────────────────────────────────────

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "======================================================"
echo "  ApexPlanet Data Analytics Internship"
echo "  Running all 5 tasks..."
echo "======================================================"

echo ""
echo "📦 Installing dependencies..."
pip install pandas numpy matplotlib seaborn scipy faker --break-system-packages -q

echo ""
echo "─── TASK 1: Data Immersion & Wrangling ─────────────"
python3 "$SCRIPT_DIR/Task1_Data_Immersion/generate_dataset.py"
python3 "$SCRIPT_DIR/Task1_Data_Immersion/data_cleaning.py"

echo ""
echo "─── TASK 2: EDA & Business Intelligence ────────────"
python3 "$SCRIPT_DIR/Task2_EDA_BI/eda_analysis.py"

echo ""
echo "─── TASK 3: Deep-Dive & Dashboarding ───────────────"
python3 "$SCRIPT_DIR/Task3_Deep_Dive_Dashboard/deep_dive_analysis.py"

echo ""
echo "─── TASK 4: Storytelling & Statistics ──────────────"
python3 "$SCRIPT_DIR/Task4_Storytelling_Stats/data_storytelling.py"

echo ""
echo "─── TASK 5: Capstone & Portfolio ───────────────────"
python3 "$SCRIPT_DIR/Task5_Capstone_Portfolio/portfolio.py"

echo ""
echo "======================================================"
echo "  ✅ ALL 5 TASKS COMPLETED SUCCESSFULLY!"
echo ""
echo "  📂 Key outputs:"
echo "     cleaned_sales_data.csv            (Task 1)"
echo "     task2_eda_report.png              (Task 2)"
echo "     interactive_dashboard.html        (Task 3)"
echo "     slide1_executive_summary.png      (Task 4)"
echo "     Task5_Capstone_Portfolio/index.html (Task 5)"
echo ""
echo "  🌐 Open the dashboard:"
echo "     open Task3_Deep_Dive_Dashboard/interactive_dashboard.html"
echo "  🌐 Open the portfolio:"
echo "     open Task5_Capstone_Portfolio/index.html"
echo "======================================================"
