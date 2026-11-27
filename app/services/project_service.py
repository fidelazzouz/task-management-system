import logging

logger = logging.getLogger(__name__)


class ProjectService:

    def __init__(self):
        self.projects = []

    def create_project(self, project):
        if project in self.projects:
            logger.warning("Project already exists: %s", project.name)
            return

        self.projects.append(project)
        logger.info("Project created successfully: %s", project.name)

    def add_task_to_project(self, project, task):
        if project not in self.projects:
            raise ValueError("Project does not exist in this service")

        project.add_task(task)
        logger.info("Task '%s' added to project '%s'", task.title, project.name)

    def delete_project(self, project):
        if project not in self.projects:
            logger.warning("Project not found: %s", project.name)
            return

        self.projects.remove(project)
        logger.info("Project deleted successfully: %s", project.name)

    def get_all_projects(self):
        return self.projects.copy()
