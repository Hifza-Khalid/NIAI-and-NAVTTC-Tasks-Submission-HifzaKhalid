# Task 12 — Set Operations
# Background
# A set is an unordered collection of unique elements. Duplicate values are automatically removed. Sets support mathematical operations: union (|), intersection (&), difference (-), symmetric difference (^).

# Operation	Symbol	Method	Meaning
# Union	|	.union()	All elements from both sets
# Intersection	&	.intersection()	Only elements in both
# Difference	-	.difference()	Elements in A but not B
# Symmetric Difference	^	.symmetric_difference()	Elements in either but not both
# 🎯 Your Task
# python_students = {"Alice", "Bob", "Carol", "David", "Eve"}
# java_students   = {"Bob", "David", "Frank", "Grace", "Alice"}


# Find students enrolled in both courses (intersection)
# Find students enrolled in at least one course (union)
# Find students taking Python but NOT Java (difference)
# Find students taking exactly one course (symmetric difference)
# Check if {"Bob", "Alice"} is a subset of python_students
# Add "Henry" to python_students and remove "Carol" from it
# Create a list [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] and use a set to print only the unique values
# 💡 Hint: Use .issubset() or the <= operator for subset check.


python_students = {"Alice", "Bob", "Carol", "David", "Eve"}
java_students   = {"Bob", "David", "Frank", "Grace", "Alice"}

# YOUR CODE HERE
# 1. Intersection
both = python_students & java_students
print("Both courses:", both)

# 2. Union
at_least_one = python_students | java_students
print("At least one course:", at_least_one)


# 3. Difference (Python but NOT Java)
python_only = python_students - java_students
print("Python but not Java:", python_only)


# 4. Symmetric difference
exactly_one = python_students ^ java_students
print("Exactly one course:", exactly_one)

# 5. Subset check: {"Bob", "Alice"} ⊆ python_students
check = {"Bob", "Alice"}.issubset(python_students)
print("Is subset:", check)

# 6. Add "Henry", remove "Carol"

python_students.add("Henry")
python_students.remove("Carol")

# 7. Unique values from list
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

unique_values = set(nums)

print("Unique values:", unique_values)