import deck as deck_mod

class Player():
    """ Representation of a player """

    def __init__(self):

        self.deck = deck_mod.new_deck()
        self.hand = deck_mod.Deck()
        self.discard = deck_mod.Deck()
        self.played = deck_mod.Deck()
        
        self.draw_hand()

        # self.game = game
        self.prepare_turn()

    def take_turn(self):
        """ Placeholder take-turn logic """
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
            # Draw a card if possible
            if (card := self.deck.draw_card()):
                self.hand.add_card(card)
            # if not, shuffle in the discard pile and try again
            else:
                self.shuffle_in_discard()
                # Try again to draw a card
                if (card := self.deck.draw_card()):
                    self.hand.add_card(card)
                # if there are no cards in deck, then player has drawn all their cards
                else:
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
