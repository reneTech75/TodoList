import json #we need this to read and write our tasks to a json file
import os #we need this to check if the tasks file exists and to create it if it doesn't 
import sys #we need this because we shall be using command line arguments to add, list, and delete tasks
from datetime import datetime #we need this to add timestamps to our tasks

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
    tasks = load_task():
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #we update the timestamp of the task to the current time
            save_task(tasks)
            print("Task updated successfully.")


#Main function that will be called when the script is run.
def main():
    


if __name__ == "__main__":
    main()