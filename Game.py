import random

from Deck import Deck
import Player
from const import MESSAGES


class Game:
    max_pl_count = 4

    def __init__(self):
        self.players = []
        self.player = None
        self.player_pos = None
        self.dealer = Player.Dealer()
        self.all_players_count = 1
        self.deck = Deck()
        self.max_bet, self.min_bet = 20, 0

    @staticmethod
    def _ask_starting(message):
        while True:
            choice = input(message)
            if choice == 'n':
                return False
            elif choice == 'y':
                return True


    def _launching(self):
        bots_count = int(input("Hello, write bots count"))
        self.all_players_count = bots_count + 1
        for _ in range(bots_count):
            b = Player.Bot()
            self.players.append(b)
            print(b, " is created")

        self.player = Player.Player()
        self.player_pos = random.randint(0, self.all_players_count)
        print('Your position is: ', self.player_pos)
        self.players.insert(self.player_pos, self.player)

    def ask_bet(self):
        for player in self.players:
            player.change_bet(self.max_bet, self.min_bet)

    def first_descr(self):
        for player in self.players:
            for _ in range(2):
                card = self.deck.get_card()
                player.take_card(card)
        card = self.deck.get_card()
        self.players


    def check_stop(self, player):
        points = player.full_points
        if points >= 21:
            return True
        else:
            return False

    def remove_player(self, player):
        player.print_cards()
        self.players.remove(player)

    def ask_cards(self):
        for player in self.players:
            while player.ask_card():
                card = self.deck.get_card()
                player.take_card(card)

                is_stop = self.check_stop(player)
                if is_stop:
                    if player.full_points > 21 or isinstance(player, Player.Player):
                        self.remove_player(player)
                    break

                if isinstance(player, Player.Player):
                    player.print_cards()


    def chaeck_winner(self):
        if self.dealer.full_points > 21:
            # all win
            for winner in self.players:
                winner.money += winner.bet * 2
        else:
            for player in self.players:
                if player.full_points == self.dealer.full_points:
                    player.money += player.bet
                elif player.full_points > self.dealer.full_points:
                    player.money += player.bet * 2

    def play_with_dealer(self):
        while self.dealer.ask_card():
            card = self.deck.get_card()
            self.dealer.take_card(card)
        self.dealer.print_cards()

    def start_game(self):
        message = MESSAGES.get("ask_start")
        # todo: max players count?
        if not self._ask_starting(message=message):
            exit(1)

        # generating data for starting
        self._launching()

        # ask about bet
        self.ask_bet()

        # give first card to the players
        self.first_descr()

        # print player cards after first deal
        self.player.print_cards()


        self.ask_cards()

        self.play_with_dealer()

Game.asd = 10
