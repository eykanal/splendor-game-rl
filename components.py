#!/usr/bin/env python
'''
Implementation of Splendor game in python.

Author: Eliezer Kanal
'''
from settings import GEMS, WILD


class Player:
    def __init__(self):
        all_tokens = GEMS + WILD
        self.tokens = {gem: 0 for gem in all_tokens}
        self.cards = {gem: [] for gem in GEMS}
        self.hand = []
        self.tiles = []

    def prestige(self):
        card_prestige = sum([c.prestige for c in self.cards])
        tile_prestige = sum([t.prestige for t in self.tiles])
        return card_prestige + tile_prestige

    def card_counts(self):
        return list(self.cards.values())

    def play_turn(self):
        pass

    def _take_three_tokens(self, tokens, game):
        '''
        User chooses the "takes three tokens" action.

        Args:
            tokens: list of the three gem names (from settings.GEMS)
            game: instance of Game from which tokens should be taken

        Returns:
            game: updated Game instance
        '''
        for token in tokens:
            if game.tokens[token] == 0:
                raise RuntimeError('Requested token from empty pile')
            game.tokens[token] -= 1
            self.tokens[token] += 1
        return game

    def _take_two_tokens(self, token, game):
        '''
        User chooses the "takes two tokens" action.

        Args:
            tokens: string of chosen token (from settings.GEMS)
            game: instance of Game from which tokens should be taken

        Returns:
            game: updated Game instance
        '''
        if game.tokens[token] < 4:
            raise RuntimeError('Requested two token from pile of 3 or less')
        game.tokens[token] -= 2
        self.tokens[token] += 2
        return game

    def _take card(self, card, game):
        pass

    def _discard_tokens(self):
        '''
        Called at the end of a turn, this discards tokens if the Player has
        more than the allowable number of tokens.
        '''


class Token:
    def __init__(self, gem):
        self.gem = gem
        self.owner = None

    def take(self, player):
        self.owner = player


class Card:
    def __init__(self, level, gem, cost, prestige):
        self.level = level
        self.gem = gem
        self.cost = cost
        self.prestige = prestige
        self.owner = None


class Tile:
    def __init__(self, requirement, prestige):
        self.requirement = requirement
        self.prestige = prestige
        self.owner = None
