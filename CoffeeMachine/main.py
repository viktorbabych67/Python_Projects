MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"])
#
#
# def coins_insertion(user_input):
#     quarters = float(input("How many quarters? ")) * 0.25
#     dimes = float(input("How many dimes? ")) * 0.10
#     nickels = float(input("How many nickels? ")) * 0.05
#     pennies = float(input("How many pennies? ")) * 0.01
#     total = quarters + dimes + nickels + pennies
#     coffe_cost = MENU[f"{user_input}"]["cost"]
#     result = 0
#     while total < coffe_cost:
#         result = coffe_cost - total
#         total += float(input(f"You need to add ${result} to be able to add a coffe. The price of the coffe is ${coffe_cost}, you gave {total}"))
#     if total > coffe_cost:
#         result = total - coffe_cost
#
#     print(f"Here is ${result} in change.")
#
#
# money = 0
# continue_order = True
# user_input = ""
# while continue_order:
#     no_resourses = False
#     while no_resourses != True:
#         user_input = input("What would you like? (espresso/latte/cappuccino): ")
#         no_resourses = True
#         if user_input != "report":
#             if MENU[user_input]["ingredients"]["water"] > resources["water"]:
#                 print("Sorry. There is not enough water.")
#                 no_resourses = False
#             if user_input != "espresso":
#                 if resources["milk"] < MENU[user_input]["ingredients"]["milk"]:
#                     print("Sorry. There is not enough milk.")
#                     no_resourses = False
#             if resources["coffee"] < MENU[user_input]["ingredients"]["coffee"]:
#                 print("Sorry. There is not enough coffee.")
#                 no_resourses = False
#
#         if user_input == "report":
#             no_resourses = False
#             print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}\nCoffee: {resources["coffee"]}\nMoney: {money}")
#
#     print("Please insert coins.")
#     coins_insertion(user_input)
#     resources["water"] -= MENU[user_input]["ingredients"]["water"]
#     if user_input != "espresso":
#         resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
#
#     resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
#     money += MENU[f"{user_input}"]["cost"]
#
#     print(f"Here is you {user_input}. Enjoy!")


###################### Other Solution ##############################

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

