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
        return (
            f"Task: {self.title} | "
            f"Priority: {self.priority} | "
            f"Status: {self.status}"
        )

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

    def complete(self):
        self.status = "done"


class BugTask(Task):

    def __init__(self, title, description, priority, bug_severity):
        super().__init__(title, description, priority)
        self.bug_severity = bug_severity

    def __str__(self):
        return f"{super().__str__()} | Severity: {self.bug_severity}"


class MeetingTask(Task):

    def __init__(self, title, description, priority, meeting_date):
        super().__init__(title, description, priority)
        self.meeting_date = meeting_date

    def __str__(self):
        return f"{super().__str__()} | Date: {self.meeting_date}"


class Project:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)


class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.projects = []

    def update_email(self, new_email):
        self.email = new_email

    def add_project(self, project):
        self.projects.append(project)
