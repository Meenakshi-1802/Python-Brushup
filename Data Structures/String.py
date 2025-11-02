#Creating a String
string = "Python is a high level programming language"
print("Original String:", string)

#Indexing
print("Character at index 0:", string[0])
print("Character at index 5:", string[5])
print("Last character:", string[-1])

#Slicing
print("Characters from index 0 to 6:", string[0:6])
print("Characters from index 7 to 18:", string[7:18])
print("First 10 characters:", string[:10])
print("Characters from 10 to end:", string[10:])
print("Every 2nd character:", string[::2])
print("Reverse String:", string[::-1])

#Concatenation
str1 = "Python"
str2 = "Programming"
combined = str1 + " " + str2
print("Combined String:", combined)

#Length
print("Length of string:", len(string))

#String Functions / Methods
print("Uppercase:", string.upper())
print("Lowercase:", string.lower())
print("Title case:", string.title())
print("Capitalize:", string.capitalize())
print("Replace 'high' with 'low':", string.replace("high", "low"))
print("Count of 'a':", string.count('a'))
print("Find position of 'level':", string.find("level"))
print("Does string end with 'ge'? :", string.endswith("ge"))
print("Does string start with 'Py'? :", string.startswith("Py"))

#Split and Join
words = string.split()     # Splits string into list of words
print("Split words:", words)
joined_string = "-".join(words)   # Joins words with a '-'
print("Joined with '-':", joined_string)

#Checking character types
word = "Python123"
print("Is Alpha:", word.isalpha())      # False (contains numbers)
print("Is Alphanumeric:", word.isalnum())  # True
print("Is Digit:", word.isdigit())      # False
print("Is Lowercase:", word.islower())  # False
print("Is Uppercase:", word.isupper())  # False

#Removing spaces
s = "   Hello Python   "
print("Before strip:", repr(s))
print("After strip:", repr(s.strip()))  # Removes spaces

