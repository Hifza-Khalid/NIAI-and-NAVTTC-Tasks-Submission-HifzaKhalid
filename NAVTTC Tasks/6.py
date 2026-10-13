# Find square root of real or complex numbers

# Importing the complex math module
import cmath

num = 1 + 2j

# To take input from the user
# num = eval(input("Enter a number: "))

# Calculate square root
num_sqrt = cmath.sqrt(num)

# Display the result
print("The square root of {0} is {1:.3f}+{2:.3f}j".format(
    num, num_sqrt.real, num_sqrt.imag
))