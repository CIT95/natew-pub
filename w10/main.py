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

# My code
money = ""


def resource_check(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = 0
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = round(((quarters * .25) + (dimes * .10) + (nickels * .05) +
                   (pennies * .01)), 2)
    return total


def transaction(coins_inserted, drink_cost):
    if coins_inserted > drink_cost:
        change_given = round((coins_inserted - drink_cost), 2)
        print(f"Here is ${change_given: .2f} in change.")
        money = 0
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_drink(drink_selection, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_selection}. Enjoy!")


def run_report():
    print("The machine currently has:")
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${money: .2f}")


coffee_machine_on = True

while coffee_machine_on:
    drink_order = input("What would you like? (espresso/latte/cappuccino):\
").lower
    if drink_order = "off":
        coffee_machine_on = False
        print("Machine powering down.")
    elif drink_order == "report":
        run_report()
    else:
        drink = MENU[drink_order]
        drink_cost = drink["cost"]
        print(f"That'll be ${drink_cost: .2f}")
        if resource_check(drink["ingredients"]):
            collected_payment = process_coins()
            if transaction(collected_payment, drink["cost"]):
                make_drink(drink_order, drink["ingredients"])
