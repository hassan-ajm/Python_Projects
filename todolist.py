import json 

FILE = "task.json"

def load_task():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] 

def save_task(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    new_task = input("Enter the task: ")
    new_id = tasks[-1]["id"] + 1 if tasks else 1 
    tasks.append({"id": new_id, "task": new_task, "done": False})
    save_task(tasks)
    print(f"Task '{new_task}' added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("NO Task Yet")
        return
    else:
        for t in tasks:
            status = "Done" if t["done"] else "Pending"
            # FIX: Used '{status}' directly instead of '{t[status]}', and used single quotes for inner dictionary keys
            print(f"ID: {t['id']}, Task: {t['task']}, Status: {status}")

def mark_task_done(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("Enter the ID of the task to be marked as Done: "))
        for t in tasks:
            if t["id"] == task_id:
                t["done"] = True
                save_task(tasks)
                print(f"Task '{t['task']}' marked as Done!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("Enter the ID of the task to be deleted: "))
        for t in tasks:
            if t["id"] == task_id:
                tasks.remove(t)
                save_task(tasks)
                print(f"Task '{t['task']}' deleted successfully!")
                return  # FIX: Added 'return' so it exits once deleted and avoids falling through
        print("Task ID not found.")  # FIX: Cleaned up loop-else structure to correctly report missing IDs
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

tasks = load_task()
print("===================To DO List===================")

while True:
    print("\n1) Add  2) List  3) Done  4) Delete  q) Quit")

    choice = input("Choice: ")
    if choice == "1": 
        add_task(tasks)
    elif choice == "2": 
        list_tasks(tasks)
    elif choice == "3": 
        mark_task_done(tasks)  # FIX: Corrected function call from 'mark_done' to 'mark_task_done'
    elif choice == "4": 
        delete_task(tasks)
    elif choice == "q":
        print("Goodbye.")
        break
    else: 
        print("Invalid choice.")