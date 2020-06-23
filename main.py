from Deck import Deck
from Game import Game
from Player import Bot


if __name__ == '__main__':
    g = Game()
    g.start_game()

    for pl in g.players:
        print(pl.full_points)
    print(g.player_pos)
