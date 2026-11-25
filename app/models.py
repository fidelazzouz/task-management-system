class Task:

    ALLOWED_STATUSES = ("todo", "in_progress", "done")
    ALLOWED_PRIORITIES = ("low", "medium", "high")
    
    def __init__(self, title, description, priority):
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "todo"

    def __str__(self):
       return f"Task: {self.title} | Priority: {self.priority} | Status: {self.status}"

    def __repr__(self):
        return (
            f"Task(title={self.title!r}, "
            f"priority={self.priority!r}, "
            f"status={self.status!r})"
        )
    @classmethod
    def get_allowed_statuses(cls):
        return cls.ALLOWED_STATUSES
    
    @classmethod
    def get_allowed_priorities(cls):
        return cls.ALLOWED_PRIORITIES
    
    @classmethod
    def is_valid_priority(cls, priority):
        return priority in cls.ALLOWED_PRIORITIES
    
    @classmethod
    def is_valid_status(cls, status):
        return status in cls.ALLOWED_STATUSES
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_status):
        if new_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid task status")
        self._status = new_status

    @property
    def priority(self):
        return self._priority
    
    @priority.setter
    def priority(self, new_priority):
        if new_priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Invalid task priority")

        self._priority = new_priority
    
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

