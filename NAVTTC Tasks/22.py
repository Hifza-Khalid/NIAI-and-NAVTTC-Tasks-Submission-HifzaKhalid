# Python Tuples
# Tuple is similar to a list, but its elements cannot be changed.

# Creating a tuple
my_tuple = ()

# Tuple with integers
my_tuple = (1, 2, 3)

# Tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)

# Nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# Tuple packing
my_tuple = 3, 4.6, "dog"

# Tuple unpacking
a, b, c = my_tuple

# Tuple with one element
single_tuple = ("hello",)

# Accessing tuple elements
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

print(my_tuple[0])
print(my_tuple[5])

# Negative indexing
print(my_tuple[-1])
print(my_tuple[-6])

# Slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

# Nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

print(n_tuple[0][3])
print(n_tuple[1][1])
print(n_tuple[2][0])

# Tuple concatenation
print((1, 2, 3) + (4, 5, 6))

# Tuple repetition
print(("Repeat",) * 3)

# Tuple methods
my_tuple = ('a', 'p', 'p', 'l', 'e')

print(my_tuple.count('p'))
print(my_tuple.index('l'))

# Membership test
print('a' in my_tuple)
print('b' in my_tuple)
print('g' not in my_tuple)

# Iterating through a tuple
for name in ('John', 'Kate'):
    print("Hello", name)

# Built-in functions
numbers = (1, 2, 3, 4, 5)

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Sorted:", sorted(numbers))