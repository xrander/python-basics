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


restaurant_1 = Restaurant("McDonalds", "fastfood")
print(f"The name of the restaurant is {restaurant_1.restaurant_name}.")
print(f"{restaurant_1.restaurant_name} is a {restaurant_1.cuisine_type} cuisine")

restaurant_1.open_restaurant()
restaurant_1.describe_restaurant()


restaurant_2 = Restaurant("Mojo", "Fast Casual")
restaurant_3 = Restaurant("Wok", "Fine Cuisine")
restaurant_4 = Restaurant("Kebab shop", "Causual dining")

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_4.describe_restaurant()