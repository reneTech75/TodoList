import json #we need this to read and write our tasks to a json file
import os #we need this to check if the tasks file exists and to create it if it doesn't 
import sys #we need this because we shall be using command line arguments to add, list, and delete tasks
from datetime import datetime #we need this to add timestamps to our tasks

#sys.argv is a list in Python, which contains the command-line arguments passed to the script.
# The first element, sys.argv[0], is the name of the script itself. The subsequent elements are the arguments passed to the script.
# For example, if you run the script like this:
# python task_cli.py add "Buy groceries"
# Then sys.argv will be:
# ['task_cli.py', 'add', 'Buy groceries']
# In this case, sys.argv[1] will be 'add' and sys.argv[2] will be 'Buy groceries'.
#sys.argv[1] will be the command (add, list, delete, update) and sys.argv[2] will be the task description or task id depending on the command.
#sys.argv[3] will be the new description for the update command.
# We will use these command line arguments to determine what action to take (add, list, delete, update) and to get the necessary information for that action (task description or task id).







FILE_NAME = "tasks.json" #this is the name of the file where we will store our tasks

#----------------FILE HANDLING FUNCTIONS----------------#

def load_task():
    #This function will will read from the json file and return the data read
    #If the json file does not exist already, it will create one, and return an empty list.
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file) #we create an empty list in the json file to store our tasks
        return []
    
    with open(FILE_NAME, 'r') as file:
        data = json.load(file) #we read the data from the json file and return it
    return data
    
def save_task(tasks):
    #This function will take a list of tasks as an argument and write it to the json file.
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4) #we write the tasks to the json file with an indentation of 4 for better readability

def update_task(task_id, new_description):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #we update the timestamp of the task to the current time
            save_task(tasks)
            print("Task updated successfully.")

def delete_task(task_id):
    tasks = load_task()
    #tasks = [task for task in tasks if task["id"] != task_id] #we create a new list of tasks that does not include the task with the given id
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task) #we remove the task with the given id from the list of tasks
            save_task(tasks)
            print("Task deleted successfully.") 

def change_status(task_id, status):
    tasks = load_task()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #we update the timestamp of the task to the current time
            save_task(tasks)
            print("Task status updated successfully.")
            return
    print("Task not found.") #if we do not find the task with the given id, we print this message
    
def add_task(description):
    tasks = load_task()
    task_id = len(tasks) + 1 #we generate a new id for the task by taking the length of the current list of tasks and adding 1 to it
    new_task = {
        "id": task_id,
        "description": description,
        "status": "pending", #we set the default status of a new task to pending
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #we add a timestamp to the task when it is created
        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S") #we also add a timestamp for when the task is updated, which will be the same as the createdAt timestamp when the task is first created
    }
    tasks.append(new_task) #we add the new task to the list of tasks
    save_task(tasks) #we save the updated list of tasks to the json file
    print("Task added successfully.")


def get_next_id(tasks):
    return len(tasks) + 1 #we generate a new id for the task by taking the length of the current list of tasks and adding 1 to it

def list_tasks(filter_status=None):
    tasks = load_task()
    if filter_status is not None:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}, Created At: {task['createdAt']}, Updated At: {task['updatedAt']}")

#Main function that will be called when the script is run.
def main():
    if len(sys.argv) < 2:
        print("Please provide a command (add, list, delete, update, status).")
        return
    command = sys.argv[1]
    if command == "add":
        if len(sys.argv)< 3:
            print("please provide a description for the task.")
            return
        add_task(sys.argv[2])
    elif command == "update":
        if len(sys.argv) < 4:
            print("Please provide a task id and a new description for the task.")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Please provide a task id to delete.")
            return
        delete_task(int(sys.argv[2]))
    elif command == "mark-in-progress":
        if len(sys.argv) < 3:
            print("Please provide a task id to mark as in progress.")
            return
        change_status(int(sys.argv[2]), "in-progress")
    elif command == "mark-done":
        if len(sys.argv) < 3:
            print("Please provide a task id to mark as done.")
            return
        change_status(int(sys.argv[2]), "done")
    elif command == "list":
        if len(sys.argv) == 2:
            list_tasks()
        else:
            status = sys.argv[2]
            list_tasks(status)
    else:
        print("Invalid command. Please use add, list, delete, update, mark-in-progress, or mark-done.")



if __name__ == "__main__":
    main()