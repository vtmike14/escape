class Item:
	"""A single item"""

	def __init__(self, data):
		self.item = data

	def __str__(self):
		return self.item


class Room:
	"""A single room"""

	def __init__(self, data):
		self.description = data['desc']
		self._items = []
		for item in data['items']:
			self._items.append(Item(item))

	def __str__(self):
		str_items = [str(item) for item in self._items]
		return self.description + "\nitems: " + ", ".join(map(str,self._items))

class House:
	"""A world contains one or more rooms"""

	def __init__(self, data, current_name):
		self.rooms = {}
		for key,value in data.items():
			self.rooms[key] = Room(data[key])
		
		self.current = self.rooms[current_name]

	def __str__(self):
		return "World:\n{0}".format("\n%%\n".join(
			[name+": "+str(room) for name, room in self.rooms.items()]))

