
# Pandas DataFrames

# Create a simple Pandas DataFrame:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 


#refer to the row index:
print(df.loc[0])


df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 


#refer to the named index:
print(df.loc["day2"])


df = pd.read_csv('data.csv')

print(df) 