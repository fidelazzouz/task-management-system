import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

from app.models import Task, User, Project

from app.services import (
    TaskService,
    ProjectService,
    RegistrationService,
    NotificationService,
    ProfileReportGenerator,
)

from app.repositories import InMemoryUserRepository

# Create user
user = User("fidel", "fidel@example.com")


# Create project
project = Project("Task Management", "My first software engineering project")

user.add_project(project)


# Create tasks
task1 = Task("Learn Python", "Study modules and packages", "high")

task2 = Task("Learn SOLID", "Practice SOLID principles", "medium")


# Task Service
task_service = TaskService()

task_service.create_task(task1)
task_service.create_task(task2)


# Project Service
project_service = ProjectService()

project_service.create_project(project)

project_service.add_task_to_project(project, task1)
project_service.add_task_to_project(project, task2)


# Update task
task_service.update_task_status(task1, "in_progress")


# User Registration
repository = InMemoryUserRepository()

registration_service = RegistrationService(repository)

registration_service.register(user)


# Notification
notification_service = NotificationService()

notification_service.send_welcome_email(user)


# Profile Report
report = ProfileReportGenerator()

report.generate_profile_report(user)


# Display tasks
print("\nProject Tasks:")

project.display_tasks()
