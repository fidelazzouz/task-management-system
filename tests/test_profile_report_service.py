import pytest

from app.models.user import User
from app.models.project import Project
from app.services.profile_report_service import ProfileReportGenerator


@pytest.fixture
def user():
    user = User("fidel", "fidel@example.com")
    user.add_project(Project("Task Management", "Testing project"))
    return user


@pytest.fixture
def report_generator():
    return ProfileReportGenerator()


def test_generate_profile_report(report_generator, user):
    report = report_generator.generate_profile_report(user)
    assert "fidel" in report
    assert "fidel@example.com" in report
    assert "Projects: 1" in report


def test_generate_report_without_projects(report_generator):
    user = User("test", "test@example.com")
    report = report_generator.generate_profile_report(user)
    assert "Projects: 0" in report


def test_generate_report_with_none_user(report_generator):
    with pytest.raises(ValueError, match="User cannot be None"):
        report_generator.generate_profile_report(None)
