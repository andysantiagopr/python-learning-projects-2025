# Learning Objectives:
# - Use lists to store and manage dynamic data.
# - Implement loops to automate repetitive actions (rolling dice).
# - Utilize functions for modular programming and reusability.
# - Modify list elements conditionally (changing 6 to 1 if total exceeds 12).
# - Use while loops to handle continuous user input and game progression.
# - Apply conditional statements to enforce game rules and determine win/loss conditions.

import random

print("Welcome to Santiago's Dice Challenge! Roll your chances until 12!")

player_rolls = []
dice_faces = [1, 2, 3, 4, 5, 6]

def roll_dice():
    return random.choice(dice_faces)

for _ in range(3):
    player_rolls.append(roll_dice())

print(f"Player, your dice rolls are {player_rolls} with a total of {sum(player_rolls)} \n")

def evaluate_game():
    global player_rolls
    total_points = sum(player_rolls)

    while total_points > 12 and 6 in player_rolls:
        player_rolls[player_rolls.index(6)] = 1
        total_points = sum(player_rolls)

    if total_points > 12:
        print("You lose. Game over")
        return False

    return True

continue_rolling = True

while continue_rolling:
    roll_again = input("Would you like to roll the dice again? Type 'y' for yes and 'n' for no: \n")

    if roll_again == 'n':
        continue_rolling = False
        print(f"Your final hand: {player_rolls}, Final score: {sum(player_rolls)}! Thanks for playing! 🎲")

    else:
        player_rolls.append(roll_dice())
        print(f"Player, your dice rolls are {player_rolls} with a total score of {sum(player_rolls)}")

        continue_rolling = evaluate_game()
