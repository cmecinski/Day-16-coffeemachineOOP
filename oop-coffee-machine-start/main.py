from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cash_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()


machine_on = True
while machine_on:
    options = menu.get_items()
    prompt = input(f"What would you like? {options}: ")
    if prompt == "off":
        machine_on = False
    elif prompt == "report":
        coffee_machine.report()
        cash_machine.report()
    else:
        drink = menu.find_drink(prompt)
        if coffee_machine.is_resource_sufficient(drink):
            if cash_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)