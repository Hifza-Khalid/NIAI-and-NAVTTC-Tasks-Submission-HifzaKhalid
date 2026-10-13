# 📝 Task 14 , Array Indexing, Slicing & Reshaping
# Background
# NumPy arrays use row, column indexing: A[row, col] or A[row][col].
# Slicing: A[r1:r2, c1:c2] extracts a sub-array.
# .reshape(rows, cols) changes the shape without changing the data.
# .T gives the transpose.

# 🎯 Your Task
# A = np.arange(1, 26).reshape(5, 5)
# This creates:

# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]
# Print the element at row 2, column 3 (value: 14)
# Print the entire third row (index 2): [11 12 13 14 15]
# Print the entire second column (index 1): [ 2 7 12 17 22]
# Extract the top-left 3×3 sub-matrix: rows 0–2, columns 0–2
# Extract the bottom-right 2×2 sub-matrix: last 2 rows and last 2 cols
# Print the transpose of A (shape should become (5,5) but rows/cols swapped)
# Reshape A into a 1D array of 25 elements, then into a shape (25, 1) column vector
# 💡 Hint: A[:3, :3] extracts the top-left corner. A[-2:, -2:] grabs the bottom-right corner.


import numpy as np

A = np.arange(1, 26).reshape(5, 5)

print("Original matrix A:")
print(A)
print()


# 1. Element at row 2, col 3
# Indexing starts from 0, so row 2 and column 3 gives 14
print("1. Element at row 2, col 3:")
print(A[2, 3])


# 2. Entire third row (index 2)
print("\n2. Third row:")

print(A[2, :])


# 3. Entire second column (index 1)
print("\n3. Second column:")
print(A[:, 1])


# 4. Top-left 3x3 sub-matrix
print("\n4. Top-left 3x3:")
print(A[:3, :3])


# 5. Bottom-right 2x2 sub-matrix
print("\n5. Bottom-right 2x2:")
print(A[-2:, -2:])


# 6. Transpose
print("\n6. Transpose:")
print(A.T)


# 7. Reshape to 1D (25,) then to column vector (25, 1)

# Convert A into a 1D array
A_1D = A.reshape(25)

print("\n7. 1D array:")
print(A_1D)
print("Shape:", A_1D.shape)

# Convert 1D array into a column vector
A_column = A_1D.reshape(25, 1)

print("\nColumn vector:")
print(A_column)
print("Shape:", A_column.shape)