# 📘 Chapter 2: Introduction to Software

**Software** is a collection of programs such as C, C++, Java, Python, HTML, and others.

Software is mainly divided into two categories:

## 🧩 Software Categories

## Software
## ├── System Software
## └── Application Software


---

## ⚙️ System Software
- Interacts directly with **hardware components**
- Example: **Operating Systems**

> ❓ **Q. Can we run any program without an OS?**  
> ✅ **Ans:** No.  
> Except BIOS, all programs require an Operating System to run.

### 🧠 BIOS (Basic Input and Output System)
- A **hardware-level program** embedded on a chip
- Responsible for **booting** the OS
- **Booting**: The process of loading the Operating System from **Hard Disk to RAM**

---

## 🖥️ What is an Operating System?

1. A **platform** to run all application software  
2. Acts as an **interface** between hardware and application software  
3. Has built-in **libraries** for communication between applications and hardware  
4. Every program must **link** with the OS library before execution  

<img width="761" height="94" alt="Screenshot 2025-08-01 184945" src="https://github.com/user-attachments/assets/caf6b9f6-e48b-4af6-9fc1-deb44d72de0f" />

---

## 🧩 Application Software

### ➤ Front-End Software  
- Interacts with **end users**  
- Collects data from users and sends to the back-end  
- Examples: Languages, ERPs, UI apps

### ➤ Back-End Software  
- Handles **server-side logic** and **database operations**  
- Examples: Databases, Files, HDFS (Big Data Storage)

<img width="1024" height="676" alt="image" src="https://github.com/user-attachments/assets/6df4861b-0e60-4b64-ae06-4d09887a25a3" />


> 📌 Python is a **Back-End Programming / Scripting Language** used to develop server-side applications.

---

## 🧠 Software Languages Classification

### 1️⃣ Low-Level Language
- **System-understandable** language (Binary: `11001010`)  
- Executed directly by **processors** like 8085, 8086  
- Also called **Machine Language**

### 2️⃣ High-Level Language
- **Human-understandable** (like English)  
- Easier to learn and write  
- Examples: `C`, `C++`, `Java`, `Python`, `HTML`, `.NET`, `Scala`

> ❓ **Q. Which is the first developed high-level language?**  
> ✅ **C Language** developed by **Dennis Ritchie** in **1972**

---

## 🔄 Language Conversion

High-Level Language ➝ Binary Code  
➡️ Requires an **Interpreter** or **Compiler**

| Role | Description |
|------|-------------|
| **Compiler** | Converts entire code at once |
| **Interpreter** | Executes code line-by-line |

---

## 🔍 Difference Between Compiler and Interpreter

| S.No | Interpreter | Compiler |
|------|-------------|----------|
| 1 | Executes line-by-line | Executes whole program |
| 2 | Gives result one line at a time | Gives output at once |
| 3 | Stops at first error | Checks all errors |
| 4 | No `.exe` file generated | Generates `.exe` if no error |
| 5 | Executes **source code** only | Executes **compiled file** |
| 6 | Scripting languages | Programming languages |
| 7 | Examples: Python, Shell, HTML, JS | Examples: C, C++, .NET C# |
| 8 | No `.exe` concept | Uses `.exe` |
| 9 | Open-source, modifiable | Not open-source (compiled) |

---

## ☕ About Java

Java uses **both Compiler and Interpreter**:

## Source Code → Byte Code → Binary Code → Processor → Output

- **Java Compiler**: Converts source code to byte code  
- **Java Interpreter**: Converts byte code to binary for execution

---

