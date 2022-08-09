logo = """
    __  ___  _____ _____  ___   ___      ___ ___  ____    __ __ __ ____ ____    ___ 
   /  ]/   \|     |     |/  _] /  _]    |   |   |/    |  /  ]  |  |    |    \  /  _]
  /  /|     |   __|   __/  [_ /  [_     | _   _ |  o  | /  /|  |  ||  ||  _  |/  [_ 
 /  / |  O  |  |_ |  |_|    _]    _]    |  \_/  |     |/  / |  _  ||  ||  |  |    _]
/   \_|     |   _]|   _]   [_|   [_     |   |   |  _  /   \_|  |  ||  ||  |  |   [_ 
\     |     |  |  |  | |     |     |    |   |   |  |  \     |  |  ||  ||  |  |     |
 \____|\___/|__|  |__| |_____|_____|    |___|___|__|__|\____|__|__|____|__|__|_____|
                                                                                    
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,}

def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough {}.".format(item))
            is_enough = False
    return is_enough

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    is_succesful = True
    if drink_cost >= money_received:
        print("Sorry that's not enough money.")
        is_succesful= False
    else:
        change = round(money_received - drink_cost, 2)
        print("Here is {} in change.".format(change))
        global profit
        profit += drink_cost
        is_succesful = True
    return is_succesful

def make_coffee(drink_name, order_ingredients):
    for item in  order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Here is your {}. Enjoy!".format(drink_name))

is_on = True

while is_on:
    print(logo)
    choice = input("What would you like?(espresso/latte/cappucino): ")

    if choice == "off":
        is_on =  False
    elif choice == "report":

        print("Water: {}\nMilk: {}\nCoffee: {}\nMoney: {}".format(resources['water'], resources['milk'], resources['coffee'], profit))
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                
