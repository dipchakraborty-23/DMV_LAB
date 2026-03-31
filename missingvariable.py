import pandas as pd

df = pd.read_csv("D:\\D:\Dip_DMV_LAB\Dataset\\salary_dataset.csv")

print("--- Missing Values Before ---")
print(df.isnull().sum())

df = df.fillna(df.mean(numeric_only=True))

print("\n--- Cleaned Data ---")
print(df.to_string())

