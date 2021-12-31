# Original project code
# print("Welcome to the tip calculator!")
# total = input("What was the total bill? $")
# per_tip = input("What percentage tip would you like to give? 10, 12, or 15?
# ")
# people = input("How many people to split the bill? ")

# per_person = float(total) * (1 + (int(per_tip) / 100)) \
#     / int(people)

# dollar_per = round(per_person, 2)
# # New code after commit starts here to address error
# dollar_per = "{:.2f}".format(per_person)
# # New code after commit ends here

# print(f"Each person should pay: ${dollar_per}")

# Modified code

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? $"))
people = int(input("How many people are splitting the bill? "))
per_tip = int(input("What percentage tip would you like to give? 10, 12, or 15\
? "))
together = input("Will you all be paying the same tip? Y / N ")

if together == "Y":
    per_person = total * (1 + per_tip / 100) / people
    dollar_per = round(per_person, 2)
    dollar_per = "{:.2f}".format(per_person)
    print(f"Each person should pay: ${dollar_per}")
elif together == "N":
    ind_tip_percent = int(input("What percentage of the tip will you be \
paying? (Enter as a whole number) "))
    ind_owe = per_tip * (ind_tip_percent / 100) + total / people
    my_cost = round(ind_owe, 2)
    my_cost = "{:.2f}".format(ind_owe)
    print(f"Since you are paying {ind_tip_percent}% of the tip, you owe \
${my_cost}.")

# I decided to modify the tip calculator to include the option of paying
# a different percentage of the tip. I know sometimes when I am out with
# friends and we split a check, if someone ordered more, it is sometimes
# easier for us to split the total evenly but one person pay more of the
# tip. However, in order to do this, I had to research conditional statements
# a bit.
