
from app.models import (
    Task,
    BugTask,
    MeetingTask,
    Project,
    User
)

from app.services import (
    InMemoryUserRepository,
    SQLUserRepository,
    MongoUserRepository,
    RegistrationService,
    NotificationService,
    ProfileReportGenerator,
    DeliveryCalculator,
    NormalDelivery,
    ExpressDelivery,
    SameDayDelivery
)


# =========================
# 1. Create User
# =========================

user = User("Ahmad", "ahmad@example.com")


# =========================
# 2. Create Project
# =========================

project = Project(
    "Software Project",
    "Task Management System"
)


# =========================
# 3. Create Tasks
# =========================

task1 = Task(
    "Create login",
    "Build login functionality",
    "high"
)

task2 = BugTask(
    "Fix login bug",
    "Login fails with invalid input",
    "high",
    "critical"
)

task3 = MeetingTask(
    "Team meeting",
    "Discuss project progress",
    "medium",
    "2026-11-26"
)


# =========================
# 4. Add Tasks to Project
# =========================

project.add_task(task1)
project.add_task(task2)
project.add_task(task3)


# =========================
# 5. Add Project to User
# =========================

user.add_project(project)


# =========================
# 6. Update Task Status
# =========================

task1.status = "in_progress"
task2.complete()


# =========================
# 7. Display Tasks
# =========================

print("\n--- Project Tasks ---")

for task in project.tasks:
    print(task)


# =========================
# 8. Test DIP and Dependency Injection
# =========================

print("\n--- User Registration ---")

repository = InMemoryUserRepository()

registration_service = RegistrationService(repository)
registration_service.register(user)


# Try SQL Repository

sql_repository = SQLUserRepository()

registration_service = RegistrationService(sql_repository)
registration_service.register(user)


# Try Mongo Repository

mongo_repository = MongoUserRepository()

registration_service = RegistrationService(mongo_repository)
registration_service.register(user)


# =========================
# 9. Test Other Services
# =========================

print("\n--- User Services ---")

notification = NotificationService()
notification.send_welcome_email(user)

report = ProfileReportGenerator()
report.generate_profile_report(user)


# =========================
# 10. Test OCP
# =========================

print("\n--- Delivery Calculator ---")

calculator = DeliveryCalculator()

print("Normal:", calculator.calculate(NormalDelivery()))
print("Express:", calculator.calculate(ExpressDelivery()))
print("Same Day:", calculator.calculate(SameDayDelivery()))
