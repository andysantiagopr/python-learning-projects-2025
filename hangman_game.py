"""
Hangman Game

Learning Objectives:
- Work with **strings, lists, loops, and conditionals** to build game logic.
- Implement **user input handling** to track guesses and prevent duplicates.
- Use **functions** to improve code structure and reusability.
- Store guessed letters efficiently using **sets**.
- Import and use the **random** module to select words.
- Enhance user experience with **ASCII art**.
- (Optional) Load words from a file to expand word choices.
"""

import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
lives = 6
placeholder = ""
word_length = len(chosen_word)
game_over = False
correct_letters = []

for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

while not game_over:

    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
            print(f"Letter {guess} has already been attempted")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that is not in the word. You lose a life!")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************! \n"
                  f"The correct word was '{chosen_word}'!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
