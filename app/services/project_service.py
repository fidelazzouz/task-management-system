class ProjectService:

    def __init__(self):
        self.projects = []

    def create_project(self, project):
        self.projects.append(project)

    def add_task_to_project(self, project, task):
        project.add_task(task)

    def delete_project(self, project):
        if project in self.projects:
            self.projects.remove(project)

    def get_all_projects(self):
        return self.projects
