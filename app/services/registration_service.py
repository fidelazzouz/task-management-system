class RegistrationService:

    def __init__(self, repository):
        self.repository = repository

    def register(self, user):
        self.repository.save(user)
