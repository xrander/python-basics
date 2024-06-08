from restaurant import Restaurant

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