#!/usr/bin/env python
'''
Implementation of Splendor game in python.

Author: Eliezer Kanal
'''

import pickle
import random

from settings import NUM_TOKENS, GEMS, WILD, CARDS_FILE, TILES_FILE
import components as c


class Game:
    def __init__(self, num_players):
        self.players = []
        self.tokens = {gem: 0 for gem in GEMS+WILD}
        self.cards = {1: [], 2: [], 3: []}
        self.tiles = []

        # create tokens
        num_tokens = NUM_TOKENS[num_players]
        for token in GEMS:
            self.tokens[token] = num_tokens
        for token in WILD:
            self.tokens[token] = 5

        # define the playing cards
        with open(CARDS_FILE, 'rb') as f:
            cards = pickle.load(f)
        
        for card in cards:
            self.cards[card[0]].append(card[1:])

        for level in self.cards:
            random.shuffle(self.cards[level])

        # define the tiles
        with open(TILES_FILE, 'rb') as f:
            tiles = pickle.load(f)
        
        for tile in tiles:
            self.tiles.append(c.Tile(*tile))

        random.shuffle(self.tiles)

        # add players
        for _ in range(num_players):
            self.players.append(c.Player())

        # set up first turn
        self.current_player = self.players[0]

        # set up currently shown cards


        self.take_turn()

    def check_earned_tile(self):
        for tile in self.tiles:
            for player in self.players:
                # TODO: working here
                pass


    def take_turn(self):
        pass
