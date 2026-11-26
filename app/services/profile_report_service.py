class ProfileReportGenerator:

    def generate_profile_report(self, user):

        print("User Profile Report")
        print("-------------------")
        print("Username:", user.username)
        print("Email:", user.email)
        print("Projects:", len(user.projects))
