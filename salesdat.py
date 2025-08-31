import os, random
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

os.makedirs("data", exist_ok=True)

regions = ["North", "South", "East", "West"]
products = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]

start = datetime(2024, 1, 1)
rows = []
for i in range(365):
    date = start + timedelta(days=i)
    for _ in range(random.randint(5, 20)):
        region = random.choice(regions)
        product = random.choice(products)
        qty = random.randint(1, 8)
        price = random.choice([199, 249, 299, 349, 399])
        rows.append({"date": date.date(), "region": region, "product": product,
                     "quantity": qty, "unit_price": price, "revenue": qty * price})

df = pd.DataFrame(rows)
df.to_csv("data/sales_data.csv", index=False)
print("Wrote data/sales_data.csv with", len(df), "rows")
