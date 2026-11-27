import pytest

from app.models.task import Task, InvalidTaskStatusError


def test_task_initial_status():
    task = Task("Learn Python", "Study Unit Testing", "high")

    assert task.status == "todo"


def test_task_initial_title():
    task = Task(
        title="Learn OOP",
        description="Study Object Oriented Programming",
        priority="medium",
    )

    assert task.title == "Learn OOP"


def test_task_initial_priority():
    task = Task(
        title="Learn OOP",
        description="Study Object Oriented Programming",
        priority="high",
    )

    assert task.priority == "high"


def test_empty_title():
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(
            title="",
            description="Testing empty title",
            priority="high",
        )


@pytest.mark.parametrize("priority", ["urgent", "critical", "normal"])
def test_invalid_priorities(priority):
    with pytest.raises(ValueError, match="Invalid task priority"):
        Task(
            title="Test",
            description="Testing invalid priority",
            priority=priority,
        )


@pytest.mark.parametrize("status", ["todo", "in_progress", "done"])
def test_valid_status_update(status):
    task = Task("Test", "Description", "high")

    task.update_status(status)

    assert task.status == status


def test_invalid_status_update():
    task = Task("Test", "Description", "high")

    with pytest.raises(InvalidTaskStatusError):
        task.update_status("invalid")

    assert task.status == "todo"
