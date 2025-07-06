"""
Rock, Paper, Scissors Game - Learning Objectives

This beginner project helps to practice and demonstrate the following skills:

Understanding Python Data Structures:
    - Used lists to store ASCII art representations of the game options (rock, paper, scissors).

Conditional Logic:
    - Implemented if/elif/else statements to handle game rules and determine the winner.

Handling User Input:
    - Used input() to gather player choice and convert it to an integer for processing.

Random Module:
    - Applied random.randint() to generate the computer’s selection.

String Manipulation and Output Formatting:
    - Printed multi-line ASCII images to make the game visually appealing.

Error Handling for Invalid Inputs:
    - Checked for valid user responses and handled invalid inputs with a friendly error message.

Additional Takeaways:
- Practiced importing modules (random).
- Improved comfort with basic program flow (input → processing → output).
- Reinforced comparison operators (>, <, ==) to control game logic.
- Enhanced beginner-level understanding of list indexing.
"""


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [" ", rock, paper, scissors]

import random

print("Welcome to my rock, paper and scissors game!")

user_selection = int(input("Type 1 for rock, 2 for paper, and 3 for scissors\n"))
if user_selection >=1 and user_selection <=3:
    print(images[user_selection])

computer_selection = random.randint(1,3)
print("Computer chose:")
print(images[computer_selection])

if user_selection >= 4 or user_selection <1:
    print("You typed an invalid response. You lose!")
elif user_selection == 1 and computer_selection == 3:
    print("You win!")
elif computer_selection == 1 and user_selection == 3:
    print("You lose!")
elif user_selection > computer_selection:
    print("You win!")
elif computer_selection > user_selection:
    print("You lose!")
elif user_selection == computer_selection:
    print("It's a tie!")
