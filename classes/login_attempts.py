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
        self.login_attempt = 0

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
        """Greet users witht their username"""
        print(f"Welcome back {self.username}\n")
    
    def read_login_attempts(self):
        """Display number of time user have tried to login."""
        print(f"You've logged in {self.login_attempt} times")

    def increment_loging_attempts(self):
        """Increase logging attempt by one"""
        self.login_attempt += 1
    
    def reset_login_attempts(self):
        """Reset log in attempt to zero"""
        self.login_attempt = 0

user_1 = Users("olamide", "adu", "xrand", "xrand@gmail.com", "kattegård alle", "denmark")
print(user_1.describe_user())

user_1.increment_loging_attempts()
user_1.increment_loging_attempts()
user_1.increment_loging_attempts()

user_1.read_login_attempts()

user_1.reset_login_attempts()
user_1.read_login_attempts()