import random
import datetime

from player import Player
from utils import connect_to_db


class Game:
    def __init__(self, num_players):
        self.players = []
        self.db = None
        self.game_id = None

        # set up new game
        db = connect_to_db()
        self.db = db  # for later, will use db now for convenience

        game = db.games.insert_one({"turns_taken": 0, "started": datetime.datetime.now()})
        game_id = game.inserted_id
        self.game_id = game_id

        # get lists from ground truth collections
        cards_gt = db.cards.find({"game_id": {"$exists": False}}, {"_id": 0})
        tokens_gt = db.tokens.find({"game_id": {"$exists": False}}, {"_id": 0})
        tiles_gt = db.tiles.find({"game_id": {"$exists": False}}, {"_id": 0})

        # re-insert all the cards with a game ID
        game_cards = [dict(i, game_id=game_id) for i in cards_gt]
        game_tokens = [dict(i, game_id=game_id) for i in tokens_gt]
        all_game_tiles = [dict(i, game_id=game_id) for i in tiles_gt]
        game_tiles = random.sample(all_game_tiles, 4)  # only need four for a game

        db.cards.insert_many(game_cards)
        db.tiles.insert_many(game_tiles)
        db.tokens.insert_many(game_tokens)

        # create players
        player_ids = db.players.insert_many([{"game_id": game_id, "order": i} for i in range(3)])
        self.players = [Player(player_id) for player_id in player_ids]

        # set tokens appropriately
        token_count = db.tokens.count_documents({'game_id': game_id, 'gem': 'onyx'})
        if num_players in [2, 3] and token_count > 5:
            gems = db.tokens.distinct('gem')
            del gems[gems.index('gold')]
            for gem in gems:
                db.tokens.delete_one({'game_id': game_id, 'gem': gem})
                db.tokens.delete_one({'game_id': game_id, 'gem': gem})
                if num_players == 3:
                    db.tokens.delete_one({'game_id': game_id, 'gem': gem})

        # show four cards
        cards = list(db.cards.find({"game_id": game_id}))
        show_cards = []
        for level in db.cards.distinct('level'):
            l = list(filter(lambda x: x['level'] == level, cards))
            s = random.sample(l, 4)
            show_cards.extend(s)
        db.cards.update_many(
            {"_id": {"$in": [n["_id"] for n in show_cards]}},
            {"$set": {"in_play": True}})

        # play game
        self.play()

    def check_earned_tile(self):
        pass

    def get_scores(self):
        score = []
        for item in ['tiles', 'cards']:
            result = self.db[item].aggregate([
                {"$match": {"game_id": self.game_id, "player_id": {"$exists": True}}},
                {"$group": {"_id": "$player_id", "score": {"$sum": "$prestige"}}}
            ])
            score.append(result)
        # TODO: actually add these things together

    def play(self):
        for player in self.players:
            self.players[player].move()

            if all(map(lambda x: x > 15, self.get_scores())):
                # TODO: find the number of turns, stop when all equal
                # TODO: break out of loop and quit
                pass
