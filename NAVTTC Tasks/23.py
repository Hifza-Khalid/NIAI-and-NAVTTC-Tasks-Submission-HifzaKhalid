# Python Strings

# Multiline string
message = """To avoid pain, they avoid pleasure.
To avoid death, they avoid life."""

print(message)

# Access String Characters
model = 'ChatGPT'

# Access the first character
print(model[0])    # Output: C

# Access the fifth character
print(model[4])    # Output: G

# Access the last character
print(model[-1])   # Output: T

# Access the fourth last character
print(model[-4])   # Output: t

print(model[8])       # IndexError


# Access characters from index 0 up to (but not including) 4
print(model[0:4])   # Output: Chat

# Strings are Immutable

model[0] = 'W'
print(model)

model = 'Opus'
version = '5'

model = model + " " + version
print(model)    # Opus 5


# Python String Methods
text = "ChatGPT is great."

# Replace "ChatGPT" with "Claude"
new_text = text.replace("ChatGPT", "Claude")

print(new_text)  # Output: Claude is great.


# String Membership Test
print('Chat' in 'ChatGPT')        # True
print('Claude' not in 'ChatGPT')  # True

# Iterate Through a String
model = 'Opus'

for c in model:
    print(c)

# Python String Length
model = 'Opus'

# Count the number of characters
print(len(model))   # Output: 4


# Escape Sequences
# example = "He said, "What's there?"" 

# print(example) # Error

# escape double quotes
example = "He said, \"What's there?\""

# escape single quotes
example = 'He said, "What\'s there?"'

print(example)

# Output: He said, "What's there?"

# String Formatting (f-Strings)
company = 'Google'
field = 'AI'

message = f'{company} is an {field} company.'
print(message)
