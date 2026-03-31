import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\Dip_DMV_LAB\Dataset\cleaned_dataset.csv")

print(df.isnull().sum())

print("\nRows with Missing Values:\n")
print(df[df.isnull().any(axis=1)])

df_clean = df.dropna()


Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = ((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR)))

print("\nOutlier count per column:\n")
print(outliers.sum())

print("\nRows containing outliers:\n")
print(df[outliers.any(axis=1)])

plt.figure()
plt.bar(df_clean["YearsExperience"], df_clean["Salary"], color='blue')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Bar Chart: Experience vs Salary")
plt.show()

plt.figure()
plt.pie(df_clean["Salary"].head(5), labels=df_clean["YearsExperience"].head(5), autopct='%1.1f%%')
plt.title("Pie Chart (First 5 Records)")
plt.show()


plt.figure()
plt.step(df_clean["YearsExperience"], df_clean["Salary"], where='mid', color='green')
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Stair Chart: Experience vs Salary")
plt.show()