# 🐍 Chapter 3: Features of Python

Python is a powerful, beginner-friendly, and versatile programming language. Below are the top features that make Python one of the most widely used languages across industries.

---

## ✅ 15 Key Features of Python

### 1. **Platform Independent**  
   - Python scripts can run on any operating system (Windows, Linux, macOS).
   - There is no `.exe` file in Python; it contains only pure Python code.
   - The Python interpreter is OS-dependent, but Python scripts are OS-independent.
   - ✅ Write Once, Run Anywhere
     

### 2. **Portable**  
   - Python applications are portable — the same code runs on different OSes without modification.
   - Unlike C, Python code does not rely on OS-specific syntax.
     

### 3. **Dynamically Typed**  
   - No need to declare variable types explicitly.
   - Python decides the type at runtime.  
  
   x = 10       # Integer  
   x = "Hello"  # Now it's a string
    

### 4. **Python Collections**

- Used to store and manage large volumes of data.

- Supports: lists, tuples, sets, dictionaries, and the collections module.

- Improves performance in server-side applications.


### 5. **Object-Oriented Programming (OOP)**

- Supports encapsulation, abstraction, inheritance (including multiple inheritance), and polymorphism.

- Python supports both procedure-oriented and object-oriented programming.


### 6. **Exception Handling**

Manages errors gracefully without crashing the program.

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)

    
### 7. **I/O Streams and File Handling**

Python supports reading/writing files easily.

with open('sample.txt', 'r') as file:
    content = file.read()

    
### 8. **Multi-Threading**

- Supports concurrent execution using threads.

- Useful for parallel, real-time, and background tasks.

import threading  
def task():  
    print("Running in thread")  
thread = threading.Thread(target=task)  
thread.start()


### 9. **Network Programming**

- Supports socket programming and RESTful APIs.

- Libraries: socket, requests, asyncio

import socket  
s = socket.socket()  
s.connect(("example.com", 80))


### 10. **Database Access**

- Supports integration with databases like MySQL, PostgreSQL, SQLite, Oracle, etc.

- Libraries: sqlite3, mysql.connector, psycopg2

import sqlite3  
conn = sqlite3.connect('data.db')  
cursor = conn.cursor()


### 11. **Rich Standard Library**

Comes with built-in modules for math, regex, file I/O, web services, threading, testing, GUI, and more.

### 12. **Embeddable**

- Python can be embedded into other languages like C/C++.

- Also allows calling C/C++ code from Python scripts.

### 13. **GUI Programming**

- Supports graphical user interface development using:

- Tkinter

- PyQt

- wxPython

- Kivy

import tkinter as tk  
window = tk.Tk()  
window.title("My App")  
window.mainloop()


### 14. **Modular Programming**

- Allows splitting large programs into reusable modules and packages.

- Promotes clean code and better maintenance.

# mymodule.py  
def greet():  
    print("Hello!")  

# main.py  
import mymodule  
mymodule.greet()


### 15. **Free and Open Source**

Python is freely available and open-source under FLOSS (Free/Libre and Open Source Software).

🔗 Download: https://www.python.org/downloads/
