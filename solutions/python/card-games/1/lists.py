"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    list = []
    for x in range(number, number + 3):
        list.append(x)
    return list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    pass
    list = rounds_1 + rounds_2
    return list

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return True if number in rounds else False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    avg = card_average(hand)
    first_last = (hand[0] + hand[len(hand) - 1]) / 2
    if first_last == avg:
        return True
        
    for item in hand:
        if item == avg:
            return True 
            
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_index_total = 0
    even_index_count = 0
    odd_index_total = 0
    odd_index_count = 0

    for idx, value in enumerate(hand):
        if idx % 2 == 0:
            even_index_total += value
            even_index_count += 1
        else:
            odd_index_total += value
            odd_index_count += 1

    # Avoid division by zero (just in case)
    if even_index_count == 0 or odd_index_count == 0:
        return False

    return (even_index_total / even_index_count) == (odd_index_total / odd_index_count)


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[len(hand) - 1] == 11:
        hand[len(hand) - 1] = 22
    return hand
