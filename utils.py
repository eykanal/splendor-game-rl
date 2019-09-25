import pickle
import json

import click
import mongoengine as me
import pymongo

from settings import GEMS, WILD
from models import Card, Tile, Token


def connect_to_db():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.splendor
    return db

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
    card_data = json.load(open('cards.json', 'r'))
    tile_data = json.load(open('tiles.json', 'r'))

    db = connect_to_db()

    if db.cards.count_documents({}) is 0:
        db.cards.insert_many(card_data)
    if db.tiles.count_documents({}) is 0:
        db.tiles.insert_many(tile_data)
    if db.tokens.count_documents({}) is 0:
        token_data = [{"gem": gem} for gem in GEMS*7 + WILD*5]
        db.tokens.insert_many(token_data)

def drop_all_games():
    db = connect_to_db()

    db.cards.delete_many({"game_id": {"$exists": True}})
    db.tiles.delete_many({"game_id": {"$exists": True}})
    db.tokens.delete_many({"game_id": {"$exists": True}})
    db.players.delete_many({})
    db.games.delete_many({})

if __name__ == "__main__":
    cli()
