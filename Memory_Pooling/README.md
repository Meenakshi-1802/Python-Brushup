# 🐍 Python Memory Pooling

## 📌 What is Memory Pooling?
Memory pooling in Python means:
- Each time you assign a value, Python **does not always create a new memory location**.
- If the value **already exists** in heap memory, Python **reuses the same memory address** for the new variable.
- If the value does **not exist**, Python **creates a new memory location**.
