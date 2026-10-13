# =========15. Python ====================
# Exercise on for loops in Python:
# https://www.geeksforgeeks.org/python-for-loops/

# Python For Loops
a = ["Geeks", "for", "Geeks"]
for i in a:
    print(i)

# Loop Through String
s = "Geeks"
for i in s:
    print(i)

# range() Method
for i in range(0, 10, 2):
    print(i)

# -------- Control Statements ----

# 1. Continue Statement
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        continue
    print(i)

# 2. Break Statement
for i in 'geeksforgeeks':
    if i == 'e' or i == 's':
        break
print(i)

# 3. Pass Statement
for i in 'geeksforgeeks':
    pass

# 4. Else Statement
for i in range(1, 4):
    print(i)
else:  
    print("No Break\n")


# Using Enumerate
b = ["eat", "sleep", "repeat"]
for i, j in enumerate(b):
    print (i, j)


# Nested For Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
