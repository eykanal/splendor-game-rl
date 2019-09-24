import pickle

from settings import NUM_TOKENS, GEMS, WILD, CARDS_FILE, TILES_FILE
from models import Card, Tile, Token, Player, Bank


class Game:
    bank = Bank()
    
    def __init__(self, num_players):
        # set up first turn
        self.current_player = self.players[0]
        # self.cards.put_four_in_play()

        # run main loop
        # self.play()

    def check_earned_tile(self):
        for tile in self.tiles:
            for player in self.players:
                # TODO: working here
                pass

    def play(self):
        for player in self.players:
            self.players[player].move()

        pass
