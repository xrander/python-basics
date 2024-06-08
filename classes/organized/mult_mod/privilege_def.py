class Privileges:
    """Model privileges"""
    def __init__(self, privileges=["can delete post", "can add post", "can ban user"]):
        """Initialize a list of privileges limited to administrators"""
        self.privileges = privileges

    def show_privileges(self):
        """Display privileges limited to an admin"""
        for privilege in self.privileges:
            print(f"\t - {privilege}")