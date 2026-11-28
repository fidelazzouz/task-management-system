import pytest

from app.models.project import Project
from app.models.task import Task
from app.services.project_service import ProjectService


@pytest.fixture
def service():
    return ProjectService()


@pytest.fixture
def project():
    return Project("Test Project", "Testing ProjectService")


@pytest.fixture
def task():
    return Task("Learn Python", "Study Python", "high")


def test_create_project(service, project):
    service.create_project(project)
    assert project in service.projects
    assert len(service.projects) == 1


def test_create_duplicate_project(service, project):
    service.create_project(project)
    service.create_project(project)
    assert len(service.projects) == 1


def test_add_task_to_project(service, project, task):
    service.create_project(project)
    service.add_task_to_project(project, task)
    assert task in project.tasks


def test_add_task_to_nonexistent_project(service, project, task):
    with pytest.raises(ValueError, match="Project does not exist"):
        service.add_task_to_project(project, task)


def test_delete_project(service, project):
    service.create_project(project)
    service.delete_project(project)
    assert project not in service.projects


def test_delete_nonexistent_project(service, project):
    service.delete_project(project)
    assert project not in service.projects


def test_get_all_projects_returns_copy(service, project):
    service.create_project(project)
    projects = service.get_all_projects()
    projects.clear()
    assert len(service.projects) == 1
