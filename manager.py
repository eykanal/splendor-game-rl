import random
import json


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

    def _get_filtered_indices(self, filter_tuples):
        # returns list of bool values indicating filter match
        filters = []
        for filt in filter_tuples:
            def fx(x): return getattr(x, filt[0]) == filt[1]
            filters.append(fx)
        return list(map(lambda x: all(f(x) for f in filters), self.items))

    def get_owned_items(self, owner):
        filt = [("owner", owner),]
        return self._get_filtered_indices(filt)

    def shuffle(self):
        random.shuffle(self.items)

    def to_json(self):
        return self.items

    def to_jsons(self):
        json.dumps(self.items)


class CardManager(ItemManager):
    def get_played_cards(self, owner):
        filt = [("owner", owner), ("in_hand", False)]
        return self._get_filtered_indices(filt)

    def put_four_in_play(self):
        for level in range(3):
            filt = [("owner", None), ("level", level)]
            ind = self._get_filtered_indices(filt)

            for card in ind[0:min(4, sum(ind))]:
                self.items[card].in_play = True


class TokenManager(ItemManager):
    def _get_one(self, gem):
        filt = [("gem", gem), ("owner", None)]
        token = self._get_filtered_indices(filt)
        return token[0]

    def take(self, gem, owner):
        pass


class TileManager(ItemManager):
    pass
