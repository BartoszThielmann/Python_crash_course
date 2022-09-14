"""A set of classes representing a restaurant"""

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
