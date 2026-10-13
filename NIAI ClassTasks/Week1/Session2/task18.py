#  Task 18 
#  Capstone: Combined Data Structures Challenge
# Background
# Real data science tasks require combining all the data structures you have learned. 
# This final task tests your ability to choose the right structure for each job.

#  Your Task
# You are given student records as a list of dictionaries:

# students = [
#     {"name": "Alice",   "scores": [85, 90, 78], "city": "Lahore"},
#     {"name": "Bob",     "scores": [60, 55, 70], "city": "Karachi"},
#     {"name": "Carol",   "scores": [92, 88, 95], "city": "Islamabad"},
#     {"name": "David",   "scores": [70, 65, 80], "city": "Lahore"},
#     {"name": "Eve",     "scores": [50, 45, 55], "city": "Karachi"},
#     {"name": "Frank",   "scores": [88, 92, 84], "city": "Islamabad"},
#     {"name": "Grace",   "scores": [75, 80, 78], "city": "Lahore"},
# ]
# Complete each of the following:

# Average score: Add a key "average" to each student dict containing the average of
#  their scores (round to 2 decimal places). Print all names and averages.

# Grade assignment: Using a dictionary comprehension, create a dict {name: grade} where grade is:

# "A" if average ≥ 85
# "B" if average ≥ 70
# "C" if average ≥ 55
# "F" otherwise
# Top students: Use a list comprehension to create a list of names of students with average ≥ 80.

# Unique cities: Use a set to find all unique cities, then print them.

# NumPy statistics: Convert all scores into a 2D NumPy array (shape 7×3). Compute and print:

# Overall mean, min, max
# Mean score per student (axis=1)
# Mean score per test/column (axis=0)
# Pandas summary: Create a DataFrame with columns Name, Average, Grade, City. 
# Print it, then print the average score per city using .groupby().

# 💡 Hints:

# sum(scores) / len(scores) or np.mean(scores) for averages
# np.array([s["scores"] for s in students]) to build the 2D array
# For the DataFrame, build a list of dicts or use parallel lists


import numpy as np
import pandas as pd

students = [
    {"name": "Alice",  "scores": [85, 90, 78], "city": "Lahore"},
    {"name": "Bob",    "scores": [60, 55, 70], "city": "Karachi"},
    {"name": "Carol",  "scores": [92, 88, 95], "city": "Islamabad"},
    {"name": "David",  "scores": [70, 65, 80], "city": "Lahore"},
    {"name": "Eve",    "scores": [50, 45, 55], "city": "Karachi"},
    {"name": "Frank",  "scores": [88, 92, 84], "city": "Islamabad"},
    {"name": "Grace",  "scores": [75, 80, 78], "city": "Lahore"},
]


# Step 1: Add "average" key to each student dict
for student in students:
    student["average"] = round(
        sum(student["scores"]) / len(student["scores"]), 2
    )

print("Names and Averages:")
for student in students:
    print(student["name"], ":", student["average"])


# Step 2: Dict comprehension {name: grade}
grades = {
    student["name"]:
        "A" if student["average"] >= 85
        else "B" if student["average"] >= 70
        else "C" if student["average"] >= 55
        else "F"
    for student in students
}

print("\nGrades:")
print(grades)


# Step 3: List of names with average >= 80
top_students = [
    student["name"]
    for student in students
    if student["average"] >= 80
]

print("\nTop Students:")
print(top_students)


# Step 4: Set of unique cities
unique_cities = {
    student["city"]
    for student in students
}

print("\nUnique Cities:")
print(unique_cities)


# Step 5: NumPy 2D array and statistics

# Convert all scores into a 2D NumPy array
scores_array = np.array([
    student["scores"]
    for student in students
])

print("\nScores Array:")
print(scores_array)

print("\nArray Shape:")
print(scores_array.shape)

# Overall mean
print("\nOverall Mean:")
print(np.mean(scores_array))

# Overall minimum
print("\nOverall Minimum:")
print(np.min(scores_array))

# Overall maximum
print("\nOverall Maximum:")
print(np.max(scores_array))

# Mean score per student (axis=1)
print("\nMean Score Per Student:")
print(np.mean(scores_array, axis=1))

# Mean score per test/column (axis=0)
print("\nMean Score Per Test:")
print(np.mean(scores_array, axis=0))


# Step 6: Pandas DataFrame and groupby city

# Create DataFrame
df = pd.DataFrame([
    {
        "Name": student["name"],
        "Average": student["average"],
        "Grade": grades[student["name"]],
        "City": student["city"]
    }
    for student in students
])

print("\nStudent DataFrame:")
print(df)

# Average score per city
print("\nAverage Score Per City:")
print(df.groupby("City")["Average"].mean())



# 1. What is the key difference between a list and a tuple? When would you prefer a tuple?
# Answer: A list is mutable, while a tuple is immutable. We prefer a tuple when data should not change.

# 2. What is the key difference between a list and a set? Give one real-world use case for each.
# Answer: A list is ordered and allows duplicates, while a set stores only unique values.
# List: storing student marks. Set: removing duplicate names.

# 3. Why can't a list be used as a dictionary key, but a tuple can?
# Answer: A list is mutable, so it cannot be a dictionary key. A tuple is immutable, so it can be used as a key.

# 4. In Task 15, what is the advantage of NumPy vectorisation over using a Python for loop?
# Answer: Vectorisation is faster and more efficient because it performs operations on entire arrays at once.

# 5. In Task 17, why do we use & instead of and when filtering a Pandas DataFrame?
# Answer: We use & for element-wise comparison between Pandas Series. 'and' does not work for Series conditions.

# 6. Looking at the Capstone (Task 18), which data structure did you find most useful? Why?
# Answer: Dictionaries were most useful because they store related data using clear key-value pairs.
# Students → List
# Stores multiple student records.
# Example: students = [student1, student2, ...]
# Each Student → Dictionary
# Stores related information using key: value.
# Example: {"name": "Alice", "scores": [85, 90, 78], "city": "Lahore"}
# Scores → List
# Stores multiple scores for each student.
# Example: [85, 90, 78]
# Average → Dictionary
# Add "average" as a new key.
# Example: student["average"] = 84.33
# Grades → Dictionary
# Maps student name to grade.
# Example: {"Alice": "B", "Carol": "A"}
# Top Students → List
# Stores names of students whose average is ≥ 80.
# Example: ["Alice", "Carol", "Frank"]
# Unique Cities → Set
# Best for removing duplicate cities.
# Example: {"Lahore", "Karachi", "Islamabad"}
# Scores for calculations → NumPy Array
# Best for numerical/statistical calculations.
# Example: np.array([[85, 90, 78], ...])
# Student table → Pandas DataFrame
# Best for tabular data and data analysis.
# Example: df = pd.DataFrame(...)
# Average by city → Pandas GroupBy
# Groups students by city and calculates their average.
# Example: df.groupby("City")["Average"].mean()