from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu = Menu()
register = MoneyMachine()
print("Welcome to PyCafe!")

while maker.is_on:
    command = input("What drink would you like?: ({}) ".format(menu.get_items())).lower()
    if command == "off":
        maker.is_on = False
    elif command == "report":
        maker.report()
        register.report()
    elif menu.have_item(command):
        drink = menu.find_drink(command)
        if maker.is_resource_sufficient(drink):
            if register.make_payment(drink.cost):
                maker.make_coffee(drink)
    else:
        continue
