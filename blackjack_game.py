import random
from game_materials import *

print(logo)


def ran_card():
    one_card_from_deck = random.choice(card_list)
    return one_card_from_deck


another_game = True
while another_game:
    player_cards = []
    player_cards_value = []
    computer_cards = []
    computer_cards_value = []

    for _ in range(2):
        player_card = ran_card()
        computer_card = ran_card()
        for key in player_card:
            player_cards.append(key)
            player_cards_value.append(player_card[key])
        for key in computer_card:
            computer_cards.append(key)
            computer_cards_value.append(computer_card[key])

    print(f"Your cards: [{player_cards[0]}, {player_cards[1]}]")
    print(f"Computer's first card: {computer_cards[0]}")

    player_continue = True
    computer_continue = True
    while player_continue:
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "n":
            player_continue = False
        elif choice == "y":
            new_card = ran_card()
            for key in new_card:
                player_cards.append(key)
                player_cards_value.append((new_card[key]))

            print("---------------------------------------------------------------")
            print(f"Your final hand: {player_cards}")
            print(f"Computer's first card: {computer_cards[0]}")
            if sum(player_cards_value) > 21:
                player_continue = False
                computer_continue = False
                print(lose)

    while computer_continue:
        computer_choice = random.randint(0, 1)
        if computer_choice == 0:
            computer_continue = False
        else:
            new_card = ran_card()
            for key in new_card:
                computer_cards.append(key)
                computer_cards_value.append((new_card[key]))

        if sum(computer_cards_value) > 21:
            computer_continue = False
            print(win)

    if sum(player_cards_value) <= 21 and sum(computer_cards_value) <= 21:
        if sum(player_cards_value) == sum(computer_cards_value):
            print("Draw !!")
        elif sum(player_cards_value) > sum(computer_cards_value):
            print(win)
        else:
            print(lose)

    print(f"Your score: {sum(player_cards_value)}\nComputer Score: {sum(computer_cards_value)}")
    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if new_game == "n":
        another_game = False
