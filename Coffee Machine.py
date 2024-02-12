
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}")

def check_resource(coffee_type):

    if MENU[coffee_type]["ingredients"]["water"] <= resources["water"]:
         flag_water = True
    else:
        print(f"Water is not sufficient to make {coffee_type}")
        flag_water = False

    if  coffee_type != "espresso" and  MENU[coffee_type]["ingredients"]["milk"] <= resources["milk"]:
         flag_milk = True
    elif coffee_type != "espresso":
        print(f"Milk is not sufficient to make {coffee_type}")
        flag_milk = False
    else:
        flag_milk = True

    if MENU[coffee_type]["ingredients"]["coffee"] <= resources["coffee"]:
         flag_coffee =  True
    else:
        print(f"Coffee is not sufficient to make {coffee_type}")
        flag_coffee = False

    return  (flag_coffee and flag_milk and flag_water)



def addition_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickels = int(input("How many nickels? : "))
    pennies = int(input("How many pennies? : "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)


def check_transaction(amount_paid, coffee_type):
    coffee_price = MENU[coffee_type]["cost"]
    if amount_paid <= coffee_price:
        print("Please pay exact or more money!\nMoney has been refunded")
        return False
    else:
        return True


def resources_update(coffee_type):
    water = resources["water"] - MENU[coffee_type]["ingredients"]["water"]
    if coffee_type != 'espresso':
        milk = resources["milk"] - MENU[coffee_type]["ingredients"]["milk"]
    coffee = resources["coffee"] - MENU[coffee_type]["ingredients"]["coffee"]
    resources["water"] = water
    if coffee_type != 'espresso':
        resources["milk"] = milk
    resources["coffee"] = coffee


flag = True
while flag:

    user_input = input("What would you like?\n1. Latte\n2. Espresso\n3. Cappuccino\nPlease type report to check ingridients : ").lower()

    if user_input != 'report' and user_input != 'stop':
        coffee_price = MENU[user_input]["cost"]
        resource_check = check_resource(user_input)
        if resource_check:
            amount_paid = addition_coins()
            if check_transaction(amount_paid, user_input):
                resources_update(user_input)
                print(f"Amount paid: {amount_paid}")
                print(f"Change : {amount_paid - coffee_price}")
                print(f"Here is your {user_input} ☕")
    elif user_input == 'stop':
        flag = False
    else:
        report()