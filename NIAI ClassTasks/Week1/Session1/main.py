

# ============================================================
# PYTHON BASICS — DATA STRUCTURES
# ============================================================
#
# Topics:
# 1. Numbers
# 2. Booleans
# 3. Strings
# 4. Containers
# 5. Lists
# 6. Slicing
# 7. Loops
# 8. List Comprehensions
# 9. Dictionaries
# 10. Dictionary Loops
# 11. Dictionary Comprehensions
# 12. Sets
# 13. Set Loops
# 14. Set Comprehensions
# 15. Functions
# 16. Optional Keyword Arguments
# 17. Lambda Functions
# 18. Classes
# 19. Constructors
# 20. Instance Variables
# 21. Instance Methods
# 22. Tasks Q1–Q17


# ============================================================
# BASIC DATA TYPES
# ============================================================

# ------------------------------------------------------------
# NUMBERS
# ------------------------------------------------------------

x = 3

print(type(x))       # <class 'int'>
print(x)             # 3

print(x + 1)         # Addition → 4
print(x - 1)         # Subtraction → 2
print(x * 2)         # Multiplication → 6
print(x ** 2)        # Exponentiation → 9

x += 1
print(x)             # 4

x *= 2
print(x)             # 8


# Floats

y = 2.5

print(type(y))       # <class 'float'>
print(y)             # 2.5
print(y + 1)         # 3.5
print(y * 2)         # 5.0
print(y ** 2)        # 6.25


# Python does NOT support x++ or x--
# Use x += 1 and x -= 1 instead.

# x++       # Invalid in Python
# x--       # Invalid in Python


# ------------------------------------------------------------
# BOOLEANS
# ------------------------------------------------------------

t = True
f = False

print(type(t))       # <class 'bool'>

# AND → both conditions must be True
print(t and f)       # False

# OR → at least one condition must be True
print(t or f)        # True

# NOT → reverses the Boolean value
print(not t)         # False

# != checks whether two values are different
print(t != f)        # True


# Python logical operators:
#
# AND → and
# OR  → or
# NOT → not
#
# Other languages may use:
#
# && → AND
# || → OR
# !  → NOT


# ------------------------------------------------------------
# STRINGS
# ------------------------------------------------------------

hello = 'hello'
world = "world"

print(hello)
print(world)

print(len(hello))    # Length → 5

# String concatenation
hw = hello + ' ' + world
print(hw)            # hello world

# String formatting
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12)          # hello world 12


# ------------------------------------------------------------
# STRING METHODS
# ------------------------------------------------------------

s = "hello"

# Capitalize first character
print(s.capitalize())
# Hello

# Convert to uppercase
print(s.upper())
# HELLO

# Right justify
print(s.rjust(7))
#   hello

# Center
print(s.center(7))
#  hello

# Replace characters
print(s.replace('l', '(ell)'))
# he(ell)(ell)o

# Remove leading and trailing whitespace
print('  world '.strip())
# world


# ============================================================
# CONTAINERS
# ============================================================
#
# Python has four important built-in containers:
#
# List       → [1, 2, 3]
# Tuple      → (1, 2, 3)
# Dictionary → {'name': 'Hifza'}
# Set        → {1, 2, 3}
#
# ------------------------------------------------------------
# LISTS
# ------------------------------------------------------------

xs = [3, 1, 2]

print(xs)            # [3, 1, 2]
print(xs[2])         # 2

# Negative indexing
print(xs[-1])        # 2

# Lists are mutable
xs[2] = 'foo'
print(xs)
# [3, 1, 'foo']

# Add element to the end
xs.append('bar')
print(xs)
# [3, 1, 'foo', 'bar']

# Remove and return last element
x = xs.pop()

print(x)
# bar

print(xs)
# [3, 1, 'foo']


# ------------------------------------------------------------
# LIST SLICING
# ------------------------------------------------------------

nums = list(range(5))

print(nums)
# [0, 1, 2, 3, 4]

# Index 2 to index 4 (4 is excluded)
print(nums[2:4])
# [2, 3]

# Index 2 to the end
print(nums[2:])
# [2, 3, 4]

# Beginning to index 2 (2 is excluded)
print(nums[:2])
# [0, 1]

# Entire list
print(nums[:])
# [0, 1, 2, 3, 4]

# Beginning to the last element
print(nums[:-1])
# [0, 1, 2, 3]

# Slice assignment
nums[2:4] = [8, 9]

print(nums)
# [0, 1, 8, 9, 4]


# ============================================================
# LOOPS
# ============================================================

animals = ['cat', 'dog', 'monkey']

for animal in animals:
    print(animal)

# Output:
# cat
# dog
# monkey


# ============================================================
# LIST COMPREHENSIONS
# ============================================================

# Normal approach

nums = [0, 1, 2, 3, 4]

squares = []

for x in nums:
    squares.append(x ** 2)

print(squares)
# [0, 1, 4, 9, 16]


# Using list comprehension

nums = [0, 1, 2, 3, 4]

squares = [x ** 2 for x in nums]

print(squares)
# [0, 1, 4, 9, 16]


# List comprehension with condition

nums = [0, 1, 2, 3, 4]

even_squares = [
    x ** 2
    for x in nums
    if x % 2 == 0
]

print(even_squares)
# [0, 4, 16]


# ============================================================
# DICTIONARIES
# ============================================================

# A dictionary stores key-value pairs.

d = {
    'cat': 'cute',
    'dog': 'furry'
}

# Access value using key
print(d['cat'])
# cute

# Check if key exists
print('cat' in d)
# True

# Add a new key-value pair
d['fish'] = 'wet'

print(d['fish'])
# wet

# Accessing a missing key directly causes KeyError
# print(d['monkey'])

# get() allows us to provide a default value
print(d.get('monkey', 'N/A'))
# N/A

print(d.get('fish', 'N/A'))
# wet

# Delete an item
del d['fish']

print(d.get('fish', 'N/A'))
# N/A


# ============================================================
# DICTIONARY LOOPS
# ============================================================

d = {
    'person': 2,
    'cat': 4,
    'spider': 8
}

# Loop through dictionary keys

for animal in d:

    legs = d[animal]

    print(
        'A %s has %d legs'
        % (animal, legs)
    )

# Output:
# A person has 2 legs
# A cat has 4 legs
# A spider has 8 legs


# Loop through keys

for key in d.keys():
    print(key)


# Loop through values

for value in d.values():
    print(value)


# Loop through both keys and values

for key, value in d.items():
    print(key, value)


# ============================================================
# DICTIONARY COMPREHENSIONS
# ============================================================

nums = [0, 1, 2, 3, 4]

even_num_to_square = {
    x: x ** 2
    for x in nums
    if x % 2 == 0
}

print(even_num_to_square)
# {0: 0, 2: 4, 4: 16}


# ============================================================
# SETS
# ============================================================

# A set is an unordered collection
# of distinct/unique elements.

animals = {'cat', 'dog'}

print('cat' in animals)
# True

print('fish' in animals)
# False

# Add an element
animals.add('fish')

print('fish' in animals)
# True

# Number of elements
print(len(animals))
# 3

# Adding duplicate does nothing
animals.add('cat')

print(len(animals))
# 3

# Remove element
animals.remove('cat')

print(len(animals))
# 2


# ------------------------------------------------------------
# SETS WITH DIFFERENT DATA TYPES
# ------------------------------------------------------------

# A set can contain different hashable data types.

my_set = {
    10,
    "hello",
    3.5,
    True,
    (1, 2)
}

print(my_set)

# A list cannot be an element of a set
# because lists are mutable and unhashable.

# my_set = {[1, 2], [3, 4]}
# TypeError


# ============================================================
# SET LOOPS
# ============================================================

animals = {'cat', 'dog', 'fish'}

for animal in animals:
    print(animal)

# Sets are unordered.
# Therefore, do not depend on their iteration order.


# enumerate() gives index and value

for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))


# ============================================================
# SET COMPREHENSIONS
# ============================================================

from math import sqrt

nums = {
    int(sqrt(x))
    for x in range(30)
}

print(nums)
# {0, 1, 2, 3, 4, 5}


# ============================================================
# TUPLES
# ============================================================

# Tuples are:
# - Ordered
# - Immutable
# - Allow duplicate values
# - Can contain different data types

student = (
    "Hifza",
    22,
    "Software Engineering"
)

print(student)

print(student[0])
# Hifza

print(student[1])
# 22

print(student[2])
# Software Engineering

# Tuple values cannot be changed.

# student[0] = "Ali"
# TypeError


# ============================================================
# FUNCTIONS
# ============================================================

# Functions are reusable blocks of code.
# They are defined using the def keyword.

def sign(x):

    if x > 0:
        return 'positive'

    elif x < 0:
        return 'negative'

    else:
        return 'zero'


for x in [-1, 0, 1]:
    print(sign(x))

# Output:
# negative
# zero
# positive


# ============================================================
# FUNCTION PARAMETERS
# ============================================================

def greet(name):

    print("Hello", name)


greet("Hifza")
# Hello Hifza


# ============================================================
# RETURN
# ============================================================

def add(a, b):

    return a + b


result = add(5, 3)

print(result)
# 8


# ============================================================
# OPTIONAL / KEYWORD ARGUMENTS
# ============================================================

def hello(name, loud=False):

    if loud:

        print(
            'HELLO, %s!'
            % name.upper()
        )

    else:

        print(
            'Hello, %s'
            % name
        )


hello('Bob')
# Hello, Bob

hello('Fred', loud=True)
# HELLO, FRED!


# ============================================================
# LAMBDA FUNCTIONS
# ============================================================

# Lambda functions are anonymous functions.
#
# Syntax:
#
# lambda arguments : expression


l = lambda a: a + 5

print(l(2))
# 7


# Multiple arguments

l1 = lambda a, b, c: a * b * c

print(l1(10, 20, 30))
# 6000


# Lambda with max()

students = [
    ("Ali", 85),
    ("Ahmad", 92),
    ("Aisha", 78)
]

top = max(
    students,
    key=lambda student: student[1]
)

print(top)
# ('Ahmad', 92)


# ============================================================
# CLASSES
# ============================================================

# A class is a blueprint for creating objects.

class Greeter:

    pass


g = Greeter()


# ============================================================
# CONSTRUCTOR
# ============================================================

# __init__ is the constructor.
# It runs automatically when an object is created.

class Student:

    def __init__(self, name):

        self.name = name


student1 = Student("Hifza")

print(student1.name)
# Hifza


# ============================================================
# INSTANCE VARIABLES
# ============================================================

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


s1 = Student("Hifza", 22)
s2 = Student("Ali", 20)

print(s1.name)
print(s1.age)

print(s2.name)
print(s2.age)


# ============================================================
# INSTANCE METHODS
# ============================================================

class Greeter:

    def __init__(self, name):

        self.name = name


    def greet(self):

        print("Hello,", self.name)


g = Greeter("Fred")

g.greet()
# Hello, Fred


# ============================================================
# COMPLETE CLASS EXAMPLE
# ============================================================

class Greeter:

    # Constructor
    def __init__(self, name):

        self.name = name


    # Instance method
    def greet(self, loud=False):

        if loud:

            print(
                'HELLO, %s!'
                % self.name.upper()
            )

        else:

            print(
                'Hello, %s'
                % self.name
            )


g = Greeter('Fred')

g.greet()
# Hello, Fred

g.greet(loud=True)
# HELLO, FRED!


# ============================================================
# TASKS
# ============================================================


# ============================================================
# Q1
# Write code to determine whether a number is even or odd
# and print it.
# ============================================================

number = 5

if number % 2 == 0:

    print("even")

else:

    print("odd")


# ============================================================
# Q2
# For a given list of strings, check if the length of each
# string is even or odd. Print even or odd accordingly.
# ============================================================

x = [
    'alphabets',
    'numerics',
    'data types',
    '123',
    'wild',
    'abc',
    'chars'
]

for string in x:

    if len(string) % 2 == 0:

        print(string, "even")

    else:

        print(string, "odd")


# ============================================================
# Q3
# Write a code to reverse the string "hello" using indexing
# and print it.
# ============================================================

greeting = 'hello'

print(greeting[::-1])


# ============================================================
# Q4
# For numbers in range 0 to 100, return a list of those that
# are multiple of 2 but not 5.
# ============================================================

def func():

    result = []

    for x in range(0, 101):

        if x % 2 == 0 and x % 5 != 0:

            result.append(x)

    return result


l1 = func()

print(
    'List of multiples of 2 but not 5:'
)

print(l1)


# ============================================================
# Q5
# Write a Python function that accepts a string and calculates
# the number of upper case letters and lower case letters.
# ============================================================

string = (
    "Hello Mr. Rogers, how are you "
    "this fine Tuesday?"
)


def enum_cases(string):

    upper_count = 0
    lower_count = 0

    for char in string:

        if char.isupper():

            upper_count += 1

        elif char.islower():

            lower_count += 1

    return upper_count, lower_count


print(
    'Upper case characters: %d\n'
    'Lower case characters: %d'
    % enum_cases(string)
)


# ============================================================
# Q6
# Write a function that prints the integers from 1 to 100.
# For multiples of three, print Fizz.
# For multiples of five, print Buzz.
# For multiples of both three and five, print FizzBuzz.
# ============================================================

def special_print():

    for i in range(1, 101):

        if i % 3 == 0 and i % 5 == 0:

            print("FizzBuzz")

        elif i % 3 == 0:

            print("Fizz")

        elif i % 5 == 0:

            print("Buzz")

        else:

            print(i)


special_print()


# ============================================================
# Q7
# Write a function calculateSum(l, k) which takes a list l
# and a number k as input and returns two numbers from l
# that add up to k.
# ============================================================

l = [
    1,
    21,
    3,
    14,
    5,
    60,
    7,
    6
]

k = 81


def calculateSum(l, k):

    seen = set()

    for num in l:

        complement = k - num

        if complement in seen:

            return complement, num

        seen.add(num)

    return None


print(calculateSum(l, k))
# (21, 60)


# ============================================================
# Q8
# Write a function find_students that receives the students
# dictionary and an address, and returns a list with names
# in sorted order of all students whose address matches.
# ============================================================

def find_students(address, students):

    result = []

    for name, details in students.items():

        if details["address"] == address:

            result.append(name)

    return sorted(result)


students = {

    "Ali": {
        "age": 6,
        "address": "Lahore"
    },

    "Ahmad": {
        "age": 15,
        "address": "Islamabad"
    },

    "Eesha": {
        "age": 21,
        "address": "Karachi"
    }
}

print(
    find_students(
        "Lahore",
        students
    )
)


# ============================================================
# Q9
# Given an unsorted list of integers, write a function
# first_missing_positive that returns the smallest missing
# positive integer.
# ============================================================

def first_missing_positive(nums):

    n = len(nums)

    # Place every valid number at its correct index.
    for i in range(n):

        while (
            1 <= nums[i] <= n
            and nums[nums[i] - 1] != nums[i]
        ):

            correct_index = nums[i] - 1

            nums[i], nums[correct_index] = (
                nums[correct_index],
                nums[i]
            )

    # Find the first position containing
    # an incorrect value.
    for i in range(n):

        if nums[i] != i + 1:

            return i + 1

    return n + 1


print(
    first_missing_positive(
        [3, 4, -1, 1]
    )
)
# Output: 2

print(
    first_missing_positive(
        [1, 2, 0]
    )
)
# Output: 3

print(
    first_missing_positive(
        [7, 8, 9, 11]
    )
)
# Output: 1


# ============================================================
# Q10
# Write a function flatten_dict that takes a nested dictionary
# and returns a flattened version where keys are concatenated
# with underscores for nested levels.
#
# Handle edge cases like empty dictionaries or non-dictionary
# values.
# ============================================================

nested_dict = {

    'a': 1,

    'b': {

        'c': 2,

        'd': {

            'e': 3,
            'f': 4
        }
    },

    'g': 5
}


def flatten_dict(
    d,
    parent_key='',
    sep='_'
):

    flattened = {}

    # Handle non-dictionary values
    if not isinstance(d, dict):

        return {
            parent_key: d
        }

    for key, value in d.items():

        if parent_key:

            new_key = (
                parent_key
                + sep
                + str(key)
            )

        else:

            new_key = str(key)

        # If value is a dictionary,
        # recursively flatten it.
        if isinstance(value, dict):

            flattened.update(
                flatten_dict(
                    value,
                    new_key,
                    sep
                )
            )

        else:

            flattened[new_key] = value

    return flattened


print(
    flatten_dict(nested_dict)
)

# Expected:
# {
#     'a': 1,
#     'b_c': 2,
#     'b_d_e': 3,
#     'b_d_f': 4,
#     'g': 5
# }


# ============================================================
# Q11
# Given a list of tuples representing student names and their
# scores, write a function top_student that returns the name
# of the student with the highest score.
# ============================================================

scores = [
    ("Ali", 85),
    ("Ahmad", 92),
    ("Aisha", 78)
]


def top_student(students):

    if not students:

        return None

    top = max(
        students,
        key=lambda student: student[1]
    )

    return top[0]


print(
    top_student(scores)
)

# Expected:
# Ahmad


# ============================================================
# Q12
# Write a function count_vowels that takes a string and
# returns a dictionary where the keys are vowels
# (a, e, i, o, u) and the values are their respective counts.
# The counting should be case-insensitive.
# ============================================================

text = "Hello, how are you today?"


def count_vowels(s):

    vowels = {

        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }

    for char in s.lower():

        if char in vowels:

            vowels[char] += 1

    return vowels


print(
    count_vowels(text)
)

# Expected:
# {
#     'a': 2,
#     'e': 2,
#     'i': 0,
#     'o': 3,
#     'u': 1
# }


# ============================================================
# Q13
# Given a list of numbers, write a function remove_outliers
# that removes the smallest and largest numbers from the list
# and returns the modified list.
# ============================================================

numbers = [
    12,
    3,
    45,
    7,
    1,
    67,
    9
]


def remove_outliers(lst):

    if len(lst) <= 2:

        return []

    # Copy the list so the original is not modified.
    result = lst.copy()

    # Remove smallest
    result.remove(
        min(result)
    )

    # Remove largest
    result.remove(
        max(result)
    )

    return result


print(
    remove_outliers(numbers)
)

# Expected:
# [12, 3, 45, 7, 9]


# ============================================================
# Q14
# Longest Consecutive Sequence in a List
#
# Given an unsorted list of integers, write a function
# longest_consecutive_sequence that returns the length of
# the longest consecutive sequence of numbers.
#
# Example:
# [100, 4, 200, 1, 3, 2]
#
# 1, 2, 3, 4 → length 4
# ============================================================

nums = [
    100,
    4,
    200,
    1,
    3,
    2,
    101,
    99,
    102,
    103,
    104
]


def longest_consecutive_sequence(nums):

    if not nums:

        return 0

    # Convert list to set for fast lookup.
    num_set = set(nums)

    longest = 0

    for num in num_set:

        # Only start counting when this number
        # is the beginning of a sequence.
        if num - 1 not in num_set:

            current = num
            length = 1

            while current + 1 in num_set:

                current += 1
                length += 1

            longest = max(
                longest,
                length
            )

    return longest


print(
    longest_consecutive_sequence(nums)
)

# Expected output for the given list:
# 6
#
# Because:
# 99, 100, 101, 102, 103, 104
# contains 6 consecutive numbers.


# ============================================================
# Q15
# Implement a Trie (Prefix Tree)
#
# Write a class Trie with methods:
#
# insert(word)
# search(word)
# startsWith(prefix)
#
# to efficiently store and retrieve words.
# ============================================================

class Trie:

    def __init__(self):

        # Stores child characters.
        self.children = {}

        # True when a complete word ends
        # at this node.
        self.is_end = False


    def insert(self, word):

        current = self

        for char in word:

            if char not in current.children:

                current.children[char] = Trie()

            current = current.children[char]

        # Mark the final node as a complete word.
        current.is_end = True


    def search(self, word):

        current = self

        for char in word:

            if char not in current.children:

                return False

            current = current.children[char]

        # True only if the complete word exists.
        return current.is_end


    def startsWith(self, prefix):

        current = self

        for char in prefix:

            if char not in current.children:

                return False

            current = current.children[char]

        # Prefix exists.
        return True


trie = Trie()

trie.insert("apple")

print(
    trie.search("apple")
)
# True

print(
    trie.search("app")
)
# False

print(
    trie.startsWith("app")
)
# True

trie.insert("app")

print(
    trie.search("app")
)
# True


# ============================================================
# Q16
# Design a CircularBuffer class that supports:
#
# append(x):
# Add an element to the buffer.
# If full, overwrite the oldest element.
#
# get():
# Return the buffer as a list in insertion order.
# ============================================================

class CircularBuffer:

    def __init__(self, size):

        self.size = size
        self.buffer = []


    def append(self, x):

        # If the buffer is full,
        # remove the oldest element.
        if len(self.buffer) == self.size:

            self.buffer.pop(0)

        # Add the new element.
        self.buffer.append(x)


    def get(self):

        # Return a copy in insertion order.
        return self.buffer.copy()


cb = CircularBuffer(3)

cb.append(1)
cb.append(2)
cb.append(3)

print(
    cb.get()
)
# [1, 2, 3]

cb.append(4)

print(
    cb.get()
)
# [2, 3, 4]


# ============================================================
# Q17
# Write a function one_hot_encode that converts categorical
# labels such as ["cat", "dog", "bird"] into one-hot encoded
# arrays without using OneHotEncoder.
# ============================================================

import numpy as np


def one_hot_encode(labels):

    # Handle empty input.
    if not labels:

        return np.array([])

    # Get unique categories while preserving
    # their first appearance.
    categories = list(
        dict.fromkeys(labels)
    )

    # Create mapping:
    #
    # category → column index
    #
    # Example:
    # cat  → 0
    # dog  → 1
    # bird → 2

    category_index = {

        category: index

        for index, category
        in enumerate(categories)
    }

    # Create a matrix filled with zeros.
    encoded = np.zeros(
        (
            len(labels),
            len(categories)
        ),
        dtype=float
    )

    # Put 1 in the appropriate column.
    for i, label in enumerate(labels):

        encoded[
            i,
            category_index[label]
        ] = 1.0

    return encoded


labels = [
    "cat",
    "dog",
    "bird",
    "cat"
]

print(
    one_hot_encode(labels)
)

# Expected Output:
#
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]
#  [1. 0. 0.]]