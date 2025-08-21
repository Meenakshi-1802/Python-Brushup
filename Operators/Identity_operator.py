list1 = [1, 2, 3]
list2 = list1
list3 = [1, 4, 3]
print("list1 is list2:", list1 is list2)       # True (same object)
print("list1 is list3:", list1 is list3)       # False (different objects, same values)
print("list1 is not list3:", list1 is not list3)