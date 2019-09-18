#!/usr/bin/env python
'''
Implementation of Splendor game in python.

Author: Eliezer Kanal
'''


class Player:
    def __init__(self):
        self.tokens = []
        self.cards = []
        self.tiles = []

    def prestige(self):
        card_prestige = sum([c.prestige for c in self.cards])
        tile_prestige = sum([t.prestige for t in self.tiles])
        return card_prestige + tile_prestige


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


class Tile:
    def __init__(self, requirement, prestige):
        self.requirement = requirement
        self.prestige = prestige
