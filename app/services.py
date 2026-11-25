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


class RegistrationService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def register(self, user):
        self.repository.save(user)


class NotificationService:

    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.email}...")


class ProfileReportGenerator:

    def generate_profile_report(self, user):
        print(f"Generating profile report for {user.username}...")


class DeliveryCalculator:

    def calculate(self, delivery):
        return delivery.calculate()


class NormalDelivery:

    def calculate(self):
        return 10


class ExpressDelivery:

    def calculate(self):
        return 20


class SameDayDelivery:

    def calculate(self):
        return 30
