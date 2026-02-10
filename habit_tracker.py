import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


def menu(currenttasks, name):
    while True:
        print(f"\nHello {name}! What do you want to do today?")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nYour tasks:")
            for task in currenttasks:
                print("-", task)

        elif choice == "2":
            addtask = input("You can add a new task here: ")
            if addtask:
                currenttasks.append(addtask)
                save_tasks(currenttasks)
                print("Task added successfully!")

        elif choice == "3":
            removetask = input("Type the task you want to remove: ")
            if removetask in currenttasks:
                currenttasks.remove(removetask)
                save_tasks(currenttasks)
                print("Task removed successfully!")
            else:
                print("Task not found!")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")


def habittracker():
    currenttasks = load_tasks()

    print("Welcome to Habit Tracker & To-Do Manager!")
    name = input("What is your name? ")

    menu(currenttasks, name)


habittracker()