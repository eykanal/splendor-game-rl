import mongoengine as me


class CardQuerySet(me.QuerySet):
    def find_level(self, level):
        return self.filter(level=level)

    def bought(self, player):
        return self.filter(player=player, in_hand=False)

    def in_hand(self, player):
        return self.filter(player=player, in_hand=True)



class Card(me.Document):
    in_hand = me.BooleanField()
    in_play = me.BooleanField()
    level = me.IntField()
    gem = me.StringField()
    cost = me.ListField(me.IntField())
    prestige = me.IntField()

    meta = {'queryset_class': CardQuerySet}


class Tile(me.Document):
    requirement = me.ListField()
    prestige = me.IntField()


class Token(me.Document):
    gem = me.StringField()


class Player(me.Document):
    tiles = me.ListField(me.ReferenceField(Tile))
    cards = me.ListField(me.ReferenceField(Card))
    tokens = me.ListField(me.ReferenceField(Token))


class DefaultGame(me.Document):
    players = me.ListField(me.ReferenceField(Player))
