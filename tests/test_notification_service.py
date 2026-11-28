import logging
import pytest

from app.models.user import User
from app.services.notification_service import NotificationService


@pytest.fixture
def service():
    return NotificationService()


@pytest.fixture
def user():
    return User("fidel", "fidel@example.com")


def test_send_welcome_email(service, user, caplog):
    with caplog.at_level(logging.INFO):
        service.send_welcome_email(user)
    assert "Welcome email notification prepared for: fidel@example.com" in caplog.text


def test_send_welcome_email_none_user(service):
    with pytest.raises(ValueError, match="User cannot be None"):
        service.send_welcome_email(None)
