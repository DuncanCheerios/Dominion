import player
import deck
import card

COPPER_COUNT = 46
SILVER_COUNT = 40
GOLD_COUNT = 30
VP_COUNT = 8

class gameManager():
    """ Game Manager Object handles turn logic and the board state """

    def __init__(self):
        self.first_player = player.Player()
        self.second_player = player.Player()


    def play_game(self):

        for turn in range(5):
            print(f"\nRound {turn + 1}: ")
            print(f"Player 1 Turn: ")
            self.first_player.take_turn()
            print(f"\nPlayer 2 Turn: ")
            self.second_player.take_turn()


    def check_victory(self):
        """ Checks for game-over conditions """
        



class Kingdom_Cards():
    """ Representation of the Kingdom Cards, VP card and Coin Cards """

    def __init__(self):

        cards_dict = {}

        cards_dict["Copper"] = (deck.card_stack(card.Copper, COPPER_COUNT))
        cards_dict["Silver"] = (deck.card_stack(card.Silver, SILVER_COUNT))
        cards_dict["Gold"] = (deck.card_stack(card.Gold, GOLD_COUNT))
        cards_dict["Estate"] = (deck.card_stack(card.Estate, VP_COUNT))
        cards_dict["Duchy"] = (deck.card_stack(card.Duchy, VP_COUNT))
        cards_dict["Province"] = (deck.card_stack(card.Province, VP_COUNT))


if __name__ == "__main__":
    gm = gameManager()
    gm.play_game()
    KC = Kingdom_Cards()
