# Sales Analytics Dashboard 📊

## Overview
An interactive sales analysis using **Excel / Power BI**. This repo includes a script to generate sample data and an Excel file with summary sheets to mimic dashboard KPIs (revenue trends, top products, regional performance).

## Files
- `generate_sales_data.py` → creates `data/sales_data.csv`
- `summarize_to_excel.py` → generates `outputs/summaries.xlsx` with pivot-like sheets
- Use the CSV in **Power BI** to build a dashboard (optional).

## How to Run
```bash
pip install -r requirements.txt
python generate_sales_data.py
python summarize_to_excel.py
