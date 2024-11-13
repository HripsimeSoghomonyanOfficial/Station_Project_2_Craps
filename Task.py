import random

def roll_dice():
    try:
        return random.randint(1, 6), random.randint(1, 6)
    except Exception as e:
        print(f"An error occurred while rolling the dice: {e}")

def play_craps():
    try:
        dice1, dice2 = roll_dice()
        initial_sum = dice1 + dice2
        print(f"The sum of dice is {dice1} + {dice2} = {initial_sum}")

        if initial_sum in [7, 11]:
            print("You won")
            return
        elif initial_sum in [2, 3, 12]:
            print("You lose")
            return
        else:
            goal = initial_sum
            print(f"Now your goal number is {goal}")
            
            while True:
                dice1, dice2 = roll_dice()
                roll_sum = dice1 + dice2
                print(f"The sum of dice is {dice1} + {dice2} = {roll_sum}")
                
                if roll_sum == goal:
                    print("You won")
                    return
                elif roll_sum == 7:
                    print("You lose")
                    return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

play_craps()
