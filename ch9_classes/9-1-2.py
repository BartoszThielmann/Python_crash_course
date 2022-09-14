class Restaurant:
    """Class representing a restaurant"""
    
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f'''Restaurant name is {self.restaurant_name}. The cuisine type is {self.cuisine_type}. Number served: {self.number_served}''')
    
    def open_restaurant(self):
        """Open the restaurant"""
        print(f'Restaurant {self.restaurant_name} is now open!')
    
    def set_number_served(self, number):
        self.number_served = number
        
    def increment_number_served(self, number):
        self.number_served += number

class IceCreamStand(Restaurant):
    """Represents an Ice Cream Stand"""
    
    def __init__(self, name, cuisine):
        """Initialize attributes of the parent class
        Then initialize  attributes specific to a Ice Cream Stand"""
        super().__init__(name, cuisine)
        self.flavors = ['chocolate', 'vanilla', 'strawberry']
        
    def display_icecream_flavors(self):
        print(f'The flavors in {self.restaurant_name} are:', end=' ')
        for flavor in self.flavors:
            print(flavor, end=' ')
    
# exercise 9-1         
#restaurant = Restaurant("Bartosz's Diner", 'Polish')

#print(restaurant.restaurant_name)
#print(restaurant.cuisine_type)
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

# exercise 9-2
restaurant1 = Restaurant("Bartosz's Diner", 'Polish')
restaurant2 = Restaurant("Mariczka's Diner", 'Oriental')
restaurant3 = Restaurant("Mikus' Diner", 'Mexican')

restaurant1.set_number_served(13)
restaurant1.describe_restaurant()
restaurant2.increment_number_served(3)
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


# exercise 9-6
restaurant4 = IceCreamStand("Bartosz's Ice Cream", 'Desserts')
restaurant4.describe_restaurant()
restaurant4.display_icecream_flavors()
