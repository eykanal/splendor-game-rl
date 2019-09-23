import pickle
import json

import click
import mongoengine as me

from settings import GEMS, WILD
from models import Card, Tile, Token, DefaultGame


@click.group()
def cli():
    pass

@cli.command()
@click.argument('json_file')
def pickle_data(json_file):
    """
    Read card or tile data from JSON_FILE and save to pickle format.
    """
    data = json.load(open(json_file, "r"))
    # output file has same name but add .p extension
    output_name = '.'.join(json_file.split('.')[0:-1])
    pickle.dump(data, open("%s.p" % output_name, "wb"))

@cli.command()
def init_mongo():
    """
    Populate the mongo database with default game data
    """
    me.connect("splendor")

    card_data = json.load(open('cards.json', 'r'))
    tile_data = json.load(open('tiles.json', 'r'))

    card_params = ('level', 'gem', 'cost', 'prestige')
    tile_params = ('requirement', 'prestige')
    cards = [Card(**{h:d for h, d in zip(card_params, dat)}) for dat in card_data]
    tiles = [Tile(**{h:d for h, d in zip(tile_params, dat)}) for dat in tile_data]
    tokens = [Token(gem=gem) for gem in GEMS * 7 + WILD * 5]

    [c.save() for c in cards]
    [t.save() for t in tiles]
    [t.save() for t in tokens]

    default_game = DefaultGame()
    default_game.save()
    default_game.cards = cards
    default_game.tiles = tiles
    default_game.tokens = tokens
    default_game.save()

if __name__ == "__main__":
    cli()
