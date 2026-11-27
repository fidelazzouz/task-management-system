import logging

logger = logging.getLogger(__name__)


class RegistrationService:

    def __init__(self, repository):
        if repository is None:
            raise ValueError("Repository cannot be None")

        self.repository = repository

    def register(self, user):
        if user is None:
            raise ValueError("User cannot be None")

        self.repository.save(user)
        logger.info("User registered successfully: %s", user.username)
