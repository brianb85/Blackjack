"""
Assignment 5 - Blackjack
"""

import random

new_game = True


def add_card_to_hand(hand):
    card = random.randint(1, 13)
    if card == 1:
        card_value = 11
        card_name = "Ace"
    elif card == 11:
        card_value = 10
        card_name = "Jack"
    elif card == 12:
        card_value = 10
        card_name = "Queen"
    elif card == 13:
        card_value = 10
        card_name = "King"
    else:
        card_value = card
        card_name = card
    card_number = len(hand) + 1
    key = "card" + str(card_number)
    hand[key] = [card_value, card_name]
    return hand


def dict_key(hand):
    card_location = len(hand)
    key = "card" + str(card_location)
    return key


def hand_total(hand):
    hand_value = 0
    for x in hand:
        hand_value = hand_value + hand[x][0]
    return hand_value


def player_turn(player_total, player_hand):
    while player_total <= 20:
        player_choice = input("Would you like to [h]it or [s]tand?")
        if player_choice == "h" or player_choice == "H":
            add_card_to_hand(player_hand)
            player_total = hand_total(player_hand)
            print(f"\nHit! You drew a {player_hand[dict_key(player_hand)][1]}. Your total is {player_total}\n")
            if player_total == 21:
                print("You stand at 21")
                continue
            elif player_total > 21:
                for x in player_hand:
                    if player_hand[x][0] == 11:
                        player_hand[x][0] = 1
                        player_total = hand_total(player_hand)
                        print(f"Your Ace changes value to one. Your total is {player_total}\n")
                        break
            else:
                continue
        elif player_choice == "s" or player_choice == "S":
            return player_total
        else:
            print("\nPlease enter a valid selection\n")
    return player_total


def dealer_turn(dealer_total, dealer_hand):
    print(f"\nThe dealer reveals a hidden card of {dealer_hand["card2"][1]} and has a total of {dealer_total}\n")
    while dealer_total < 17:
        add_card_to_hand(dealer_hand)
        dealer_total = hand_total(dealer_hand)
        print(f"Hit! the dealer draws a {dealer_hand[dict_key(dealer_hand)][1]}. Their total is {dealer_total}\n")
        if dealer_total > 21:
            for x in dealer_hand:
                if dealer_hand[x][0] == 11:
                    dealer_hand[x][0] = 1
                    dealer_total = hand_total(dealer_hand)
                    print(f"The Dealer's Ace changes value to one. The Dealer's total is {dealer_total}\n")
                    break
    return dealer_total


def main():
    player_hand = {}
    dealer_hand = {}
    add_card_to_hand(player_hand)
    add_card_to_hand(player_hand)
    add_card_to_hand(dealer_hand)
    add_card_to_hand(dealer_hand)
    player_total = hand_total(player_hand)
    dealer_total = hand_total(dealer_hand)
    print(f"\nYou draw a {player_hand["card1"][1]} and a {player_hand["card2"][1]}. Your total is {player_total}\n")
    print(f"Dealer draws a {dealer_hand["card1"][1]} and a hidden card\n")
    player_total = player_turn(player_total, player_hand)
    if player_total > 21:
        print("You bust!")
        return
    dealer_total = dealer_turn(dealer_total, dealer_hand)
    if dealer_total > 21:
        print("The Dealer busts! You win!\n")
        return
    elif dealer_total >= player_total:
        print(f"You have {player_total} and the dealer has {dealer_total}. The Dealer wins!\n")
        return
    else:
        print(f"You have {player_total} and the dealer has {dealer_total}. You Win!\n")
        return


print("Welcome to Blackjack!")
while new_game:
    print(f"{"-"*60}\n")
    game = input("Do you want to play a new game? (y/n): ")
    if game == "n" or game == "N":
        print("\nThank you for playing!")
        break
    elif game == "y" or game == "Y":
        main()
    else:
        print("\nPlease select a valid option:")
