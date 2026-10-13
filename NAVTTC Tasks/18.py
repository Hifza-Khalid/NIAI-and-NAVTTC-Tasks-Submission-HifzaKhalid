# Python Continue Statement
# continue skips the current iteration.

for i in range(1, 11):
    if i == 6:
        continue

    print(i, end=" ")

# Example 1: Skipping specific characters in a string

for char in "GeeksforGeeks":
    if char == "e":
        continue
    print(char, end=" ")


# Example 2. Using continue in nested loops

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in a:
    for num in row:
        if num == 3:
            continue
        print(num, end=" ")


# Example 3. Using continue with a while loop

i = 0
while i < 10:
    if i == 5:
        i += 1  # ensure the loop variable is incremented to avoid infinite loop
        continue
    print(i)
    i += 1

