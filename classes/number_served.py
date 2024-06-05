class Restaurant:
    """Represent a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize a restaurant's name and their cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"The name of the restauarant is {self.restaurant_name}")
        print(f"\tWe offer a {self.cuisine_type} cuisine")
    
    def open_restaurant(self):
        """Open the restaurant"""
        print(f"{self.restaurant_name} is opened")

    def read_number_served(self):
        """Read the number of customers served."""
        if self.number_served < 1:
            print(f"The number of customers served is {self.number_served}")
        else:
            print(f"The number of customers served are {self.number_served}")
    
    def set_number_served(self, customers):
        """Set the number of customers served"""
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print(f"The numbers served cannot be less than the customers.")

    def incremnet_number_served(self, new_customers):
        """Add increment customers."""
        self.number_served += new_customers
    
my_restaurant = Restaurant("mcDonalds", "fast food")
print(my_restaurant.describe_restaurant())

my_restaurant.read_number_served()
my_restaurant.number_served = 10
my_restaurant.read_number_served()

my_restaurant.set_number_served(15)
my_restaurant.read_number_served()

my_restaurant.incremnet_number_served(40)
my_restaurant.read_number_served()