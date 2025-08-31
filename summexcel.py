import os
import pandas as pd
from pathlib import Path

Path("outputs").mkdir(exist_ok=True)
df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

# Monthly revenue trend
by_month = df.groupby(pd.Grouper(key="date", freq="M")).agg(revenue=("revenue","sum")).reset_index()

# Top products
top_products = df.groupby("product").agg(
    revenue=("revenue","sum"), qty=("quantity","sum")
).sort_values("revenue", ascending=False).reset_index()

# Regional breakdown
by_region = df.groupby("region").agg(
    revenue=("revenue","sum"), qty=("quantity","sum")
).reset_index()

with pd.ExcelWriter("outputs/summaries.xlsx", engine="openpyxl") as xw:
    df.head(200).to_excel(xw, sheet_name="SampleData", index=False)
    by_month.to_excel(xw, sheet_name="MonthlyRevenue", index=False)
    top_products.to_excel(xw, sheet_name="TopProducts", index=False)
    by_region.to_excel(xw, sheet_name="RegionalPerformance", index=False)

print("Wrote outputs/summaries.xlsx (MonthlyRevenue, TopProducts, RegionalPerformance)")
