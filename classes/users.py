class Users:
    """Represent a simple user profile"""

    def __init__(self, first_name, last_name, username, email, address, country):
        """Initialize the user profile"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.address = address.title()
        self.country = country.title()

    def describe_user(self):
        """Display summary information of the user"""
        print(f"\nThe user {self.username} has the following information:\n")

        # Get user full name
        full_name = f"{self.first_name} {self.last_name}"
        
        print(f"\tFull name: {full_name}")
        print(f"\tEmail: {self.email}")
        print(f"\tAddress: {self.address}")
        print(f"\tCountry: {self.country}\n")

    def greet_user(self):
        print(f"Welcome back {self.username}\n")


user_1 = Users("olamide", "adu", "xrand", "xrand@gmail.com", "kattegard alle", "Denmark")
user_2 = Users("fisola", "adesuyi", "fisola91", "fisola@gmail.com", "norrebro", "denmark")
user_3 = Users("segun", "adu", "prime", "prime@gmail.com", "ajah", "nigeria")


user_1.describe_user()
user_2.greet_user()
user_3.describe_user()