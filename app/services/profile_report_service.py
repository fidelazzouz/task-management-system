class ProfileReportGenerator:

    def generate_profile_report(self, user):
        if user is None:
            raise ValueError("User cannot be None")

        report = (
            "User Profile Report\n"
            "-------------------\n"
            f"Username: {user.username}\n"
            f"Email: {user.email}\n"
            f"Projects: {len(user.projects)}"
        )

        return report
