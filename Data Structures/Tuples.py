#Creating a Tuple
fruits = ("apple", "banana", "cherry", "mango", "orange")
print("Original Tuple:", fruits)

#Indexing
print("First fruit:", fruits[0])
print("Third fruit:", fruits[2])
print("Last fruit:", fruits[-1])

#Slicing
print("Fruits from index 1 to 3:", fruits[1:4])
print("First three fruits:", fruits[:3])
print("Fruits from index 2 to end:", fruits[2:])
print("Every second fruit:", fruits[::2])
print("Reversed Tuple:", fruits[::-1])

#Length of tuple
print("Total fruits:", len(fruits))

#Tuple Methods
numbers = (1, 2, 3, 2, 5, 2, 7)
print("Numbers tuple:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 5:", numbers.index(5))

#Tuple Packing and Unpacking
student = ("Meenakshi", 22, "Data Science")
(name, age, course) = student
print("Name:", name)
print("Age:", age)
print("Course:", course)

#Nested Tuple
nested = (("A", 1), ("B", 2), ("C", 3))
print("Nested Tuple:", nested)
print("Access nested element:", nested[1][0])  # Access 'B'

#Tuple vs List (Mutability)
list_example = ["apple", "banana", "cherry"]
tuple_example = ("apple", "banana", "cherry")

list_example[1] = "grape"  #allowed
print("Modified List:", list_example)

# tuple_example[1] = "grape"  #not allowed, would raise TypeError
print("Tuples are immutable — cannot modify elements directly.")

#Converting between list and tuple
my_list = ["a", "b", "c"]
my_tuple = tuple(my_list)
print("List to Tuple:", my_tuple)

new_list = list(fruits)
print("Tuple to List:", new_list)

#Tuple Concatenation and Repetition
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)
