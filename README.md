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

### Setup

 1. Install Python

 2. Install Required Library.

Open terminal and run:

```
pip install pyttsx3
```

## To Run the Project

1. Open terminal in the project folder
2. Run the program:
3. 2 Options will be visible-1)Add task
                             2)Start Reminder

4.Select option 1
* Enter task name
* Enter date & time in format.

5.Start Reminder System
* Select option 2
* The system will:

  * Continuously check time
  * Trigger reminder when time matches
    
6.* Displays message on screen.
* Speaks using voice.
* tasks.json will be created automatically if not present.

## Author

Name: Saanya Mittal
Reg No.-25BCE10570


##  Conclusion

This project demonstrates basic automation, file handling, and time-based execution in Python, along with an interactive voice alert system, forming a strong base for future AI enhancements.
