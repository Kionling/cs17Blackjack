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

