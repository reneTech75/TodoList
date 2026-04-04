This is a cli only program for a todo list. The purpose is to practice the foundational principles of CRUD,
 and most importantly, creating a CLI for a technical team. I will not use an actual database, 
 but rather a JSON file to hold all the data. It is easy to later transfer all that data into
  a database





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
 
 the project url is : https://roadmap.sh/projects/task-tracker