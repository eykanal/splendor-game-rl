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

    def __str__(self):
        c = "".join([str(i) for i in self.cost])
        return "%s-%s-%s" % (self.gem, c, self.prestige)


class Tile(me.Document):
    requirement = me.ListField()
    prestige = me.IntField()

    def __str__(self):
        req = "".join([str(i) for i in self.requirement])
        return "%s-%s" % (req, self.prestige)


class Token(me.Document):
    gem = me.StringField()

    def __str__(self):
        return self.gem


class Bank(me.Document):
    tiles = me.ListField(me.ReferenceField(Tile))
    cards = me.ListField(me.ReferenceField(Card))
    tokens = me.ListField(me.ReferenceField(Token))

    meta = {'allow_inheritance': True}


class Player(Bank):
    num_turns_played = me.IntField()


class Game(me.Document):
    players = me.ListField(me.ReferenceField(Player))
