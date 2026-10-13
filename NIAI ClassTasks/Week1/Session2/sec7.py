# 📝 Task 16 — Creating & Exploring a DataFrame
# Background
# A DataFrame is a 2D table with labelled rows (index) and columns. You can create one from a dictionary, a list of lists, a CSV file, or from scikit-learn datasets. Essential inspection methods: .head(), .tail(), .info(), .describe(), .shape, .columns, .dtypes, .isnull().sum().

# 🎯 Your Task
# Part A — Create from a dictionary:

# data = {
#     "Name":    ["Ali", "Sara", "John", "Fatima", "Chris"],
#     "Age":     [23, 21, 25, 22, 24],
#     "Score":   [88, 92, 78, 95, 83],
#     "Passed":  [True, True, True, True, True],
#     "City":    ["Lahore", "Karachi", "London", "Islamabad", "New York"]
# }
# Create a DataFrame from this dictionary
# Print its shape, column names, and data types
# Print the first 3 rows and the last 2 rows
# Print summary statistics using .describe()
# Part B — Load the Iris dataset: 
# 5. Load the Iris dataset using load_iris() and add the species names 
# 6. Print how many rows belong to each species using .value_counts() 
# 7. Print the mean of each numerical column grouped by species

# 💡 Hint for Iris: iris_df['species'] = iris.target_names[iris.target] maps integer targets to names.
# 💡 Hint for groupby: iris_df.groupby('species').mean(numeric_only=True)

import pandas as pd
from sklearn.datasets import load_iris

# Part A
data = {
    "Name":   ["Ali", "Sara", "John", "Fatima", "Chris"],
    "Age":    [23, 21, 25, 22, 24],
    "Score":  [88, 92, 78, 95, 83],
    "Passed": [True, True, True, True, True],
    "City":   ["Lahore", "Karachi", "London", "Islamabad", "New York"]
}

import pandas as pd
from sklearn.datasets import load_iris

# Part A
data = {
    "Name":   ["Ali", "Sara", "John", "Fatima", "Chris"],
    "Age":    [23, 21, 25, 22, 24],
    "Score":  [88, 92, 78, 95, 83],
    "Passed": [True, True, True, True, True],
    "City":   ["Lahore", "Karachi", "London", "Islamabad", "New York"]
}

# 1. Create DataFrame
df = pd.DataFrame(data)

print("DataFrame:")
print(df)


# 2. Print shape, columns, dtypes
print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)


# 3. Print the first 3 rows and the last 2 rows
print("\nFirst 3 Rows:")
print(df.head(3))

print("\nLast 2 Rows:")
print(df.tail(2))


# 4. Print summary statistics using .describe()
print("\nSummary Statistics:")
print(df.describe())


# Part B — Iris

# 5. Load the Iris dataset and create DataFrame
iris = load_iris()

iris_df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Add species names
iris_df["species"] = iris.target_names[iris.target]

print("\nIris DataFrame:")
print(iris_df)


# 6. Print how many rows belong to each species using .value_counts()
print("\nNumber of Rows per Species:")
print(iris_df["species"].value_counts())


# 7. Print the mean of each numerical column grouped by species
print("\nMean of Numerical Columns per Species:")
print(iris_df.groupby("species").mean(numeric_only=True))

# 📝 Task 17 — Selecting, Filtering & Adding Columns
# Background
# Select columns: df['col'] (Series) or df[['col1','col2']] (DataFrame)
# Select rows by position: df.iloc[start:stop]
# Select rows by label/condition: df.loc[condition]
# Add a column: df['new_col'] = expression
# Multiple conditions: Use & (AND) or | (OR) — wrap each condition in ()
# 🎯 Your Task
# Use the Iris DataFrame from Task 16.

# Select and print only the sepal length (cm) and petal length (cm) columns (first 5 rows)
# Select rows 50 through 54 using .iloc
# Filter rows where species == 'versicolor' and print how many there are
# Filter rows where petal length (cm) > 5.0 AND species == 'virginica'
# Add a new column "petal_area" = petal length (cm) × petal width (cm) and print the first 5 rows
# Sort the DataFrame by petal_area in descending order and print the top 5 rows
# 💡 Hint: df[(df['col1'] > val) & (df['col2'] == 'label')] — always wrap each condition in ().
# 💡 Hint: df.sort_values('petal_area', ascending=False).head(5)

from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target_names[iris.target]


# 1. Select sepal length and petal length columns (head 5)
print("Sepal Length and Petal Length:")
print(iris_df[['sepal length (cm)', 'petal length (cm)']].head(5))


# 2. Select rows 50 through 54 using iloc
print("\nRows 50 through 54:")
print(iris_df.iloc[50:55])


# 3. Filter versicolor species, print count
versicolor = iris_df[iris_df['species'] == 'versicolor']

print("\nVersicolor Rows:")
print(versicolor)

print("\nNumber of Versicolor rows:")
print(len(versicolor))


# 4. Filter: petal length > 5.0 AND species == 'virginica'
filtered = iris_df[
    (iris_df['petal length (cm)'] > 5.0) &
    (iris_df['species'] == 'virginica')
]

print("\nVirginica with Petal Length > 5.0:")
print(filtered)


# 5. Add petal_area column, print head
iris_df['petal_area'] = (
    iris_df['petal length (cm)'] *
    iris_df['petal width (cm)']
)

print("\nDataFrame with Petal Area:")
print(iris_df.head(5))


# 6. Sort by petal_area descending, top 5
sorted_df = iris_df.sort_values(
    'petal_area',
    ascending=False
)

print("\nTop 5 Rows by Petal Area:")
print(sorted_df.head(5))



