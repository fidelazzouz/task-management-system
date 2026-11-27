import logging

logger = logging.getLogger(__name__)


class NotificationService:

    def send_welcome_email(self, user):
        if user is None:
            raise ValueError("User cannot be None")

        logger.info("Welcome email notification prepared for: %s", user.email)
