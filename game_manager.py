import player
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


if __name__ == "__main__":
    gm = gameManager()
    gm.play_game()
