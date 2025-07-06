# ---------------------------------------------------
# Project: Day 3 - Escape_Alcatraz_Game
# Course: 100 Days of Python (Udemy)
# Author: Angel Santiago
# Date: 2 MAR 2025
# Objective: 
# - Practice working with if/elif/else statements.
# - Handle user input with input() function.
# - Use nested conditionals (if statements inside if statements).
# - Combine logic with string comparisons.
# - Build a simple text-based game using what we’ve learned so far.
# ---------------------------------------------------

## How to Run
```bash
python escape_alcatraz_game.py

print(r'''
      ================================
         ALCATRAZ  /__\            ||     ||<(.)>||<(.)>||     || 
       ____________|  |            ||    _||     ||     ||_    || 
       |_|_|_|_|_|_|  |            ||   (__D     ||     C__)   || 
       |_|_|_|_|_|_|__|            ||   (__D     ||     C__)   ||
      A@\|_|_|_|_|_|/@@Aa          ||   (__D     ||     C__)   ||
   aaA@@@@@@@@@@@@@@@@@@@aaaA      ||   (__D     ||     C__)   ||
  A@@@@@@@@@@@DWB@@@@@@@@@@@@A     ||     ||     ||     ||  dwb||
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  ================================
''')

print("Welcome to ALCATRAZ Escape Realm.")
print("Your mission is to escape ALCATRAZ.")
choice1 = input('You\'re see the morning guard walking by, what do you do? Type "talk" or "hit"\n'). lower()

if choice1 == "talk":
    choice2 = input('He said he\'ll do anything for you if you give him 500 pesos. '
          'Type "accept" to give the money or "reject" to deny offer\n').lower()
    if choice2 == "accept":
        choice3 = input('After the guard receives the pesos, you are taken to the kitchen and '
                        'hidden on a garbage container. You are transported on a dump truck and listen'
                        '\nto some people saying "we will now inspect the contents of our boxes". You have '
                        'three choices: "wait calmly", "violently attack", or "play dead". Which decision '
                        'are you making? \n').lower()
        if choice3 == "wait calmly":
            print("The guards inspected the boxes and found you in it. They decide to throw you in the water"
                  "where you where fiercely eaten by sharks.")
        elif choice3 == "violently attack":
            print("You conducted successful martial arts combat where you managed to defeat the garbage men and "
                  "take control of the vehicle. YOU MANAGED TO ESCAPE ALCATRAZ!")
        elif choice3 == "play dead":
            print("When the men inspected the box and saw you playing dead they actually thought you were dead."
                  "\nThey preferred to keep you in the box but then the dump truck dumped all garbage into "
                  "a garbage treatment system were you are shredded to bits.")
        else:
            print("You did not make any choice at all. The men got scared of you when inspected the box and you were "
                  "technically able to escape and swim your way back!")
    else:
        print("The guard proceeded to not feed you for 30 days. You unfortunately died of hunger, sorrow, "
              "and loneliness")
else:
    print("He tied you up, threw you in the window and you disappeared into eternity!")
