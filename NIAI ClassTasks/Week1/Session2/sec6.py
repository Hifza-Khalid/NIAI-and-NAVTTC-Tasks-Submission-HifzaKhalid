# 🔢 Section 6 — NumPy Arrays
# 📝 Task 13 — Creating & Inspecting NumPy Arrays
# Background
# NumPy arrays are fixed-type, multi-dimensional arrays that support fast vectorised operations.
#  Unlike Python lists, every element must be the same type. Key creation functions: np.array(),
#  np.arange(), np.linspace(), np.zeros(), np.ones(), np.eye(), np.random.random().

# 🎯 Your Task
# Create each of the following arrays and print both the array and its .shape and .dtype:

# #	Function	Parameters	Expected shape
# 1	np.arange	0 to 20, step 2	(11,)
# 2	np.linspace	0 to 1, 6 evenly spaced points	(6,)
# 3	np.zeros	3 rows × 4 columns	(3, 4)
# 4	np.ones	2 rows × 5 columns, dtype int16	(2, 5)
# 5	np.eye	4×4 identity matrix	(4, 4)
# 6	np.random.randint	values 1–100, shape 3×3	(3, 3)
# 💡 Hint: np.ones((2,5), dtype='int16') creates an integer array of ones.
# np.random.randint(low, high, size=(r,c)) creates random integer arrays.

import numpy as np

# 1. arange: 0 to 20, step 2
arr1 = np.arange(0, 21, 2)

print("1. arange:")
print(arr1)
print("Shape:", arr1.shape)
print("Dtype:", arr1.dtype)


# 2. linspace: 0 to 1 with 6 evenly spaced points
arr2 = np.linspace(0, 1, 6)

print("\n2. linspace:")
print(arr2)
print("Shape:", arr2.shape)
print("Dtype:", arr2.dtype)


# 3. zeros: 3 rows × 4 columns
arr3 = np.zeros((3, 4))

print("\n3. zeros:")
print(arr3)
print("Shape:", arr3.shape)
print("Dtype:", arr3.dtype)


# 4. ones: 2 rows × 5 columns, dtype int16
arr4 = np.ones((2, 5), dtype="int16")

print("\n4. ones:")
print(arr4)
print("Shape:", arr4.shape)
print("Dtype:", arr4.dtype)


# 5. eye: 4 × 4 identity matrix
arr5 = np.eye(4)

print("\n5. eye:")
print(arr5)
print("Shape:", arr5.shape)
print("Dtype:", arr5.dtype)


# 6. Random integers from 1 to 100, shape 3 × 3
arr6 = np.random.randint(1, 101, size=(3, 3))

print("\n6. random integers:")
print(arr6)
print("Shape:", arr6.shape)
print("Dtype:", arr6.dtype)