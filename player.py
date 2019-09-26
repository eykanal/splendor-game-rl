from settings import GEMS, WILD
from utils import connect_to_db


class Player():
    def __init__(self, player_id, game_id):
        self.id = player_id
        self.game_id = game_id

    def _buy_card(self, card, coins):
        """
        Buy a card from table

        Args:
            card: the ObjectId of a card not currently owned
            coins: dict with count of coins currently owned, must sum to cost of
                   card
        """
        db = connect_to_db()
        result = db.cards.update_one(
            {"_id": card},
            [{"$set": {"owner": self.id}}, {"$unset": "in_play"}])


    def _take_card(self, card):
        db = connect_to_db()
        result = db.cards.update_one(
            {"_id": card},
            [{"$set": {"owner": self.id, "in_hand": True}}, {"$unset": "in_play"}])
        gold_tokens = db.tokens.count_documents(
            {"game_id": self.game_id, "owner": {"$exists": False}, "gem": {"$in": WILD}})
        
    def _take_3_tokens(self, tokens):
        pass
