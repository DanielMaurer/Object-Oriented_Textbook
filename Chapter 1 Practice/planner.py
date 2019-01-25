# Danny Maurer
""" This project will be an application to track things that I have to do.
The user will be able to create an event, mark its priority, then say when
the event is complete.

Task
    Constructor
        Name
        dueDate
        isComplete
        id
    match

Planner
    Constructor
        new array
    new Task
    modify name
    modify due-date
    modify is complete
    search
"""

last_id = 0

class Task:
    """This will be what is contained in the planner. Each task has a name,
    due date, and an is complete"""

    def __init__(self, name, dueDate):
        """ Initialize a task with a name, and due date. Is complete will be set
        to false."""
        self.name = name
        self.dueDate = dueDate
        self.isComplete = False
        # The id will help locate the task in the planner
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if the task the user is searching for is a match"""
        return filter in self.name or filter in self.dueDate

class Planner:
    """The planner will house the tasks. Tasks will be created, modified and
    searched here"""

    def __init__(self):
        """Notebook starts as an empty list"""
        self.planner = []

    def new_task(self, name, dueDate):
        """ Creates a new task and adds it to the planner"""
        self.planner.append(Task(name, dueDate))

    def modify_name(self, task_id, name):
        """ Use the ID to find a task and then change its name"""
        for task in self.planner:
            if task.id == task_id: # if the task ID matched the designated ID
                task.name = name

    def modify_dueDate(self, task_id, dueDate):
        """ Use the ID to find a task and change its due date"""
        for task in self.planner:
            if task.id == task_id:
                task.dueDate == dueDate

    def modify_isComplete(self, task_id, isComplete):
        """ Use the task ID to find a task and change if it is complete or not"""
        for task in self.planer:
            if task.id == task_id:
                task.isComplete == isComplete

    def search(self, filter):
        """ Find all of the tasks that match the filter"""
        return [task for task in self.planner if task.match(filter)] # Search all of the tasks in the planner and return those whose name or dueDate matches

    
                
        











    
    
