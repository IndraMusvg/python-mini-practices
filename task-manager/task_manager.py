import datetime
import json



class Task:
    def __init__(self,task):
        self.task = task
        self.status = False
        self.creation_date = datetime.date.today()

    def mark_done(self):
        self.status = True

    def to_dict(self):
        return {
            "task": self.task,
            "status": self.status,
            "creation_date": str(self.creation_date),
        }

    def __str__(self):
        return f"{self.task} - status:  {self.status} - created: {self.creation_date}"


def add_task(tasks):
    task_title = input("Add the task to complete:")

    new_task = Task(task_title)

    tasks.append(new_task)

def task_list(tasks):
    if not tasks :
        print("The list is empty")
        return
    else:
        for number,task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

def mark_as_done(tasks):
    if not tasks:
        print("The list is empty")
        return
    task_list(tasks)
    try:  
        number_asked = int(input("Which task you completed?"))
        if 1<= number_asked <= len(tasks):
            tasks[number_asked - 1].mark_done()
        else:
         print("Your number is out of range")
            
    except ValueError:
                print("Don't use a letter")

def delete_task(tasks):
    if not tasks:
        print("The list is empty")
        return
    task_list(tasks)
    try:  
        number_asked = int(input("What task you want to remove?"))
        if 1<= number_asked <= len(tasks):
                tasks.remove(tasks[number_asked - 1])
        else:
            print("Your number is out of range")
                
    except ValueError:
            print("Don't use a letter")
            

file_path = "tasks.json"

def save_tasks(tasks):
    tasks_as_dicts = []
    for task in tasks:
        tasks_as_dicts.append(task.to_dict())
    with open(file_path, "w") as file:
        json.dump(tasks_as_dicts, file, indent=4)

def load_tasks():
    try:
         with open(file_path, "r") as file:
              data = json.load(file)
    except FileNotFoundError:  
         return[]
    except json.JSONDecodeError:
         return []
    loaded_tasks = []
    for item in data:
        new_task = Task(item["task"])
        new_task.status = item["status"]
        new_task.creation_date = datetime.date.fromisoformat(item["creation_date"])
        loaded_tasks.append(new_task)
    return loaded_tasks
    
tasks = []      

tasks = load_tasks()

while True:
    print("1.Add Task")
    print("2.Task List")
    print("3.Mark a Task")
    print("4.Delete Task")
    print("5.Exit")
    choose = input("Select an option:")
    if choose == "1":
        add_task(tasks)
        save_tasks(tasks)
    elif choose == "2":
        task_list(tasks)
    elif choose == "3":
        mark_as_done(tasks)
        save_tasks(tasks)
    elif choose == "4":
        delete_task(tasks)
        save_tasks(tasks)
    elif choose == "5":
        break
    else:
        print("That option is not here")