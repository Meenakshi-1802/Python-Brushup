# Python Identifiers

## 1. Introduction
An **identifier** is the name given to a program element in Python.  
It is **user-defined** and is used to identify variables, functions, classes, objects, and procedures.

---

## 2. Rules for Naming Identifiers
## 🔹 1. Naming Conditions (Rules)  

✅ Allowed:  
- Must start with a **letter (a-z, A-Z)** or an **underscore (_)**
- After the first character, can contain **letters, digits (0-9), or underscores (_)**  
- Can be of **any length**  
- Case-sensitive (`age`, `Age`, and `AGE` are different identifiers)  

❌ Not Allowed:  
- Cannot start with a **digit** (e.g., `1name` ❌)  
- Cannot contain **special characters** like `@, #, $, %, !, *`  
- Cannot be a **Python keyword** (like `if`, `for`, `while`, `class`, etc.)  

---

## 🔹 2. Naming Conventions  

- **Variables** → Use lowercase words with underscores  
  student_name = "Meenakshi"
  total_marks = 450

- **Functions** → Same as variables (snake_case)
  def calculate_average():
    pass
  
- **Constants** → Use UPPERCASE letters with underscores
  PI = 3.14159
MAX_LIMIT = 1000

- **Classes** → Use PascalCase (CapWords)
 class StudentRecord:
    pass
    
- **Private variables/functions** → Start with an underscore _
 _hidden_value = 42
 
- **Modules/Files** → Use lowercase with underscores
  
3. **Case-sensitive**:
   - Identifiers treat uppercase and lowercase letters as different.


4. **Cannot use reserved keywords**:
   - Python keywords like `if`, `for`, `class`, `def`, etc. cannot be used as identifiers.

---

## 3. Best Practices for Naming Identifiers
- Use meaningful and descriptive names.
- **Snake case**: Words are written in lowercase and separated by underscores (`_`).  
  Example style: `my_variable_name`
- **Pascal case**: Each word starts with an uppercase letter and no underscores.  
  Example style: `MyVariableName`
- Avoid using single-character names except for loop counters.

---
