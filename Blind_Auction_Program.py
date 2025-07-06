from art import logo
print(logo)
print("Welcome to the Santiago Blind Auction Program!")

continue_bidding = True
bidders = {}

def find_highest_bidder(bidding_dictionary):
    winning_bidder = ""
    highest_bid = 0

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winning_bidder = bidder

    print(f"The winner is {winning_bidder} with a bid of {highest_bid}.")

while continue_bidding:
    username = input("What is your name? \n")
    user_bid = int(input("How much money would you like to bid?\n $"))
    bidders[username] = user_bid
    additional_bidder = input("Type 'yes' if any other person would like to bid, otherwise type 'no': \n")
    if additional_bidder == "no":
        continue_bidding = False
        find_highest_bidder(bidders)
    else:
        print("\n" * 100)
