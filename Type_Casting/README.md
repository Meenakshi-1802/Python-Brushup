# Python Type Casting & Type Conversion

## 🔹 Type Casting (Explicit Conversion)
Type casting means explicitly converting one data type into another using **constructor functions**.  
Since Python is object-oriented, it uses classes to define its data types, including primitive ones.  

### Casting Functions
- **`int()`** → Constructs an integer number from:
  - Integer literal  
  - Float literal (rounds down)  
  - String literal (if the string represents a whole number)  

- **`float()`** → Constructs a float number from:
  - Integer literal  
  - Float literal  
  - String literal (if the string represents a float or integer)  

- **`str()`** → Constructs a string from:
  - Strings  
  - Integer literals  
  - Float literals  
  - Other data types  

- **`complex()`** → Constructs a complex number of the form **a + bj** from:
  - Real part  
  - Imaginary part  

---

## 🔹 Type Conversion (Implicit Conversion)
Type conversion means automatic conversion of one data type to another by Python.  
This is also called **Type Promotion**.  

### Key Points
- Done **automatically by Python** (no manual action).  
- Happens when different data types are used in an expression.  
- Python converts smaller data type → larger data type to avoid data loss.  
- Example: `int + float → float`  

---

## ✅ Difference Between Type Casting and Type Conversion

| Feature        | Type Casting (Explicit) | Type Conversion (Implicit) |
|----------------|--------------------------|-----------------------------|
| **Who does it?** | Programmer | Python Interpreter |
| **How?**        | Using functions (`int()`, `float()`, `str()`, `complex()`) | Automatically during operations |
| **Control**     | Full control | No control (Python decides) |
| **Other Name**  | Explicit Conversion | Type Promotion |

---

