from app.models import Task, Project, User

task = Task("Build API", "Create login API", "high")

print(task)
print(repr(task))

task.priority = "medium"
task.status = "in_progress"

print(task)

task.complete()
print(task)

print(Task.get_allowed_statuses())
print(Task.get_allowed_priorities())
print(Task.is_valid_priority("urgent"))