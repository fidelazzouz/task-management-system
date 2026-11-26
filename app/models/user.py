class User:

    def __init__(self, username, email):

        if not username.strip():
            raise ValueError("Username cannot be empty")

        if not email.strip():
            raise ValueError("Email cannot be empty")

        self.username = username
        self.email = email
        self.projects = []

    def update_email(self, new_email):

        if not new_email.strip():
            raise ValueError("Email cannot be empty")

        self.email = new_email

    def add_project(self, project):
        self.projects.append(project)
