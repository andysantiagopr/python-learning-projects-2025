# Santiago Temperature Converter
# 
# Objectives:
# - Practice function-based programming in Python.
# - Learn to use dictionaries to map function calls dynamically.
# - Implement user input handling and error prevention.
# - Utilize loops to allow multiple conversions without restarting the script.
# - Format float numbers to two decimal places for a cleaner output.
# - Improve program clarity with well-structured questions and prompts.

print("Welcome to the Santiago Temperature Converter!")
print("Convert temperatures between Celsius, Fahrenheit, and Kelvin.")

def celsius_fahrenheit(C):
    return (C * 9 / 5) + 32

def celsius_kelvin(C):
    return C + 273.15

def fahrenheit_celsius(F):
    return (F - 32) * 5/9

def fahrenheit_kelvin(F):
    return (F - 32) * 5/9 + 273.15

def kelvin_celsius(K):
    return K - 273.15

def kelvin_fahrenheit(K):
    return (K - 273.15) * 9 / 5 + 32

def restart_question():
    additional_question = input("\nWould you like to perform another conversion? Type 'y' for Yes or 'n' to Exit: ").lower()
    if additional_question == "y":
        print("\n" * 100)  # Clears screen
        return True
    else:
        print("\nThank you for using the Santiago Temperature Converter. Goodbye!")
        return False

restart = True

conversion_dictionary = {
    "C": (celsius_fahrenheit, celsius_kelvin),
    "F": (fahrenheit_celsius, fahrenheit_kelvin),
    "K": (kelvin_celsius, kelvin_fahrenheit)
}

while restart:
    user_choice = float(input("\nEnter the temperature value you want to convert: "))

    temperature_measurements = ["(C) Celsius", "(F) Fahrenheit", "(K) Kelvin"]
    print("\nSelect the current unit of measurement:")
    for measurement in temperature_measurements:
        print(measurement)

    chosen_measurement = input("\nWhich unit is your temperature in? (C, F, or K): ").upper()

    if chosen_measurement in conversion_dictionary:
        converted_1 = conversion_dictionary[chosen_measurement][0](user_choice)
        converted_2 = conversion_dictionary[chosen_measurement][1](user_choice)

        if chosen_measurement == "C":
            print(f"\n{user_choice:.2f}°C is equal to {converted_1:.2f}°F and {converted_2:.2f}K.")
        elif chosen_measurement == "F":
            print(f"\n{user_choice:.2f}°F is equal to {converted_1:.2f}°C and {converted_2:.2f}K.")
        elif chosen_measurement == "K":
            print(f"\n{user_choice:.2f}K is equal to {converted_1:.2f}°C and {converted_2:.2f}°F.")
    else:
        print("\nInvalid input. Please enter 'C', 'F', or 'K'.")

    restart = restart_question()
