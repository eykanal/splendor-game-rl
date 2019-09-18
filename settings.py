#!/usr/bin/env python
'''
Implementation of Splendor game in python.

Author: Eliezer Kanal
'''

NUM_PLAYERS = [2, 3, 4]
NUM_TOKENS = {
    NUM_PLAYERS[0]: 4,
    NUM_PLAYERS[1]: 5,
    NUM_PLAYERS[2]: 7,
}

GEMS = ['diamond', 'emerald', 'onyx', 'ruby', 'sapphire']
WILD = ['gold', ]

CARDS_FILE = 'cards.p'
TILES_FILE = 'tiles.p'

# The below are inclusive (≤)
MAX_PLAYER_TOKENS = 10
MAX_PLAYER_HAND = 3

WINNING_SCORE = 15
