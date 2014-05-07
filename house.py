class Item:	
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
		self.dirs = {}
		for key in data:
			if key != 'items' and key != 'desc':
				self.dirs[key] = data[key];

	def __str__(self):
		str_items = [str(item) for item in self._items]
		return self.description + "\nitems: " + ", ".join(str_items)

class NoPath(RuntimeError):
	pass

class Person:
	"""Character playing the game"""
	
	def __init__(self):
		self._citems = []

	def __str__(self):
		str_items = [str(item) for item in self._citems]
		if not str_items:
			return "\nYou do not have any items."
		else:
			return "\nYou have these items: " + ", ".join(str_items)

class House:
	"""A house contains one or more rooms"""

	def __init__(self, data, current_name):
		self.rooms = {}
		for key,value in data.items():
			self.rooms[key] = Room(data[key])
		self._current = self.rooms[current_name]
		self._current_name = current_name

	def go(self, direction):
		if direction in self.rooms[self._current_name].dirs:
			self._current_name = self.rooms[self._current_name].dirs[direction]
			self._current = self.rooms[self._current_name]
			print(self._current)
		else:
			print("There is no room in the direction " + direction)
		#self._current = self.rooms[self._current_name]

	@property
	def current(self):
		return self._current

	def __str__(self):
		return "World:\n{0}".format("\n%%\n".join([name+": "+str(room) for name,room in self.rooms.items()]))


