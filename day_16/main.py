from coffeemaker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine
from replit import clear

logo = """
    __  ___  _____ _____  ___   ___      ___ ___  ____    __ __ __ ____ ____    ___ 
   /  ]/   \|     |     |/  _] /  _]    |   |   |/    |  /  ]  |  |    |    \  /  _]
  /  /|     |   __|   __/  [_ /  [_     | _   _ |  o  | /  /|  |  ||  ||  _  |/  [_ 
 /  / |  O  |  |_ |  |_|    _]    _]    |  \_/  |     |/  / |  _  ||  ||  |  |    _]
/   \_|     |   _]|   _]   [_|   [_     |   |   |  _  /   \_|  |  ||  ||  |  |   [_ 
\     |     |  |  |  | |     |     |    |   |   |  |  \     |  |  ||  ||  |  |     |
 \____|\___/|__|  |__| |_____|_____|    |___|___|__|__|\____|__|__|____|__|__|_____|
                                                                                    
"""

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    print(logo)
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
                
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
  



