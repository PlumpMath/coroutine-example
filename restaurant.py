from kitchen import good_kitchen as kitchen


def run_restaurant(kitchen=None, serve=None):
    """Prepare and serve each order as it comes."""
    for order in get_orders():
        food = kitchen.send(order)
        serve(food)


def get_orders():
    """Continuously get food orders from the diners."""
    while True:
        yield input()


def fancy_serve(food):
    """Serve an item of food."""
    print("Here's your {}, sir/madam.".format(food))


if __name__ == "__main__":
    k = kitchen()
    run_restaurant(kitchen=k, serve=fancy_serve)
