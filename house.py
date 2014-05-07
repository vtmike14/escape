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
			if key != 'items' and key != 'desc' and key != 'enemy':
				self.dirs[key] = data[key];
		#print(self._items)

	def __str__(self):
		str_items = [str(item) for item in self._items]
		return self.description + "\nitems: " + ", ".join(str_items)

class Person:
	"""Character playing the game"""
	
	def __init__(self):
		self._citems = []

	def __str__(self):
		str_items = [str(item) for item in self._citems]
		if not str_items:
			return "You do not have any items."
		else:
			return "You have these items: " + ", ".join(str_items)

class House:
	"""A house contains one or more rooms"""

	def __init__(self, data, current_name):
		self.rooms = {}
		for key,value in data.items():
			self.rooms[key] = Room(data[key])
		self._current = self.rooms[current_name]
		self._current_name = current_name
		self.scared_person = Person()

	def go(self, direction):
		if direction in self.rooms[self._current_name].dirs:
			self._current_name = self.rooms[self._current_name].dirs[direction]
			self._current = self.rooms[self._current_name]
			print(self._current)
		else:
			print("There is no room in the direction " + direction)

	def pickup(self, item):
		print(str(self.rooms[self._current_name]._items))
		if item in self.rooms[self._current_name]._items:
			self.scared_person._items.append(item)
			self.rooms[self._curent_name]._items.remove(item)
		else:
			print("Unable to pickup. " + item + " is not in the " + self._current_name)

	def look(self, object):
		if not object:
			print(self._current_name)
			print(self.rooms[self._current_name])
		#elif direction
		elif object == 'items':
			print(self.scared_person)
		else:
			print("Not a valid look command")

	@property
	def current(self):
		return self._current

	def __str__(self):
		return "World:\n{0}".format("\n%%\n".join([name+": "+str(room) for name,room in self.rooms.items()]))


