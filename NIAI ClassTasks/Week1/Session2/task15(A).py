# 📝 Task 15 — Vectorised Operations & Broadcasting
# Background
# NumPy operations are applied element-wise to entire arrays without writing loops — this is called vectorisation. When arrays have compatible shapes, NumPy can broadcast smaller arrays across larger ones automatically.

# 🎯 Your Task
# Part A — Element-wise Operations:

# a = np.array([10, 20, 30, 40, 50])
# b = np.array([ 1,  2,  3,  4,  5])
# Compute and print (without loops):

# a + b, a - b, a * b, a / b
# Square root of a (use np.sqrt)
# All elements of a greater than 25 (Boolean mask)
# Use the Boolean mask to extract only elements of a greater than 25
# Part B — Matrix Operations:

# M = np.array([[1, 2], [3, 4]])
# N = np.array([[5, 6], [7, 8]])
# Element-wise multiplication M * N
# Matrix (dot) product M @ N or np.dot(M, N)
# Sum of all elements, sum along each row, sum along each column
# 💡 Hint for Boolean masking: mask = a > 25 creates [False False False True True]. Then a[mask] extracts [40 50].
# 💡 Hint for axis sums: M.sum(axis=1) sums each row; M.sum(axis=0) sums each column.

import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([1, 2, 3, 4, 5])


# Part A — Element-wise Operations

# 1. Element-wise +, -, *, /
print("1. Addition:")
print(a + b)

print("\nSubtraction:")
print(a - b)

print("\nMultiplication:")
print(a * b)

print("\nDivision:")
print(a / b)


# 2. Square root of a
print("\n2. Square root of a:")
print(np.sqrt(a))


# 3. Boolean mask: elements of a > 25
mask = a > 25

print("\n3. Boolean mask:")
print(mask)


# 4. Extract elements > 25 using mask
print("\n4. Elements greater than 25:")
print(a[mask])


# Part B — Matrix Operations

M = np.array([[1, 2], [3, 4]])
N = np.array([[5, 6], [7, 8]])


# 5. Element-wise multiplication
print("\n5. Element-wise multiplication:")
print(M * N)


# 6. Matrix dot product
print("\n6. Matrix dot product:")
print(M @ N)


# 7. Total sum, row sums, column sums

print("\n7. Total sum:")
print(M.sum())

print("\nRow sums:")
print(M.sum(axis=1))

print("\nColumn sums:")
print(M.sum(axis=0))