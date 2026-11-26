class Project:

    def __init__(self, name, description):

        if not name.strip():
            raise ValueError("Project name cannot be empty")

        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def display_tasks(self):
        for task in self.tasks:
            print(task)
