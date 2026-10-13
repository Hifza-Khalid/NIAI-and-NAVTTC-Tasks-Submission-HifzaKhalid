# Python Break Statement
# break immediately stops the loop.

a = [1, 3, 5, 7, 9, 11]
val = 7

for i in a:
    if i == val:
        print(f"Found at {i}!")
        break
else:
    print("not found")

# Break Statement with for Loop
for i in range(10):
    print(i)
    if i == 6:
        break

# Break Statement with while Loop
c = 5

while True:
    print(c)
    c -= 1
    if c == 0:
        print("Countdown finished!")
        break  # Exit the loop


# Example: If we have a list of lists (a 2D list) and we want to find a specific number. Once we find the number, we want to stop searching in both the inner and outer loops.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
val = 5
found = False

for r in matrix:
    for n in r:
        if n == val:
            print(f"{val} found!")
            found = True
            break  # Exit the inner loop
    if found:
        break  # Exit the outer loop
