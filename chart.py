# chart.py
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic monthly revenue data
np.random.seed(42)
months = pd.date_range(start="2023-01-01", periods=12, freq="M")
segments = ["Retail", "Online", "Wholesale"]

data = []
for segment in segments:
    base = np.linspace(100, 200, 12)  # seasonal growth
    noise = np.random.normal(0, 10, 12)  # variation
    revenue = base + noise + np.random.randint(0, 50)
    data.extend(zip(months, [segment]*12, revenue))

df = pd.DataFrame(data, columns=["Month", "Segment", "Revenue"])

# Professional Seaborn style
sns.set_style("whitegrid")
sns.set_context("talk")

# Create figure 512x512 px → (8,8) inches at 64 dpi
plt.figure(figsize=(8, 8), dpi=64)

# Lineplot
sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", palette="Set2")

# Titles and labels
plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Revenue ($)")

# Rotate x labels for readability
plt.xticks(rotation=45)

# Save chart
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
