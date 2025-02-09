import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = (input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()

def game_result(players_score, computers_score, players_cards, computers_cards):
    if players_score > 21 and computers_score > 21:
        print("It's a draw 😐")
    elif computers_score > 21 or players_score > computers_score:
        print("Opponent went over. You win 😁")
    elif players_score > 21 or computers_score > players_score:
        print("You went over. You lose 😭")
    elif players_score == 21 and len(players_cards) == 2:
        print("Win with a Blackjack 😎")
    elif computers_score == 21 and len(computers_cards) == 2:
        print("Lose, opponent has Blackjack 😱")
    elif players_score == computers_score:
        print("It's a draw 🙃")

def computer_algo():
    computers_cards = [random.choice(cards) for i in range(2)]
    computers_score = sum(computers_cards)
    if computers_score < 17:
        computers_cards.append(random.choice(cards))
        computers_score = sum(computers_cards)
    return computers_score, computers_cards

def player_hit(players_cards, players_score):
    continuee = ''
    while players_score < 22:
        continuee = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continuee == 'y':
            players_cards.append(random.choice(cards))
            players_score = sum(players_cards)
            print(f"Your cards: {players_cards}, Total score: {players_score}")
        elif continuee == 'n':
            break
    return players_score

while play != 'n':
    print(logo)
    players_cards = [random.choice(cards) for i in range(2)]
    players_score = sum(players_cards)
    print(f"Your cards: {players_cards}")
    computers_score, computers_cards = computer_algo()
    print(f"Computer's first card: {computers_cards[0]}")
    players_score = player_hit(players_cards, players_score)
    print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
    print(f"Your final hand: {players_cards}, final score: {players_score}")
    game_result(players_score, computers_score, players_cards, computers_cards)

    play = input("Do you want to continue playing the game of Blackjack? Type 'y' or 'n': ").lower()
    if play == 'n':
        print("Thanks for playing!")
    else:
        print("\n" * 20)
