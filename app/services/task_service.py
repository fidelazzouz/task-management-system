class TaskService:

    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task, status):
        task.update_status(status)

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks
