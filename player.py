import deck as deck_mod
from errors import EmptyDeckError

class Player():
    """ Representation of a player """

    def __init__(self):

        self.deck = deck_mod.new_deck()
        self.hand = deck_mod.Deck()
        self.discard = deck_mod.Deck()
        self.played = deck_mod.Deck()
        
        self.draw_hand()

        print(self.hand)
        # self.game = game
        self.prepare_turn()

    def take_turn(self):
        """ Placeholder take-turn logic """

        print(self.hand)

        for card in self.hand:
            card.play(self)

        self.end_turn()



    def end_turn(self):
        """ Wraps up turn Discard cards in play and redraw """

        # Discard cards in play
        self.discard.combine(self.hand)
        self.discard.combine(self.played)
        
        # Draw new hand and prep next turn
        self.draw_hand()
        self.prepare_turn()



    def prepare_turn(self):
        """ Prepares a new turn for the player """
        self.buying_power = 0
        self.actions = 1
        self.buys = 1


    def draw_hand(self):
        """draws hand of 5 cards from the deck"""
        for _ in range(5):

            try:
                self.hand.add_card(self.deck.draw_card())
            except EmptyDeckError:

                # Try to shuffle back in discard
                self.shuffle_in_discard()
                try:
                    self.hand.add_card(self.deck.draw_card())
                # If the deck is still empty (an edgecase if player has very few cards), give up
                except EmptyDeckError:
                    return


    def shuffle_in_discard(self):
        self.deck.combine(self.discard)



    def __repr__(self):
        return "Player has " + self.buying_power + " bp and " + self.actions  + " actions and " + self.buys + " and deck is: " + self.deck


    # def pretty_print(self):
    #     """ Detailed log of the player's gamestate information"""


if __name__ == "__main__":
    my_player = Player()

    print("Player hand is: ")
    print(my_player.hand)
    print("Player deck is: ")
    print(my_player.deck)
