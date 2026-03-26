import sys
import json
import os

#jason data is a list of dictionaries. So when writing json file, we need to dump a list.
#defining the positional variables
command = sys.argv[1]
id = sys.argv[2]
description = sys.argv[3]
status = sys.argv[4]
createdAt = sys.argv[5]
updatedAt = sys.argv[6]

task = {
    "id": 0,
    "description": "",
    "status": "",
    "createdAt": "",
    "updatedAt": ""
}
todo = []


def saveTask(task):
    if os.path.exists("todo.json"):
        with open("todo.json", "r") as file:
            data = json.load(file)
    else:
        data = []




    
    
    with open("todo.json", "w") as file:
        json.dump(data, file, indent=4)
    


def addTask(task, todo):
    description = sys.argv[3]
    sys.argv[4] = "not completed"
    createdAt = sys.argv[5]
    updatedAt = sys.argv[6]
   
    
    #update the task dictionary with the values from the command line arguments
    task["id"] += 1
    task["description"] = description
    task["status"] = "not completed"
    task["createdAt"] = createdAt
    task["updatedAt"] = updatedAt

    #append the task to the todo list
    todo.append(task)

    #save the task to the json file
    saveTask(task)



def update():
    sys.argv[1] = "update"

def delete():
    sys.argv[1] = "delete"

def view():
    sys.argv[1] = "view"

if command == "add":
    addTask(task, todo)
elif command == "update":
    update()
elif command == "delete":
    delete()
