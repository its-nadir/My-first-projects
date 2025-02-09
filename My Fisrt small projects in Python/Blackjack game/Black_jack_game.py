import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play=(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
def winner(players_score , computers_score):
        if players_score > 21 and computers_score > 21:
            return "draw"
        elif computers_score > 21:
            return "player"
        elif players_score > 21:
            return "computer"
        elif players_score > computers_score:
            return "player"
        elif computers_score > players_score:
            return "computer"
        else:
            return "draw"
def computer_algo():
    computers_cards = [random.choice(cards) for i in range(2)]
    computers_score = sum(computers_cards)
    if computers_score <17 :
        computers_cards.append(random.choice(cards))
        computers_score= sum(computers_cards)
    return computers_score, computers_cards
def player_hit(players_cards):
    hit = 0
    continuee = ''

    while hit < 2:
        continuee = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if continuee == 'y':
            players_cards.append(random.choice(cards))
            players_score = sum(players_cards)
            hit += 1
            print(f"Your cards: {players_cards}, Total score: {players_score}")
        elif continuee == 'n':
            break

    players_score = sum(players_cards)
    return players_score
def result(winner):
    if winnerr == "player":
        print("Opponent went over. You win 😁")
    elif winnerr == "computer":
        print("You went over. You lose 😭")
    elif winnerr == "draw":
        print("It's a draw 😐 ")
while play!='n':
    print(logo)
    players_cards = [random.choice(cards) for i in range(2)]
    print(f"Your cards: {players_cards}")
    computers_score, computers_cards = computer_algo()
    print(f"Computer's first card: {computers_cards[0]}")
    players_score = player_hit(players_cards)
    winnerr =winner(players_score, computers_score)
    print(f"Your final hand: {players_cards} , final score: {players_score}")
    print(f"computer's final hand: {computers_cards}, final score:{computers_score}")
    result(winnerr)
    play = input("Do you want to continue playing the game of Blackjack? Type 'y' or 'n':  ").lower()
    if play == 'n':
        print("Thanks for playing!")
    else:
        print("\n"*20)
        





