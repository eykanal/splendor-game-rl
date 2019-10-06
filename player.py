from settings import GEMS, WILD
from utils import connect_to_db


class Player():
    def __init__(self, player_id, game_id):
        self.id = player_id
        self.game_id = game_id

    def _buy_card(self, card, tokens):
        """
        Buy a card from table

        Args:
            card: the ObjectId of a card not currently owned
            tokens: dict with count of tokens to be spent, must sum to cost of
                   card
        """
        db = connect_to_db()
        db.cards.update_one(
            {"_id": card},
            [{"$set": {"owner": self.id}}, {"$unset": "in_play"}])
        for token in tokens:
            self._return_n_tokens(token)

    def _take_card(self, card):
        db = connect_to_db()
        result = db.cards.update_one(
            {"_id": card},
            [{"$set": {"owner": self.id, "in_hand": True}}, {"$unset": "in_play"}])
        gold_tokens = db.tokens.count_documents(
            {"game_id": self.game_id, "owner": {"$exists": False}, "gem": {"$in": WILD}})
        if result > 0:
            self._take_1_token(WILD)
        db.cards.update_one
        
    def _take_3_tokens(self, tokens):
        """
        Take tokens from the piles

        Args:
            tokens: list of tokens to be taken by name
        """
        for token in tokens:
            self._take_1_token(token)

    def _take_1_token(self, token):
        db = connect_to_db()
        result = db.tokens.find({"gem": token, "owner": {"$exists": False}}).limit(1)
        assert list(result), "Stack for requested token empty"
        db.tokens.update_one({"_id": result[0]["_id"]}, {"$set": {"owner": self.id}})

    def _return_n_tokens(self, token, n=1):
        db = connect_to_db()
        result = db.tokens.find({"gem": token, "owner": self.id}).limit(1)
        db.tokens.update_one({"_id": result[0]["_id"]}, {"$unset": "owner"})
