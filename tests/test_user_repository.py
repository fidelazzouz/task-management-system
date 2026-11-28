import logging
import pytest

from app.models.user import User
from app.repositories.user_repository import (
    InMemoryUserRepository,
    SQLUserRepository,
    MongoUserRepository,
)


@pytest.fixture
def repository():
    return InMemoryUserRepository()


@pytest.fixture
def user():
    return User("fidel", "fidel@example.com")


def test_save_user(repository, user):
    repository.save(user)
    assert user in repository.users
    assert len(repository.users) == 1


def test_save_duplicate_user(repository, user):
    repository.save(user)
    repository.save(user)
    assert len(repository.users) == 1


def test_save_none_user(repository):
    with pytest.raises(ValueError, match="User cannot be None"):
        repository.save(None)


def test_sql_repository_save(user, caplog):
    repository = SQLUserRepository()
    with caplog.at_level(logging.INFO):
        repository.save(user)
    assert "Saving user fidel to SQL database" in caplog.text


def test_mongo_repository_save(user, caplog):
    repository = MongoUserRepository()
    with caplog.at_level(logging.INFO):
        repository.save(user)
    assert "Saving user fidel to MongoDB" in caplog.text
