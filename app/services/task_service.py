import logging

from app.models.task import InvalidTaskStatusError

logger = logging.getLogger(__name__)


class TaskService:

    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        if task in self.tasks:
            logger.warning("Task already exists: %s", task.title)
            return

        self.tasks.append(task)
        logger.info("Task created successfully: %s", task.title)

    def update_task_status(self, task, status):
        if task not in self.tasks:
            raise ValueError("Task does not exist in this service")

        try:
            task.update_status(status)
            logger.info("Task '%s' status updated to '%s'", task.title, status)

        except InvalidTaskStatusError:
            logger.exception("Failed to update task status")
            raise

    def delete_task(self, task):
        if task not in self.tasks:
            logger.warning("Task not found: %s", task.title)
            return

        self.tasks.remove(task)
        logger.info("Task deleted successfully: %s", task.title)

    def get_all_tasks(self):
        return self.tasks.copy()
