# Danny Maurer
""" This class will be the menu for the planner. This will serve as the model
when a UI is created"""

import sys
from planner import Planner

class Menu:

    def __init__(self):
        self.planner = Planner() # creates a planner in the menu
        self.choices = {
            "1": self.show_tasks,
            "2": self.search_tasks,
            "3": self.add_task,
            "4": self.modify_task,
            "5": self.complete_task,
            "6": self.quit,
        }

    def display_menu(self):
        print(
            """
Planner Menu:

1. Show tasks
2. Search tasks
3. Add task
4. Edit task
5. Complete task
6. Quit
"""
            )

    def run(self):
        """ Display menu and choose an action"""
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice) # selects the action based on the given choice in the init function
            if action:
                action()
            else:
                print("{0} is not a valid option".format(choice))

    def show_tasks(self, tasks = None):
        if not tasks:
            tasks = self.planner.planner
        for task in tasks:
            print("{0}: {1} \nDue Date: {2}".format(task.id, task.name, task.dueDate))

    def search_tasks(self):
        filter = input("Search for: ")
        tasks = self.planner.search(filter)
        self.show_tasks(tasks)

    def add_task(self):
        name = input("What is the task: ")
        dueDate = input("When is it due: ")
        self.planner.new_task(name, dueDate)
        print("Your task has been added to the planner.")

    def modify_task(self):
        task_id = input("Enter the task id: ")
        name = input("Enter the new task name: ")
        dueDate = input("Enter the new due date: ")
        if name:
            self.planner.modify_name(task_id, name)
        if dueDate:
            self.planner.modify_dueDate(task_id, dueDate)

    def complete_task(self):
        task_id = input("Enter the task id: ")
        complete = input("Enter {y}es for complete and {n}o for not complete").strip().lower()
        if complete == "y":
            self.planner.modify_isComplete(task_id, True)
        else:
            self.planner.modify_isComplete(task_id, False)

    def quit(self):
        print("Thank you for planning ahead.")
        sys.exit(0)

run = int(input("Enter tne number 1 to run: "))
if run == 1:
    m = Menu()
    m.run()
        
        




                
