# Python Functions
# Functions are reusable blocks of code used for a specific task.

# Define a function
def fun():
    print("Welcome to GFG")


# Call the function
fun()


# Function with an argument
# Checks whether the number is Even or Odd
def evenOdd(x):

    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"


# Call function with different values
print(evenOdd(16))
print(evenOdd(7))


#---Types of Function Arguments
# 1. Default argument:
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

# 2. Keyword Arguments:

def student(fname, lname):
    print(fname, lname)

student(fname='Geeks', lname='Practice')
student(lname='Practice', fname='Geeks')

# 3. Positional Arguments: 
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)

print("Case-1:")
nameAge("Olivia", 27)

print("Case-2:")
nameAge(27, "Olivia")


# 4. Arbitrary Arguments: 
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')

# ---Function within Functions

def f1():
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
f1()


def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-4))


# --Pass by Reference and Pass by Value
def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)

def myFun2(x):
    x = 20

a = 10
myFun2(a)
print(a)





