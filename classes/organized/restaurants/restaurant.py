class Restaurant:
    """Represent a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize a restaurant's name and their cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """Describe the type of restaurant"""
        print(f"The name of the restauarant is {self.restaurant_name}")
        print(f"\tWe offer a {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Open the restaurant"""
        print(f"{self.restaurant_name} is opened")