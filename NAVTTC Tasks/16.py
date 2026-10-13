# Python While Loop
# Repeats the code while the condition is true.

# Set the counter to 0
count = 0

# Continue while count is less than 3
while count < 3:

    # Increase the counter by 1
    count = count + 1

    # Display the message
    print("Hello Geek")


# Infinite while Loop
age = 28
while age > 19:
    print('Infinite Loop')

# Using with continue statement
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue
    print(a[i])
    i += 1


# Using with break statement
i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
    print(a[i])
    i += 1

# Using with pass statement

a = 'geeksforgeeks'
i = 0
while i < len(a):
    i += 1
    pass
  
print('Value of i :', i)


# Using with else

i = 0
while i < 4:
    i += 1
    print(i)
else:
    print("No Break\n")

i = 0
while i < 4:
    i += 1
    print(i)
    break
else:
    print("No Break")


