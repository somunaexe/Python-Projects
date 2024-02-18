import random

def roll_dice():
    roll = input("Roll the dice? (Yes/No): ")
    sum = 0

    while roll.lower() == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("Current count: ", dice1 + dice2)
        sum += dice1 + dice2
        print("Total count: ", sum)
        roll = input("Roll again? (Yes/No): ")
    
roll_dice()