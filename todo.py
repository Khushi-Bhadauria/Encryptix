import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

tasks = load_tasks()

def show():
    for i, t in enumerate(tasks, 1):
        status = "✅" if t['done'] else "❌"
        print(f"{i}. {t['task']} - {status}")

while True:
    print("\n1. Add\n2. Show\n3. Done\n4. Delete\n5. Exit")
    c = input("Choose: ")

    if c == "1":
        t = input("Enter task: ")
        tasks.append({"task": t, "done": False})
        save_tasks()

    elif c == "2":
        show()

    elif c == "3":
        show()
        i = int(input("Mark task #: ")) - 1
        if 0 <= i < len(tasks):
            tasks[i]["done"] = True
            save_tasks()

    elif c == "4":
        show()
        i = int(input("Delete task #: ")) - 1
        if 0 <= i < len(tasks):
            tasks.pop(i)
            save_tasks()

    elif c == "5":
        break
