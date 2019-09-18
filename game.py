#!/usr/bin/env python
'''
Implementation of Splendor game in python.

Author: Eliezer Kanal
'''

import pickle

import settings
import components as c


class Game:
    def __init__(self, num_players):
        num_tokens = settings.NUM_TOKENS[num_players]

        # create tokens
        self.tokens = {}
        for gem in settings.GEMS:
            self.tokens[gem] = []
            for _ in range(num_tokens):
                self.tokens[gem].append(c.Token(gem))

        # add wilds
        self.tokens['g'] = [c.Token('g') for n in range(5)]

        # define the playing cards
        cards = pickle.loads(open(settings.CARDS_FILE, 'r'))
        self.cards = []
        for card in cards:
            self.cards.append(c.Card(*card))

        # define the tiles
        tiles = pickle.loads(open(settings.TILES_FILE, 'r'))
        self.tiles = []
        for tile in tiles:
            self.tiles.append(c.Tile(*tile))

        # add players
        self.players = []
        for _ in range(num_players):
            self.players.append(c.Player())

        # useful vars
        self.current_player = self.players[0]

        self.take_turn()

    def check_earned_tile(self):
        for tile in self.tiles:
            for player in self.players:
                # TODO: working here
                pass


    def take_turn(self):
        pass

