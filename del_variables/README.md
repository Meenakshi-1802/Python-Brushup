# 🗑 Deleting Variables in Python

## 1. What Does It Mean to Delete a Variable?

In Python, you can **delete** a variable using the `del` keyword.  
This removes the variable **name** from memory, meaning it no longer exists in the current program scope.

---

## 2. Syntax

del variable_name

## 3. How It Works

del a does not delete the actual value immediately if other variables are still referring to it.

It only removes the reference (the name) from the namespace.

If no references are left to the value, Python's garbage collector removes it from memory.
