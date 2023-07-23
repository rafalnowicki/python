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

checkout = {
    "quarter": 0,
    "dime": 0,
    "nickel": 0,
    "penny": 0,
}


# TODO: Make a Coffee Machine program

def report():
    """Prints all recourses"""
    for key, value in resources.items():
        print(f"{key}: {value}")
    for key, value in checkout.items():
        sum = 0
        sum += value
    print(f"Money: {sum}")


def check(coffee_type):
    water = (MENU[coffee_type]["ingredients"]["water"])
    milk = (MENU[coffee_type]["ingredients"]["milk"])
    coffee = (MENU[coffee_type]["ingredients"]["coffee"])
    if water > resources["water"]:
        print(f"Sorry there is not enough water.")
        return False
    if milk > resources["milk"]:
        print(f"Sorry there is not enough milk.")
        return False
    if coffee > resources['coffee']:
        print(f"Sorry there is not enough coffee.")
        return False


def payment(coffee_type):
    cost = MENU[coffee_type]["cost"]
    print(f"The {coffee_type} costs {cost}$")
    print("Please insert coins.")
    quarters = float(input("How many quarters 0.25$? "))
    dimes = float(input("How many dimes 0.10$? "))
    nickles = float(input("How many nickles 0.05$? "))
    pennies = float(input("How many pennies 0.01$? "))
    checkout["quarter"] += quarters
    checkout["dime"] += dimes
    checkout["nickel"] += nickles
    checkout["penny"] += pennies
    cash_in = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    cash_in = round(cash_in, 2)
    if cash_in > cost:
        change = cash_in - cost
        change = round(change, 2)
        print(f"Here is {change} in change.")

    if cash_in >= cost:
        print(f"Here is your {order} ☕️. Enjoy!")

    if cash_in < cost:
        print("Sorry that's not enough money. Money refunded.")


def resources_used(coffee_type):
    """Reduces recourses with coffee made"""
    water = (MENU[coffee_type]["ingredients"]["water"])
    milk = (MENU[coffee_type]["ingredients"]["milk"])
    coffee = (MENU[coffee_type]["ingredients"]["coffee"])
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


order = ""
while order != "off":
    order = input("    What would you like? espresso/latte/cappuccino: ")
    if order == "report" or order == "r":
        if order == "r":
            order = "report"
        report()
    elif order == "espresso" or order == "e":
        if order == "e":
            order = "espresso"
        if check(order) != False:
            payment(order)
            resources_used(order)
    elif order == "latte" or order == "l":
        if order == "l":
            order = "latte"
        if check(order) != False:
            payment(order)
            resources_used(order)
    elif order == "cappuccino" or order == "c":
        if order == "c":
            order = "cappuccino"
        if check(order) != False:
            payment(order)
            resources_used(order)
    elif order == "off" or order == "o":
        if order == "o":
            order = "off"
        print("Good bye!")
    else:
        print("Provide a command, please.")
        print("Available commands: \n report\n espresso\n latte\n cappuccino\n off")
