"""
🏦 Loan Approval System - Santiago Bank

📌 Description:
This program simulates a **loan approval system** where multiple applicants can request loans.
The system tracks all applications and determines the **highest loan request**.
Once all applications are collected, the program announces the **applicant with the highest loan request**.

🎯 Learning Objectives:
1️⃣ **Dictionaries** - Store applicant names as keys and loan amounts as values.
2️⃣ **Loops (`while` and `for`)** - Continuously collect loan requests and iterate through applicants.
3️⃣ **User Input Handling** - Convert string inputs into integers and validate user responses.
4️⃣ **Conditional Logic (`if-else`)** - Compare values to determine the highest loan request.
5️⃣ **Functions** - Encapsulate logic for finding the highest loan amount.

✅ Features:
- Allows multiple users to **apply for loans**.
- Keeps loan amounts **private** by clearing the screen between inputs.
- **Finds and announces the highest loan request** at the end.
"""

loan_requests = {}

new_loan = True

def find_highest_loan(loan_request_dictionary):
    highest_loan_username = ""  
    highest_loan_request_final = 0 

    for applicant in loan_request_dictionary:
        user_loan_amount = loan_request_dictionary[applicant]

 
        if user_loan_amount > highest_loan_request_final:
            highest_loan_request_final = user_loan_amount
            highest_loan_username = applicant  

    print(f"Loan Approved: {highest_loan_username} with a request of ${highest_loan_request_final}!")

while new_loan:
    name = input("Enter your full name: \n")
    loan_amount = int(input("Enter the loan amount requested: \n$"))

    loan_requests[name] = loan_amount  

    additional_applicant = input("Is there another applicant? Type 'yes' or 'no': \n").lower()

    if additional_applicant == "no":
        new_loan = False 
        find_highest_loan(loan_requests)
    else:
        print("\n" * 100) 
