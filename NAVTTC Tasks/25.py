# Python Dictionary

# Creating a dictionary
country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"
}

# Printing the dictionary
print(country_capitals)

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London



country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

print(country_capitals)


# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)


# clear the dictionary
country_capitals.clear()

print(country_capitals) 


# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)


country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


country_capitals = {"England": "London", "Italy": "Rome"}

# get dictionary's length
print(len(country_capitals))   # Output: 2

numbers = {10: "ten", 20: "twenty", 30: "thirty"}

# get dictionary's length
print(len(numbers))            # Output: 3

countries = {}

# get dictionary's length
print(len(countries))          # Output: 0

file_types = {
    ".txt": "Text File",
    ".pdf": "PDF Document",
    ".jpg": "JPEG Image",
}

# use of in and not in operators
print(".pdf" in file_types)       # Output: True
print(".mp3" in file_types)       # Output: False
print(".mp3" not in file_types)   # Output: True

