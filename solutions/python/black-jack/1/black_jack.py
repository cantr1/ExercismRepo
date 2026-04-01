"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    match card:
        case 'J' | 'Q' | 'K':
            return 10
        case 'A':
            return 1
        case _:
            return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    c1 = value_of_card(card_one)
    c2 = value_of_card(card_two)

    if c1 > c2:
        return card_one
    elif c2 > c1:
        return card_two
    elif c1 == c2:
        return card_one,card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    c1 = 11 if card_one == 'A' else value_of_card(card_one)
    c2 = 11 if card_two == 'A' else value_of_card(card_two)

    total_value = c1 + c2

    if total_value + 11 <= 21:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    cards = {card_one, card_two}
    return ('A' in cards) and (card_one in ['10', 'J', 'Q', 'K'] or card_two in ['10', 'J', 'Q', 'K'])


def can_split_pairs(card_one, card_two):
    """Return True if both cards have the same value (e.g. 'K' and 'J' both count as 10)."""
    return value_of_card(card_one) == value_of_card(card_two)

def can_double_down(card_one, card_two):
    """Return True if the total of the two cards is 9, 10, or 11."""
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
