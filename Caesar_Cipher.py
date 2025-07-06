"""
Caesar Cipher - Learning Objectives

1. String Manipulation:
   - Iterate over strings, preserve non-alphabetical characters.
   - Use list indexing and modular arithmetic for letter shifts.

2. Functions & Parameters:
   - Write a reusable caesar() function with encode/decode modes.
   - Adjust shift logic with conditional statements.

3. Loops & User Input:
   - Use a while loop for repeated encryption/decryption.
   - Prompt users for action until they decide to quit.

4. Basic Encryption Concepts:
   - Understand a simple substitution cipher (Caesar).
   - Practice encoding/decoding by shifting letters in the alphabet.
"""


from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter

        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to do again. Otherwise, type 'no'. \n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")
