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

# Create figure exactly 512x512 px
plt.figure(figsize=(5.12, 5.12), dpi=100)

# Lineplot
sns.lineplot(data=df, x="Month", y="Revenue", hue="Segment", marker="o", palette="Set2")

# Titles and labels
plt.title("Monthly Revenue Trends by Customer Segment", fontsize=16)
plt.xlabel("Month")
plt.ylabel("Revenue ($)")

# Rotate x labels for readability
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save chart with exact size
plt.savefig("chart.png", dpi=100)
