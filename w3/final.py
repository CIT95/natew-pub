print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
# My code

direction = input("As you travel down your path, you come to a crossroads and \
must choose a direction.\nDo you head left or right? LEFT or RIGHT ")

if direction.lower() == "left":
    crossing = input(f"You head to the {direction.lower()} and meet a woman \
who tells you there is an old home just beyond the river up ahead. She \
says she has heard travelers talk of a hidden treasure there. You thank \
her and continue to the river.\nDo you swim across or wait for the \
ferryman? SWIM or WAIT ")
    if crossing.lower() == "wait":
        door = input("You survey the treacherous waters and decide to wait.\n\
When the ferry finally arrives, the ferryman tells you a story of the \
house you are searching for. He says that three brothers of family Monty \
once lived there and all agreed to hide their family's treasure. To \
protect their treasure they created a final test for those that found the \
house. In the house existed a hall with three doors. Behind two of the \
doors lie terrible deaths for those who entered, but one door held the family\
's fortune. When you ask which door of the Monty Hall held the treasure, \
the ferryman says he doesn't know. He only says that the only clue that \
was ever found was the riddle: 'If gold is what you seek, stray from fire \
and fear the ice.'\nYou thank the ferryman and make your way to the house. \
You come to the house and find the hall. Before you are three doors: one \
yellow, one red, and one blue. Which do you choose?\n YELLOW RED or BLUE ")
        if door.lower() == "yellow":
            print("Congratulations brave explorer! You have bested the Monty \
Hall and have found the treasure! You win!")
        elif door.lower() == "red":
            print("You failed to heed the warning of the riddle! The flames \
of the eternal inferno behind the fiery red door consume you!\nGAME OVER")
        elif door.lower() == "blue":
            print("You failed to heed the warning of the riddle! The yeti \
of the frozen mountains has waited for its feast for far too long! \
You are eaten.\nGAME OVER")
        else:
            print("GAME OVER")
    else:
        print("You foolishly attempt to swim across the treacherous waters \
and are quickly overwhelmed by the raging rapids. You struggle to keep your \
head above water but eventually drown.\nGAME OVER")
else:
    print("You wander aimlessly and find yourself in the dreaded haunted \
forest. After days of madly trying to find your way out, you succumb to the \
terrors of the forest.\nGAME OVER")
