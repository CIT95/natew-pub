# A daily expense tracker

print("Welcome to the expense tracker. Let us help you stay on budget!")
budget_builder = input("First, our program uses the following budget \
categories:\nEntertainment\nFood\nTransportation\nMiscellaneous\nDo you \
want to make additions to this set? Y or N ")
budget_categories = {
    "Entertainment": [],
    "Food": [],
    "Transportation": [],
    "Miscellaneous": []
}


def total_calculate(category):
    total_category = budget_categories[chosen_category.title()]
    category_expense = 0
    for number in total_category:
        category_expense += number
    return category_expense


def summation(num1, num2):
    return num1 + num2


if budget_builder == "Y" or budget_builder == "y":
    builder = True
    while builder:   
        new_category = input("What is the name of the category you wish to \
include?\n").title()
        budget_categories[new_category] = []
        switch_builder = input("Would you like to add another category? Y or \
N ")
        if switch_builder == "N" or switch_builder == "n":
            builder = False
print("Let's start tracking!")

day_tracker = True
while day_tracker:
    expense_category = input("What category would you like to add \
to?\n").title()
    expense = float(input(f"How much did you spend on {expense_category} \
this time? $"))
    for category in budget_categories:
        if expense_category == category:
            budget_categories[category] += [expense]
    day_tracker_switch = input("Would you like to add another expense? Y \
or N ")
    if day_tracker_switch.lower() == "n":
        day_tracker = False
chosen_category = input("Which input would you like to see the total \
expenditure for? ")
category_expense = total_calculate(chosen_category)
print(f"You've spent ${category_expense} on {chosen_category.lower()} so \
far.")
total_summation_switch = input("Would you like to exit and see your total \
spending so far? Y or N ")
if total_summation_switch.lower() == "y":
    total_expense = []
    for category in budget_categories:
        total_category_expense = 0
        working_expense = 0
        total_category_expense = total_calculate(category)
        working_expense = summation(total_category_expense,
                                    working_expense)
        total_expense.append(working_expense)
    total = total_calculate(total_expense)
    print(f"You have spent ${total} so far")
else:
    day_tracker = True
