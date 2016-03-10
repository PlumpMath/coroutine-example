from time import sleep

class Food:
    def __init__(self):
        """Every item takes 1 second to prepare."""
        sleep(1)
        
    def __str__(self):
        """Return the food's name."""
        return self.__class__.__name__


class Soup(Food): pass
class Steak(Food): pass
class IceCream(Food): pass
