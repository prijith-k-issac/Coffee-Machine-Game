
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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


def resource_validator(user_chosen):
    water_required = MENU[user_chosen]["ingredients"]["water"]
    milk_required = MENU[user_chosen]["ingredients"]["milk"]
    coffee_required = MENU[user_chosen]["ingredients"]["coffee"]
    if resources["water"] >= water_required and resources["milk"] >= milk_required and \
            resources["coffee"] >= coffee_required:
        return True
    else:
        global shortage
        if resources["water"] < water_required:
            shortage = "water"
        elif resources["milk"] < milk_required:
            shortage = "milk"
        else:
            shortage = "coffee"

        return False




def coin_counter(user_chosen):
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    coins = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if coins >= MENU[user_chosen]["cost"]:
        global money
        money += MENU[user_chosen]["cost"]
        balance = round((coins - MENU[user_chosen]["cost"]), 2)
        print(f"Here is ${balance} in change")
        print(f"Here is your {user_chosen} ☕.Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded")


def resource_reducer(user_chosen):
    resources["water"] = resources["water"] - MENU[user_chosen]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[user_chosen]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[user_chosen]["ingredients"]["coffee"]


def report_generator():
    print(f'water: {resources["water"]}')
    print(f'milk: {resources["milk"]}')
    print(f'coffee: {resources["coffee"]}')
    print(f'money: {money}')

money = 0
shortage = ""
is_continue = True

while is_continue:
    user_input = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        value = resource_validator(user_input)
        if value:
            coin_counter(user_input)
            resource_reducer(user_input)
        else:
            print(f"  Sorry there is not enough {shortage}")
    elif user_input == 'report':
        report_generator()
    elif user_input == 'off':
        is_continue = False






