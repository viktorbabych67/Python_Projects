from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine




menu = Menu()





is_on = True

while is_on:
    coffee = CoffeeMaker()
    order_info = {}
    money = MoneyMachine()

    choice = input(f"​What would you like? {menu.get_items()}: ").strip().lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee.report()
        money.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        order_info = menu.find_drink(choice)

        if coffee.is_resource_sufficient(order_info):
            if money.make_payment(order_info.cost):
                coffee.make_coffee(order_info)
    else:
        print("Wrong input!")



