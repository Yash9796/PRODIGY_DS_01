"""
Task 01 - Data Visualization
Prodigy InfoTech Data Science Internship
"""

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("titanic.csv")

print("Dataset Loaded Successfully\n")

# -------------------------------
# Bar Chart - Gender Distribution
# -------------------------------

gender_counts = df['Sex'].value_counts()

plt.figure(figsize=(6,5))
plt.bar(gender_counts.index, gender_counts.values)
plt.title("Gender Distribution of Passengers")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# Histogram - Age Distribution
# -------------------------------

plt.figure(figsize=(6,5))
plt.hist(df['Age'].dropna(), bins=20)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

print("Task 01 Completed Successfully ✅")
