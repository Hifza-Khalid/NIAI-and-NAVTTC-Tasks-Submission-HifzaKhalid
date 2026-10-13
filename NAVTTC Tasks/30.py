# NumPy Array Slicing

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Slice elements from index 1 to index 5
print(arr[1:5])


# Slice elements from index 4 to the end of the array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

# Slice elements from the beginning to index 4 (not included):

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

# Slice from the index 3 from the end to index 1 from the end:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])


# Return every other element from index 1 to index 5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

# Return every other element from the entire array:

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])


# From the second element, slice elements from index 1 to index 4 (not included):

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])


# From both elements, return index 2:

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 2])


# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])