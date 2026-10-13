# Pandas - Analyzing DataFrames

import pandas as pd

df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataFrame Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())