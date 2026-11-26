class Task:

    ALLOWED_STATUSES = ("todo", "in_progress", "done")
    ALLOWED_PRIORITIES = ("low", "medium", "high")

    def __init__(self, title, description, priority):

        if not title.strip():
            raise ValueError("Task title cannot be empty")

        if priority not in self.ALLOWED_PRIORITIES:
            raise ValueError("Invalid priority")

        self.title = title
        self.description = description
        self.priority = priority
        self.status = "todo"

    def update_status(self, new_status):

        if new_status not in self.ALLOWED_STATUSES:
            raise ValueError("Invalid status")

        self.status = new_status

    def __str__(self):
        return (
            f"Task: {self.title}\n"
            f"Description: {self.description}\n"
            f"Priority: {self.priority}\n"
            f"Status: {self.status}"
        )
