# Import the random function
import random

# Ask for the user's name
user_name = input("Hello, what's your name?\n")

# Establish a list for the greeting and weather and a value for the temperature

greetings = ["Good morning, ", "Rise and shine ", "Time to get ready for the \
day "]

weather = ["sunny", "partly cloudy", "rainy", "windy", "foggy", "icy"]

temperature = 0

# Establish a list for the days of the week and for alternative activities

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
        "Saturday"]

lazy_day = ["read", "meditate", "go for a bike ride", "binge your favorite \
show"]

# Create a greeting that generates a randomly chosen salutation and a random
# weather condition


weather_condition = random.choice(weather)
if weather_condition == "sunny":
    temperature = 84
elif weather_condition == "partly cloudy" or weather_condition == "windy":
    temperature = 65
elif weather_condition == "rainy" or weather_condition == "foggy":
    temperature = 51
else:
    temperature = 34

for day in days:
    print(random.choice(greetings) + user_name + "!")
    print(f"Today is {day}, and it is {weather_condition} with a high of \
{temperature} degrees F.")
    if day == "Sunday":
        fun = random.choice(lazy_day)
        print(f"Enjoy your {day} and {fun}!")
        decision = input("Are you ready for the next day? Y or N\n").lower()
        if decision == "n":
            break
    elif day == "Saturday":
        print("Drink some water, grab your cleats and go play soccer!")
        decision = input("Are you ready for the next day? Y or N\n").lower()
        if decision == "n":
            break
    else:
        time = int(input("What time is it? Please submit the time without a \
colon (:) (e.g. 615)\n"))
        timeframe = input("Is it AM or PM?\n").lower()
        if timeframe == "pm":
            time = time + 1200
#       Help decide which route to take.
        print("Let's see if you should take the freeway or surface streets to \
work!")
        if (time > 730 and time < 830) or (time > 1430 and time < 1830):
            if timeframe == "pm":
                time = time - 1200
            print(f"Since it's {time}, you should probably take surface \
streets.")
        else:
            if timeframe == "pm":
                time = time - 1200
            print(f"Since it's {time}, you can probably take the freeway \
without too much traffic.")
        coffee = input("Did you make coffee this morning? Y / N \n").lower()
        if coffee == "n":
            if time < 700:
                wait_time = 700 - 40 - time
                print(f"Hi Top opens in {wait_time} minutes, so you can get \
coffee then.")
            elif (time >= 900 and time < 1400) and (day == "Tuesday" or
                                                    day == "Thursday"):
                print("Hi Top is open, so you can pick up coffee on your \
prep.")
            else:
                print("Just grab coffee at school.")
        else:
            print("Nicely done!")
        decision = input("Are you ready for the next day? Y or N\n").lower()
        if decision == "n":
            break
