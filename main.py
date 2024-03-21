import random


def create_deck(): 
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck

    
def hand_value(hand):
    value = 0
    ace_count = 0
    for card in hand:
        if card['value'] in ['Jack', 'Queen', 'King']:
            value += 10
        elif card['value'] == 'Ace':
            ace_count += 1
        else:
            value += int(card['value'])
    while ace_count > 0 and value + 10 <= 21:
        value += 10
        ace_count -= 1
    return value


def display_hand(hand, player_type):
    print(f"{player_type} hand:" + " ".join([f"{card['value']} of {card['suit']}" for card in hand]))
    print(f"{player_type} hand value: {hand_value(hand)}")


def blackjack():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    display_hand(player_hand, "Player")
    display_hand(dealer_hand, "Dealer")
    while hand_value(player_hand) < 21:
        hit_or_stand = input("Do you want to hit or stand? ")
        if hit_or_stand.lower() == "hit":
            player_hand.append(deck.pop())
            display_hand(player_hand, "Player")
        else:
            break
    if hand_value(player_hand) > 21:
        print("Player busts, dealer wins!")
        return
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        display_hand(dealer_hand, "Dealer")
    if hand_value(dealer_hand) > 21:
        print("Dealer busts, player wins!")
        return
    if hand_value(player_hand) > hand_value(dealer_hand):
        print("Player wins!")
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print("Dealer wins!")
    else:
        print("It's a tie!")
    play_again = input("Do you want to play again? ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
    else:
        blackjack()


if __name__ == "__main__":
    blackjack()