from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
resources = coffee_maker.resources
menu_item = Menu()
money = MoneyMachine()

flag = True
while flag:
    order = input("What would you like?\n1. Latte\n2. Espresso\n3. Cappuccino\nPlease type report to check "
                  "ingredients : ").lower()

    if order != "report" and order != 'stop':
        coffee = menu_item.find_drink(order)
        if coffee is None:
            order = input("Please select from the below\n1. Latte\n2. Espresso\n3. Cappuccino\nPlease type report to "
                          "check ingredients : ").lower()
        else:
            if coffee_maker.is_resource_sufficient(coffee):
                coffee_price = coffee.cost
                if money.make_payment(coffee_price):
                    coffee_maker.make_coffee(coffee)
    elif order == "report":
        coffee_maker.report()