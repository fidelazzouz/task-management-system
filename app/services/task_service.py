import logging

from app.models.task import InvalidTaskStatusError

logger = logging.getLogger(__name__)


class TaskService:

    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)
        logger.info("Task created successfully: %s", task.title)

    def update_task_status(self, task, status):
        try:
            task.update_status(status)
            logger.info("Task '%s' status updated to '%s'", task.title, status)

        except InvalidTaskStatusError:
            logger.exception("Failed to update task status")
            raise

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks
