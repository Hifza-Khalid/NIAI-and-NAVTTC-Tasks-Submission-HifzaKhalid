# Python Lists

# Creating a List
cart = ["T-shirt", "Lamp", "Pen"]
print(cart)

# A list of mixed data types
my_list = [1, "Python", 3.14]
print(my_list)

# Empty list
my_list = []
print(my_list)

# Convert a string to a list
vowels = "aeiou"
vowels_list = list(vowels)
print(vowels_list)


# Accessing List Items
languages = ["Python", "Swift", "C++"]

# Access the first item
print(f"languages[0] = {languages[0]}")

# Access the third item
print(f"languages[2] = {languages[2]}")


# Negative Indexing
languages = ["Python", "Swift", "C++"]

# Access the last item
print('languages[-1] =', languages[-1])

# Access the third last item
print('languages[-3] =', languages[-3])


# Updating List Items
cart = ["T-shirt", "Lamp", "Pen"]

# Update second item
cart[1] = "Shoes"

print(cart)


# Adding Items using append()
cart = ["T-shirt", "Lamp", "Pen"]

# Add "Book" to the list
cart.append("Book")

print(cart)


# Adding Items using extend()
cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]

# Add all items from fav_items
cart.extend(fav_items)

print(cart)


# Insert an item
cart = ["T-shirt", "Lamp", "Pen"]

# Add "Book" at index 2
cart.insert(2, "Book")

print(cart)


# Remove Items
cart = ["T-shirt", "Lamp", "Pen", "Book"]

# Remove "Pen"
cart.remove("Pen")

# Remove the last item
last_item = cart.pop()

print(cart)
print(last_item)

# Clear the list
cart.clear()
print(cart)


# Delete an item using del
cart = ['T-shirt', 'Lamp', 'Pen', 'Book']

# Delete the third item
del cart[2]

print(cart)


# Copying a List
favorite_items = ["T-shirt", "Lamp", "Pen"]

# Copy the list
cart = favorite_items.copy()

# Add an item
favorite_items.append("Book")

print(f"favorite_items = {favorite_items}")
print(f"cart = {cart}")


# len() Function
favorite_items = ["T-shirt", "Lamp", "Pen"]

size = len(favorite_items)

print(size)


# List Membership Test
cart = ["T-shirt", "Lamp", "Pen"]

result = "Lamp" in cart
print(result)

result = "Book" in cart
print(result)


# Iterating Through a List
cart_items = ["T-shirt", "Lamp", "Pen"]

for item in cart_items:
    print(item)