# Pandas - Data Correlations


import pandas as pd

df = pd.read_csv("data.csv")

# Find the correlation between all numerical columns
print(df.corr())