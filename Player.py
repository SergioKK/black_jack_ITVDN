import abc
from Deck import Deck
import random

from const import MESSAGES

class AbstractPlayer(abc.ABC):

    def __init__(self):
        self.cards = []
        self.bet = 0
        self.full_points = 0
        self.money = 100

    def change_points(self):
        self.full_points = sum([card.points for card in self.cards])


    @abc.abstractmethod
    def change_bet(self,  max_bet, min_bet):
        pass

    def print_cards(self):
        print(self, "bot data")
        for card in self.cards:
            print(card)
        print(self.full_points)

    def take_card(self, card):
        self.cards.append(card)
        self.change_points()


class Player(AbstractPlayer):


    def change_bet(self, max_bet, min_bet):
        while True:
            value = int(input('Make your bet: '))
            if max_bet > value > min_bet:
                self.bet = value
                self.money -= self.bet
                break
        print('Your bet is: ', self.bet)

    def ask_card(self):
        choice = input(MESSAGES.get('ask_card'))
        if choice == 'y':
            return True
        else:
            return False

class Bot(AbstractPlayer):

    def __init__(self):
        super().__init__()
        self.max_points = random.randint(17, 20)

    def change_bet(self, max_bet, min_bet):
        self.bet = random.randint(min_bet, max_bet)
        self.money -= self.bet
        print(self, 'give: ', self.bet)

    def ask_card(self):
        if self.max_points > self.full_points:
            return True
        else:
            return False

class Dealer(AbstractPlayer):

    max_points = 17

    def change_bet(self,  max_bet, min_bet):
        """
        NOTE: This type is Dealer so it has no bets
        :param max_bet:
        :param min_bet:
        :return:
        """
        raise Exception('This type is dealer so it has no bet')

    def ask_card(self):
        if self.max_points > self.full_points:
            return True
        else:
            return False
