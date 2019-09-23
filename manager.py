import random


class ItemManager:
    def __init__(self):
        self.items = list()

    def register_item(self, item):
        if not hasattr(item, 'owner'):
            raise AttributeError("Item must have 'owner' attribute to be registered")
        if self.items.count(item) > 0:
            raise RuntimeError("Item already registered")
        self.items.append(item)
        self.assign_owner(item, None)

    def assign_owner(self, item, owner):
        try:
            index = self.items.index(item)
        except ValueError:
            print("Item isn't registered with ItemManager")
        self.items[index].owner = owner

    def get_items(self):
        return self.items

    def get_item_count(self):
        return len(self.get_items())

    def get_filtered_items(self, filters):
        return list(filter(lambda x: all(f(x) for f in filters), self.items))

    def get_owned_items(self, owner):
        def f1(x): return x.owner == owner
        return self.get_filtered_items([f1,])

    def shuffle(self):
        random.shuffle(self.items)


class CardManager(ItemManager):
    def get_played_cards(self, owner):
        def f1(x): return x.owner == owner
        def f2(x): return x.in_hand == False
        return self.get_filtered_items([f1, f2,])

    def put_four_in_play(self):
        def f1(x): return x.owner == None
        cards = self.get_filtered_items([f1,])

        for card in self.items[0:min(4, len(cards))]:
            self.items[card].in_play = True


class TokenManager(ItemManager):
    pass


class TileManager(ItemManager):
    pass
