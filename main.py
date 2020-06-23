from Deck import Deck
from Game import Game

if __name__ == '__main__':
    g = Game()
    g.start_game()

    for pl in g.players:
        print(pl.full_points)
