from user_def import Users
from privilege_def import Privileges

class Admin(Users):
    """Represent a user with privileged access, specific to an administrator"""
    def __init__(self, first_name, last_name, username, email, address, country):
        """Initialize attributes of users"""
        super().__init__(first_name, last_name, username, email, address, country)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Display the extra privileges of admins"""
        print(f"The admin {self.last_name} has the following privileges: \n")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

admin_1 = Admin("olamide", "adu", "xrand", "xrand@gmail.com", "kattegård alle", "denmark")

admin_1.show_privileges()