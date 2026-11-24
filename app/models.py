class Task:

    ALLOWED_STATUSES = ("todo", "in_progress", "done")
    
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "todo"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid task status")
        self._status = new_status

    def display(self):
        print("Title:", self.title)
        print("Description:", self.description)
        print("Priority:", self.priority)
        print("Status:", self.status)
        
    def complete(self):
        self.status = "done"

class Project:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def display_tasks(self):
        for task in self.tasks:
            task.display()

class User:
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.projects = []
    
    def add_project(self, project):
        self.projects.append(project)
    
    def display_projects(self):
        if not self.projects:
            print("No projects found")
            return
        
        print("User:", self.username)
        for project in self.projects:
            print("Project:", project.name)
            print("Description:", project.description)

