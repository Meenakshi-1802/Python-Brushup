# Control Flow Statements in Python 🚀  

Control flow statements are used to **make decisions** and **repeat tasks** in a program.  
They allow programs to choose different paths and control execution based on conditions.  

---

## 🔹 Conditional Statements  

### 1️⃣ Simple if  
- The `if` statement checks a condition.  
- If the condition is **True**, a block of code is executed.  
- If the condition is **False**, nothing happens.  

---

### 2️⃣ if-else  
- The `if-else` statement provides two alternative paths.  
- If the condition is **True** → one block is executed.  
- If the condition is **False** → the other block is executed.  

---

### 3️⃣ Nested if  
- A nested `if` means an `if` inside another `if`.  
- Used when one decision depends on the result of another condition.  
- Useful for checking multiple levels of conditions.  

---

### 4️⃣ If-elif-else (Ladder if / If-elif ladder)  
- Used when we need to check multiple conditions one by one.  
- Conditions are checked from **top to bottom**.  
- The first condition that is **True** is executed, and the rest are skipped.  
- If none are True, the `else` block (if present) runs.  

---

### 🔑 Difference: Nested If vs Ladder If  

| Feature        | Nested If | Ladder If (if-elif-else) |
|----------------|-----------|--------------------------|
| Structure      | One `if` inside another | Multiple conditions in sequence |
| Readability    | More complex (due to indentation) | Easier to read and follow |
| Use Case       | When conditions are **dependent** on each other | When checking **separate multiple conditions** |
| Testing Style  | Mostly used for **positive tests** (checking only when previous condition is True) | Mostly used for **negative tests** (checking step by step until one is True) |

---

## 🔹 Looping Statements  

Loops are used to **repeat a block of code** multiple times until a condition is met.  

### 5️⃣ while Loop  
- Repeats a block of code **as long as** the condition is True.  
- Condition is checked **before each iteration**.  
- Risk: If condition never becomes False → **infinite loop**.  

---

### 6️⃣ for Loop  
- Used for iterating over a sequence (list, tuple, string, range, etc.).  
- Executes the block once for **each item in the sequence**.  

---

### 7️⃣ Nested Loops  
- A loop **inside another loop**.  
- Used for working with multi-dimensional data (like tables, matrices).  

---

### 🔑 Difference: while vs for  

| Feature      | while Loop | for Loop |
|--------------|------------|----------|
| Condition    | Repeats while condition is True | Iterates over a sequence/range |
| Use Case     | When number of iterations is **unknown** | When number of iterations is **known** |
| Risk         | Can cause infinite loop if condition not handled | Safer, usually finite iterations |

---

## ✅ Summary  

- **if** → single condition  
- **if-else** → two choices  
- **nested if** → decision inside another decision  
- **if-elif-else ladder** → many conditions checked step by step  
- **while** → repeat while condition is True  
- **for** → iterate through a sequence  
- **nested loops** → loops inside loops  

💡 These **control + loop statements** make programs dynamic, repetitive, and decision-making! 🚀  
