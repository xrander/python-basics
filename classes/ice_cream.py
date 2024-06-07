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

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant specific to ice cream stands"""
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """Initialize attribute of the parent restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavor(self):
        """Display the flavors available"""
        print("The flavors available are: ")
        for flavor in self.flavors:
            print(f"\t- {flavor.title()}")

my_icecream = IceCreamStand("The point")
my_icecream.flavors = ["vanilla", "mango", "strawberry", "raspberry"]

my_icecream.describe_restaurant()
my_icecream.display_flavor()