import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class UserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.users = []

    def save(self, user):
        if user is None:
            raise ValueError("User cannot be None")

        if user in self.users:
            logger.warning("User already exists: %s", user.username)
            return

        self.users.append(user)
        logger.info("User %s saved in memory", user.username)


class SQLUserRepository(UserRepository):

    def save(self, user):
        if user is None:
            raise ValueError("User cannot be None")

        logger.info("Saving user %s to SQL database", user.username)


class MongoUserRepository(UserRepository):

    def save(self, user):
        if user is None:
            raise ValueError("User cannot be None")

        logger.info("Saving user %s to MongoDB", user.username)
