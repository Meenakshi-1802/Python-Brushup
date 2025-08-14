# 🧠 Python Memory Management

## 1. Overview
Python manages memory automatically with the help of its **memory manager** and **garbage collector**.  
It organizes memory into different sections based on usage.

---

## 2. Python memory is divided into different areas:
- **Stack Memory** → Stores reference variables and function call data.
- **Heap Memory** → Stores actual objects.
- **Global Memory** → Stores global variables.
- **Static Memory** → Stores static variables.
- **Text Memory** → Stores program instructions.

  <img width="759" height="424" alt="Screenshot 2025-08-14 193503" src="https://github.com/user-attachments/assets/c75c683e-cc11-4f42-a437-8ed16447f262" />


---

## 3. Stack and Heap Memory for Python Variables

When you create a variable in Python:
1. **Stack memory** stores the **reference variable**.
2. **Heap memory** stores the **actual object**.
3. The reference variable in stack points to the object's location in heap.
   
   <img width="527" height="533" alt="Screenshot 2025-08-14 193447" src="https://github.com/user-attachments/assets/a4e4a2c2-e841-41d6-b00d-2311267a93d8" />

---

## 2. Higher Order Memory Space
- Stores all **command-line arguments**.
- Stores **operating system environment variables**.

---

## 4. Stack Memory Space
- Stores **local variables**.
- Memory allocation follows **LIFO (Last In, First Out)**.
- Grows automatically as long as sharable memory is available.
- If the stack is full, it raises a **stack overflow exception**.
- Python is **dynamically typed** — variable declaration is not necessary, and variable types are determined at runtime.
- Every time a value is assigned, a **new memory location** is created.
- In Python, there is no concept of simple variables; everything is a **reference variable**.
- Reference variables are stored in **stack memory** and refer to **objects** stored in **heap memory**.
- Supports **memory pooling** (memory reusability).

---

## 5. Shared Memory Space
- Can be shared by both **stack** and **heap**.

---

## 6. Heap Memory Space
- Used for **dynamic memory management**.
- Memory allocation and deallocation happen **at runtime**.
- Grows automatically as long as sharable memory is available.
- Memory allocation is **random**.
- Contains the **data** and its **address**, which is stored in reference variables inside the stack.

---

## 7. Global Memory Space
- Stores **global variables**.
- Size depends on the number of global variables declared in the Python application.

---

## 8. Static Memory Space
- Stores **static variables**.
- Size is fixed according to the number of static variables declared in the Python application.

---

## 9. Text Memory Space
- Contains all **Python program instructions**.
- Stores **Python libraries**.

---

## 10. Key Points
- **Stack** contains all reference variables.
- **Heap** contains objects that reference variables point to.
- Memory management in Python is handled **automatically**.
- Python is **100% object-oriented** — all values are objects.

---
