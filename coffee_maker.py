class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }
        self.is_on = True

    def report(self):
        """Prints a report of all resources."""
        print("Water: {}ml".format(self.resources['water']))
        print("Milk: {}ml".format(self.resources['milk']))
        print("Coffee: {}g".format(self.resources['coffee']))

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print("Sorry there is not enough {}.".format(item))
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print("Here is your {} ☕️. Enjoy!".format(order.name))
