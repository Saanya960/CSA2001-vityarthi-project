import json
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def add_task():
    task=input("Enter task ")
    time=input("Enter time(YYYY-MM-DD HH:MM) ")
    

    task_data={
        "task":task,
        "time":time,
    }

    try:
        with open("tasks.json","r") as file:
            tasks=json.load(file)
    except:
        tasks=[]

    tasks.append(task_data)

    with open("tasks.json","w")as file:
        json.dump(tasks,file,indent=4)
    
    print("Task added")

import time

def check_tasks():
    while True:
        now = datetime.now().strftime("%Y-%m-%d %H:%M")

        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
        except:
            tasks = []

        for task in tasks:
            if task["time"] == now:
                speak(f"🔔 Reminder: {task['task']}")

if __name__ == "__main__":
    while True:
        print("\n1. Add Task\n2. Start Reminder")
        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            check_tasks()