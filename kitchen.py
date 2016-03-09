from utils import coroutine
from food import Soup, Steak, IceCream


cookbook = {
    "soup": Soup,
    "steak": Steak,
    "ice cream": IceCream,
}


@coroutine
def good_kitchen():
    """Take requests from the restaurant and cook the right food."""
    # Wait for the first request.
    request = yield

    while True:
        # Find the recipe and make the food.
        FoodItem = cookbook[request]
        # Send the food up to the restaurant and get the next request.
        request = yield FoodItem()
