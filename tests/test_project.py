import pytest

from app.models.project import Project
from app.models.task import Task


@pytest.fixture
def project():
    return Project("My Project", "Testing Project")


def test_project_name(project):
    assert project.name == "My Project"


def test_project_initial_tasks(project):
    assert project.tasks == []


def test_empty_project_name():
    with pytest.raises(ValueError, match="Project name cannot be empty"):
        Project("", "Testing Project")


def test_add_task(project):
    task = Task("Learn Python", "Study Python", "high")
    project.add_task(task)
    assert task in project.tasks
    assert len(project.tasks) == 1


def test_remove_task(project):
    task = Task("Learn Python", "Study Python", "high")
    project.add_task(task)
    project.remove_task(task)
    assert task not in project.tasks