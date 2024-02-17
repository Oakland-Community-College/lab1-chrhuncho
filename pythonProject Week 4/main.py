import math
import random
#Print welcome message for Table Top Game
print("Hello, welcome to Table Top Role Playing")
print("This is based off Fallout:New Vegas")
#User enters character name here
def get_name():
    input('Hello, please enter character name.\n')
get_name()
def sum_of_four_six_sided_dice_with_lowest_dropped():
    number = random.randint(1,10)
    if number == 1:
        print("You have chosen strength!")
    elif number == 2:
        print("You have chosen dexterity!")
    elif number == 3:
        print("You have chosen constitution!")
    elif number == 4:
        print("You have chosen intelligence!")
    elif number == 5:
        print("You have chosen wisdom!")
    elif number == 6:
        print("You have chosen perception!")
    elif number == 7:
        print("You have chosen agility!")
    elif number == 8:
        print("You have chosen endurance!")
    elif number == 9:
        print("You have chosen luck!")
    else:
        print("You have chosen charisma")
sum_of_four_six_sided_dice_with_lowest_dropped()
print("Ok, now time to roll a dice to add more attributes")
dice_roll= int(input("Dice Roll(Number will be amount of times you roll the dice): "))
dice_roll= random.randint(1,10)
if dice_roll == 1:
    print("You have added +5 strength")
elif dice_roll == 2:
    print("You have added +5 perception")
elif dice_roll == 3:
    print("You have added +5 luck")
elif dice_roll == 4:
    print("You have added +10 intelligence")
elif dice_roll == 5:
    print("You have added +7 agility")
elif dice_roll == 6:
    print("You have added +3 endurance")
elif dice_roll == 7:
    print("You have added +4 charisma")
elif dice_roll == 8:
    print("You have added +9 wisdom")
elif dice_roll == 9:
    print("You have added +2 constitution")
else:
    print("You have added +5 dexterity")

