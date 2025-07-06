"""
Learning Objectives for This Project:
- Understand and apply functions for modular code
- Use dictionaries to map operations to functions
- Implement a loop for continuous calculations
- Handle user input and ensure smooth user interaction
- Practice clean and readable coding practices
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

continue_calculating = True
first_number = float(input("Enter the first number: \n"))

while continue_calculating:
    for operator in operations:
        print(operator)

    chosen_operator = input("Choose an operation from the above: \n")
    second_number = float(input("Enter the next number: \n"))

    result = operations[chosen_operator](first_number, second_number)
    print(f"{first_number} {chosen_operator} {second_number} = {result}")

    continue_with_result = input(f"Would you like to continue using {result}? (y/n): \n").lower()

    if continue_with_result == 'n':
        new_calculation = input("Would you like to start a new calculation? (y/n): \n").lower()
        if new_calculation == 'n':
            continue_calculating = False
            print("Thank you and Goodbye!")
        else:
            print("\n" * 100)
            first_number = float(input("Enter the first number: \n"))
    else:
        first_number = result
        print("\n" * 100)
