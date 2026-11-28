import pytest

from app.models.task import Task, InvalidTaskStatusError
from app.services.task_service import TaskService


@pytest.fixture
def service():
    return TaskService()


@pytest.fixture
def task():
    return Task(
        title="Learn Pytest",
        description="Study Unit Testing",
        priority="high",
    )


def test_create_task(service, task):
    service.create_task(task)
    assert len(service.tasks) == 1
    assert task in service.tasks


def test_create_duplicate_task(service, task):
    service.create_task(task)
    service.create_task(task)
    assert len(service.tasks) == 1


def test_update_task_status(service, task):
    service.create_task(task)
    service.update_task_status(task, "in_progress")
    assert task.status == "in_progress"


def test_update_task_status_invalid(service, task):
    service.create_task(task)
    with pytest.raises(InvalidTaskStatusError):
        service.update_task_status(task, "invalid")
    assert task.status == "todo"


def test_update_task_not_in_service(service, task):
    with pytest.raises(ValueError, match="Task does not exist"):
        service.update_task_status(task, "done")


def test_delete_task(service, task):
    service.create_task(task)
    service.delete_task(task)
    assert task not in service.tasks
    assert len(service.tasks) == 0


def test_get_all_tasks(service):
    task1 = Task("Task 1", "Description 1", "high")
    task2 = Task("Task 2", "Description 2", "medium")
    service.create_task(task1)
    service.create_task(task2)
    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert task1 in tasks
    assert task2 in tasks


def test_get_all_tasks_returns_copy(service, task):
    service.create_task(task)
    tasks = service.get_all_tasks()
    tasks.clear()
    assert len(service.tasks) == 1
