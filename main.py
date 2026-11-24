from app.models import Task, Project, User

user = User("Ahmad", "ahmad@example.com")
project = Project("Website", "Company portfolio website")
task1 = Task("Design homepage", "Create main layout and UI", "High")
task2 = Task("setup Database", "Configure postgreSQL tables", "Medium")

project.add_task(task1)
project.add_task(task2)

user.add_project(project)

task1.status = "in_progress"
print("User:", user.username)
user.display_projects()
project.display_tasks()