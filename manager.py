import random


class ItemManager:
	def __init__(self):
		self.items = list()

	def register_item(self, item):
		if not hasattr(item, 'owner'):
			raise AttributeError("Item must have 'owner' attribute to be registered")
		if self.items.count(item) > 0:
			raise RuntimeError("Item already present in list")
		self.items.append(item)
		self.assign_owner(item, None)

	def assign_owner(self, item, owner):
		try:
			index = self.items.index(item)
		except ValueError:
			print("Item isn't registered with ItemManager")
		self.items[index].owner = owner

	def get_total_items(self):
		return self.items

	def get_total_count(self):
		return len(get_total_items())

	def get_owned_items(self, owner):
		return [i for i in self.items if i.owner == owner]

	def get_owned_count(self, owner):
		return len(self.get_items(item, owner))

	def shuffle(self):
		random.shuffle(self.items)
