from random import randint

class Dice:
    """Class representing a dice"""

    def __init__(self, sides = 6):
        """Initialize number of sides"""
        self.sides = sides
        
    def roll_die(self, number = 10):
        """Roll the die and print the results"""
        self.roll_number = number
        print(f'Rolling {self.sides}-sided dice {self.roll_number} times:')
        for roll in range(1, self.roll_number):
            print(randint(1, self.sides))

sides_6 = Dice()
sides_10 = Dice(10)
sides_20 = Dice(20)

sides_6.roll_die()
sides_10.roll_die()
sides_20.roll_die()
