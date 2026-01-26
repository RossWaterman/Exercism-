"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand)/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    return ((hand[0] + hand[-1])/2) == card_average(hand) or (hand[len(hand)//2]) == card_average(hand)


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even_cards = []
    odd_cards = []
    for e in range(0,len(hand),2):
        even_cards.append(hand[e])
    for o in range(1,len(hand),2):
        odd_cards.append(hand[o])
    return sum(even_cards)/len(even_cards) == sum(odd_cards)/len(odd_cards)


def maybe_double_last(hand):
    """Double last position if it's 11 (tuple or flat list)."""
    new_hand = []
    for item in hand:
        if isinstance(item, (list, tuple)) and item[-1] == 11:
            item_list = list(item)
            item_list[-1] = 22
            new_hand.append(tuple(item_list))
        elif isinstance(item, int) and hand[-1] == 11:
            hand = list(hand)
            hand[-1] = 22
            return hand
        else:
            new_hand.append(item)
    return new_hand

    
            
