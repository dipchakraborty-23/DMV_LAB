import pandas as pd


df = pd.read_csv("dataset.csv")


print("Original Dataset:\n")
print(df)


print("\nMissing Value Locations:\n")
print(df.isnull())


print("\nMissing Values Count:\n")
print(df.isnull().sum())


missing_rows = df[df.isnull().any(axis=1)]
print("\nRows with Missing Values:\n")
print(missing_rows)


df_filled = df.fillna(df.mean(numeric_only=True))

print("\nDataset After Filling Missing Values:\n")
print(df_filled)


df_filled.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_dataset.csv'")