from art import logo
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

choice = True
all_offers = {}

while choice:
    name = input("What is your name? ")
    bid = float(input("What is your bid? "))

    all_offers[name] = bid

    continuee = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if continuee == "yes":
        clear_screen()
    else:
        choice = False


higher_bid = 0
winner = ""


def find_highest_bidder(bids):
    higher_bid = 0
    winner = ""

    for person, price in bids.items():
        if price > higher_bid:
            higher_bid = price
            winner = person

    print(f"The winner is {winner} with a bid of ${higher_bid}")
find_highest_bidder(all_offers)
