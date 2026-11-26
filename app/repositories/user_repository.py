from abc import ABC, abstractmethod


class UserRepository(ABC):

    @abstractmethod
    def save(self, user):
        pass


class InMemoryUserRepository(UserRepository):

    def __init__(self):
        self.users = []

    def save(self, user):
        self.users.append(user)
        print(f"User {user.username} saved in memory.")


class SQLUserRepository(UserRepository):

    def save(self, user):
        print(f"Saving user {user.username} to SQL database...")


class MongoUserRepository(UserRepository):

    def save(self, user):
        print(f"Saving user {user.username} to MongoDB...")
