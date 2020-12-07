from random import shuffle
from errors import EmptyDeckError
from collections import Counter
import card
import player

class Deck():
    """ Representation of a deck of cards.  Useful for decks, trash, discard, etc """

    def __init__(self):
        self.cards = []

        # Visibility of the top card
        self.visible = False

    def add_card(self, card):
        """ Adds card to the top of the deck.  Does not shuffle """
        self.cards.insert(0, card)


    def shuffle(self):
        """ Shuffle the deck of cards """
        shuffle(self.cards)


    def draw_card(self):
        """ removes and returns the top card or None if deck is empty"""
        try:
            return self.cards.pop(0)
        except IndexError:
            raise EmptyDeckError
        

    def combine(self, other_deck):
        """ Combines this deck and the other_deck.  Result shuffled and stored in this """
        self.cards.extend(other_deck.cards)
        other_deck.cards = []
        self.shuffle()


    def count(self):
        """ Count/Return cards in the deck"""
        return len(self.cards)

    def __iter__(self):
        return DeckIterator(self)

    # TODO Change this?
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        card_data = []
        for card, count in Counter(self.cards).items():
            card_data.append(f"{card.__str__()}: {count}")
        return "; ".join(card_data)


class DeckIterator:
    """Iterator for Deck"""
    def __init__(self, deck):
        self._deck = deck
        self._index = 0
    
    def __next__(self):
        """ Grabs next card in deck"""
        if self._index < (len(self._deck.cards)):
            return_card = self._deck.cards[self._index]
            self._index += 1
            return return_card
        raise StopIteration


def new_deck():
    """ Creates and returns starter deck of 7 coppers, 3 estates"""
    return_deck = Deck()

    # Add 7 copper and 3 Estate
    for _ in range(7):
        return_deck.add_card( card.Copper() )
    for _ in range(3):
        return_deck.add_card( card.Estate() )
    
    #Shuffle and return
    return_deck.shuffle()
    return return_deck


def card_stack(card_name, count):
    """ Creates/Returns a stack of <count> cards"""
    stack = Deck()
    for _ in range(count):
        stack.add_card(card_name())
    return stack





if __name__ == "__main__":

    deck = new_deck()
    deck.shuffle()
    print(deck)

    Joe = player.Player()

    try:
        while (_card := deck.draw_card()):
            _card.play(Joe)
    except EmptyDeckError:
        pass


    print(Joe.buying_power)
