#Create a list
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("Original list:", fruits)

#Indexing
print("First fruit:", fruits[0])      # Positive index
print("Last fruit:", fruits[-1])      # Negative index

#Slicing
print("Fruits from index 1 to 3:", fruits[1:4])     # ['banana', 'cherry', 'mango']
print("First three fruits:", fruits[:3])            # ['apple', 'banana', 'cherry']
print("Fruits from index 2 to end:", fruits[2:])    # ['cherry', 'mango', 'orange']
print("All fruits except last one:", fruits[:-1])   # ['apple', 'banana', 'cherry', 'mango']
print("Every 2nd fruit:", fruits[::2])              # ['apple', 'cherry', 'orange']
print("Reverse order:", fruits[::-1])               # ['orange', 'mango', 'cherry', 'banana', 'apple']

#Add elements
fruits.append("kiwi")         # Add one item at end
fruits.insert(2, "grape")     # Insert at specific position
print("After adding fruits:", fruits)

#Remove elements
fruits.remove("banana")       # Remove by value
fruits.pop(3)                 # Remove by index
print("After removing fruits:", fruits)

#Sorting and Reversing
fruits.sort()                 # Sort alphabetically
print("Sorted list:", fruits)
fruits.reverse()              # Reverse order
print("Reversed list:", fruits)

#Other useful functions
print("Total fruits:", len(fruits))      # Number of elements
print("Index of 'apple':", fruits.index("apple"))
print("Count of 'apple':", fruits.count("apple"))

#Copy & Clear
copy_list = fruits.copy()     # Make a copy
fruits.clear()                # Remove all elements
print("\nCopy of list:", copy_list)
print("Cleared original list:", fruits)
