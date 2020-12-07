from abc import ABC, abstractmethod
import player

class Card(ABC):
    """Abstract Card Object"""

    name = "Generic Card"

    @abstractmethod
    def play(self):
        return

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Coin(Card):
    """ Generic Coin-type Card""" 

    value = 0

    def play(self, player):
        player.buying_power += self.value
        print(f"{self} played.  BP = {player.buying_power}")
        return

    def __repr__(self):
        return f"{self.name} Card worth {self.value}"

    def __str__(self):
        return super().__str__()

class Copper(Coin):
    """ A Coin with value 1"""
    name = "Copper"
    value = 1
    cost = 0


class Silver(Coin):
    """ A Coin with value 2"""
    name = "Silver"
    value = 2
    cost = 3
    
class Gold(Coin):
    """ A Coin with value 3"""
    name = "Gold"
    value = 3
    cost = 6

class Platinum(Coin):
    """ A Coin with value 5"""
    name = "Platinum"
    value = 5
    cost = 9




class VictoryCard(Card):
    """ Generic Victory_Point Card""" 

    vp = 0

    def play(self, player):
        print(f"VP Card {self} Played to No Effect")
        return

    def __repr__(self):
        return f"{self.name} Card worth {self.vp} Victory Points"

    def __str__(self):
        return super().__str__()

class Estate(VictoryCard):
    """Estate worth 1 VP"""
    name = "Estate"
    vp = 1
    cost = 2

class Duchy(VictoryCard):
    """Duchy worth 3 VP"""
    name = "Duchy"
    vp = 3
    cost = 5

class Province(VictoryCard):
    """Province worth 6 VP"""
    name = "Province"
    vp = 6
    cost = 8