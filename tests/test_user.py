import pytest

from app.models.user import User
from app.models.project import Project


@pytest.fixture
def user():
    return User("fidel", "fidel@example.com")


def test_user_username(user):
    assert user.username == "fidel"


def test_user_email(user):
    assert user.email == "fidel@example.com"


def test_user_initial_projects(user):
    assert user.projects == []


def test_update_email(user):
    user.update_email("new@example.com")
    assert user.email == "new@example.com"


def test_update_email_empty(user):
    with pytest.raises(ValueError, match="Email cannot be empty"):
        user.update_email("")


def test_add_project(user):
    project = Project("Test Project", "Testing project")
    user.add_project(project)
    assert project in user.projects
    assert len(user.projects) == 1
