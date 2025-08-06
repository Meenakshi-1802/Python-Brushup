# 📘 Chapter 5: Python Installation and Versions

This chapter will guide you through the complete setup of Python on your system. It includes downloading and installing Python, understanding the two main modes (Interactive and Script), running Python from the command line, using IDLE, performing basic operations (addition, subtraction, multiplication, and division), and installing PyCharm & VS Code for development.

---

## ✅ 1. Python Installation on Windows

### Step 1: Download Python

- Visit the official Python website: https://www.python.org/downloads
- Click on the latest version available for Windows.
- Download the appropriate installer, such as `python-3.13.5-amd64.exe`.

### Step 2: Install Python

- Move the downloaded file to the `C:\` drive.
- Right-click the installer → Select **Run as Administrator** → Click **Yes**.
- Make sure to check the box that says **Add Python to PATH**.
- Click **Install Now**.
- Once the installation is complete, click **Close**.

### Step 3: Verify Python Installation

- Open the **Command Prompt**.
- Type the command to check if Python is installed successfully.
- The version number will be displayed if everything is correct.

---

## 🧠 2. What is IDLE?

- **IDLE** stands for **Integrated Development and Learning Environment**.
- It is a simple editor that comes with Python installation.
- IDLE supports two ways to work:
  - **Interactive Mode** – for testing code quickly
  - **Script Mode** – for writing and saving full programs

---

## 💡 3. Interactive Mode

- In this mode, you type Python commands directly and get the result immediately.
- Used mainly for quick testing or learning.
- You can open it through **Command Prompt** or by launching **IDLE**.

---

## 📝 4. Script Mode

- In Script Mode, you write full Python programs and save them with the `.py` extension.
- These scripts can be saved and run multiple times.
- This mode is preferred for writing business logic or larger programs.
- You can use IDLE or any text editor like Notepad, Notepad++, or an IDE.

---

## ➕➖✖️➗ 5. Basic Python Operations

Python supports all basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

These operations are the foundation of any logic building in Python and are essential for data processing.

---

## 📦 6. What is pip?

- **pip** stands for **Pip Installs Packages**.
- It is Python’s built-in package manager.
- It is used to install and manage additional libraries and tools.
- You can install libraries like NumPy, Pandas, Matplotlib, etc., using pip.
- pip is installed automatically when you install Python from python.org.

---

## 💻 7. Running Python Scripts via Command Line

- Python files with `.py` extension can be executed directly from the Command Prompt.
- This allows you to test scripts without opening any editor or IDE.
- You must navigate to the folder where your script is saved and then run it.

---

## 🔧 8. Installing PyCharm IDE

### Step 1: Download PyCharm

- Go to: https://www.jetbrains.com/pycharm/download
- Download the **Community Edition** (free version).

### Step 2: Install PyCharm

- Move the setup file to the `C:\` drive.
- Right-click → Select **Run as Administrator** → Click **Yes**.
- Follow the installation wizard:
  - Click **Next**
  - Check all boxes (like creating a shortcut, associating `.py` files, etc.)
  - Choose a folder for installation (e.g., JetBrains)
  - Click **Install**

### Step 3: Launch PyCharm

- After installation, launch PyCharm from the desktop shortcut.
- Accept terms and conditions.
- Choose default settings or customize as per your preference.

---

## 🧪 9. Creating Your First Project in PyCharm

- Click on **New Project**.
- Set the location to something like `D:\mypython`.
- Select **New Environment using virtualenv**.
- Click **Create**.

---

## 🎨 10. Customizing PyCharm for Better Use

- **Appearance Theme**: File → Settings → Appearance → Choose `Win10 Lite`
- **Font Size**: File → Settings → Editor → Font → Set font size (e.g., 20)
- **Color Scheme**: Editor → Color Scheme → Choose `Classic Light`

---

## 🔍 11. Enabling IntelliSense in PyCharm

- File → Settings → Plugins
- Search for and install **PyLint**
- Restart PyCharm to activate auto-suggestions and error checking

---

## 📝 12. Writing Your First Python File in PyCharm

- Right-click on your project folder → Select `New → Python File`
- Name the file (e.g., `test.py`)
- Open the file and start writing your Python program
- Right-click on the file → Select `Run`

---

## 🧩 13. Setting Up VS Code (Visual Studio Code)

VS Code is a lightweight, beginner-friendly code editor that supports Python and has built-in Git integration.

### 🔽 Step 1: Download & Install

- Visit: https://code.visualstudio.com/
- Click on **Download for Windows**
- Run the installer and complete the installation with default settings

### 🔌 Step 2: Install Python Extension

- Open VS Code
- Click on the **Extensions icon** (left sidebar)
- Search for `Python` by Microsoft
- Click **Install**

### 🧠 Step 3: Optional – Git Integration

To push code to GitHub directly from VS Code:

1. Install **Git for Windows**: https://git-scm.com/
2. Restart your system after installation
3. Open VS Code and load your Python project folder
4. Click on the **Source Control icon**
5. Sign in to GitHub via the bottom-left account icon
6. Initialize repository, commit your changes, and push to GitHub

✅ Now you're coding, tracking changes, and uploading to GitHub — all from VS Code!

---

## 🏁 Summary

| Task                             | Tool              | Purpose                                      |
|----------------------------------|-------------------|----------------------------------------------|
| Install Python                   | python.org        | Set up Python on your system                 |
| Use IDLE                         | Built-in          | Write and run Python interactively or in files |
| Perform Basic Operations         | Python Shell/IDLE | Understand arithmetic with Python            |
| Manage Packages                  | pip               | Install libraries like numpy, pandas, etc.   |
| Run Scripts from Command Line    | CMD               | Execute Python files easily                  |
| Install and Use PyCharm          | JetBrains PyCharm | Write, run, and manage large Python projects |
| Install and Use VS Code          | VS Code           | Lightweight editor + GitHub integration      |
| Customize Editor                 | Settings Panel    | Improve readability and productivity         |
| Enable IntelliSense              | PyLint Plugin     | Auto-suggestions and error detection         |

---

🎯 You’re now fully set up and ready to explore the world of Python development — from writing your first line of code to uploading real projects to GitHub!

