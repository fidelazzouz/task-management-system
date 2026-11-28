import pytest
from unittest.mock import Mock

from app.models.user import User
from app.services.registration_service import RegistrationService


@pytest.fixture
def repository():
    return Mock()


@pytest.fixture
def service(repository):
    return RegistrationService(repository)


@pytest.fixture
def user():
    return User("fidel", "fidel@example.com")


def test_register_user(service, repository, user):
    service.register(user)
    repository.save.assert_called_once_with(user)


def test_register_none_user(service):
    with pytest.raises(ValueError, match="User cannot be None"):
        service.register(None)


def test_registration_service_without_repository():
    with pytest.raises(ValueError, match="Repository cannot be None"):
        RegistrationService(None)
