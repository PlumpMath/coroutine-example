from kitchen import good_kitchen as kitchen


def run_restaurant(kitchen=None, serve=None):
    """Send requests for food to the kitchen, and serve them when they appear."""
    for order in get_orders():
        food = kitchen.send(order)
        serve(food)


def get_orders():
    """Continuously get food orders from the diners."""
    while True:
        yield input()


def fancy_serve(food):
    """Serve an item of food to an esteemed customer."""
    print("Here's your {}, sir/madam.".format(food))


if __name__ == "__main__":
    k = kitchen()
    run_restaurant(kitchen=k, serve=fancy_serve)
