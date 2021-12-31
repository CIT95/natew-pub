print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
per_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

per_person = float(total) * (1 + (int(per_tip) / 100)) \
    / int(people)

dollar_per = round(per_person, 2)
# New code after commit starts here to address error
dollar_per = "{:.2f}".format(per_person)
# New code after commit ends here

print(f"Each person should pay: ${dollar_per}")