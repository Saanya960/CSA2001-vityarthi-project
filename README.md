# CSA2001-vityarthi-project
# AI Task Reminder System

## Project Overview

It is a Python-based application designed to help users manage their daily tasks efficiently. It allows users to schedule tasks with a specific date and time and provides reminders through both text notifications and voice alerts.

This project focuses on improving productivity by ensuring that important tasks are not forgotten, even if the user is not actively looking at their screen.

---

##  Features

* Add tasks with date and time
* Store tasks permanently using a JSON file
* Automatic time-based reminder system
* Voice alert using text-to-speech
* Supports multiple tasks

---

##  Technologies Used

* Python
* Libraries:

  * `datetime`
  * `time`
  * `json`
  * `pyttsx3`

---

### Setup Instructions

### 1. Install Python

### 2. Install Required Library

Open terminal/command prompt and run:

```
pip install pyttsx3
```

### 4. Project Structure

```
ai-reminder/
─ main.py
─ tasks.json
```

---

##  How to Run the Project

1. Open terminal in the project folder
2. Run the program:

```
python main.py
```

3. You will see options:

```
1. Add Task
2. Start Reminder
```

---

## How to Use

###  Add Task

* Select option **1**
* Enter task name
* Enter date & time in format:

```
YYYY-MM-DD HH:MM
```

Example:

```
2026-03-28 18:30
```

---

### ➤ Start Reminder System

* Select option **2**
* The system will:

  * Continuously check time
  * Trigger reminder when time matches

---

## 🔔 Reminder Output

* Displays message on screen:

```
Reminder: Study AI
```

* Speaks using voice:

```
"Reminder: Study AI"
```

---

* Ensure correct time format while entering tasks
* `tasks.json` will be created automatically if not present

---

---

## Author

Name: Saanya Mittal
Reg No.-25BCE10570

---

##  Conclusion

This project demonstrates basic automation, file handling, and time-based execution in Python, along with an interactive voice alert system, forming a strong base for future AI enhancements.
