class Item:	
	def __init__(self, data):
		self.item = data

	def __str__(self):
		return self.item

	def __eq__(self, other):
		return self.item == other.item

class Room:
	"""A single room"""

	def __init__(self, data, name):
		self.name = name
		self.description = data['desc']
		self._items = []
		for item in data['items']:
			self._items.append(Item(item))
		self.dirs = {}
		keys_otherthan_dir = ['items', 'desc', 'enemy', 'lock']
		for key in data:
			if key not in keys_otherthan_dir:
				self.dirs[key] = data[key]
		#locked room
		self.locks = {}
		if 'lock' in data:
			for key,value in data['lock'].items():
				self.locks[key] = value

		self.enemies = {}
		if 'enemy' in data:
			for key,value in data['enemy'].items():
				self.enemies[key] = value

	def isLocked(self, item):
		print(item + " lock:: " + " ".join(name + " : " + value for name,value in self.locks.items()) + "is " + str(isinstance(item, Room)))
		if item in self.locks:
			return True
		else:
			return False

	def hasEnemy(self, item):
		if item in self.enemies:
			return True
		else:
			return False

	def __str__(self):
		if self.name in self.locks:
			return "The " + self.name + " seems to be inaccessible. You need a " + self.locks[self.name] + " to look around."
		else:
			str_items = [str(item) for item in self._items]
			return self.name + "\n" + self.description + "\nitems: " + ", ".join(str_items) + "\n" + "\n".join([dir+": "+str(room) for dir,room in self.dirs.items()])

class Person:
	"""Character playing the game"""
	
	def __init__(self):
		self._citems = []

	def __str__(self):
		str_items = [str(item) for item in self._citems]
		#if not str_items:
		#	return "You do not have any items."
		#else:
		#	return "You have these items: " + ", ".join(str_items)
		return str_items

class House:
	"""A house contains one or more rooms"""

	def __init__(self, data, current_name):
		self.rooms = {}
		for key,value in data.items():
			self.rooms[key] = Room(data[key], key)
		#self._current = self.rooms[current_name]
		self._current_name = current_name
		self.scared_person = Person()

	def go(self, direction):
		cur_room = self.rooms[self._current_name]
		if direction in cur_room.dirs:
			if not cur_room.isLocked(cur_room.dirs[direction]) and not cur_room.hasEnemy(cur_room):
				self._current_name = cur_room.dirs[direction]
				print(self.current)

			elif cur_room.isLocked(cur_room.dirs[direction]) and (cur_room.locks[cur_room.dirs[direction]] in self.scared_person._citems):
				self._current_name = cur_room.dirs[direction]
				print(self.current)

			elif cur_room.hasEnemy(cur_room):
				print("You need to defeat the enemy before you can continue anywhere")
			
			else:
				print("You need a " + cur_room.locks[cur_room.dirs[direction]] + " to access this direction " + direction) 
			#self._current = self.rooms[self._current_name]
			#print(self._current)
		else:
			print("There is no room in the direction " + direction)

	def pickup(self, item):
		if Item(item) in self.rooms[self._current_name]._items:
			self.scared_person._citems.append(item)
			self.rooms[self._current_name]._items.remove(Item(item))
			print("You picked up a " + item)
		else:
			print("Unable to pickup. " + item + " is not in the " + self._current_name)

	def look(self, object):
		cur = self.rooms[self._current_name]

		if not object:
			print(self.rooms[self._current_name])
		elif object == 'items':
			if not self.scared_person:
				print("You do not have any items")
			else:
				str_person = [str(item) for item in self.scared_person._citems]
				print("You have these items: " + ", ".join(str_person))
		elif cur.isLocked(cur.dirs[object]):
			print("You cannot look in this direction")
		elif object in cur.dirs:
			name_in_dir = self.rooms[self._current_name].dirs[object]
			print(self.rooms[name_in_dir])
		else:
			print("Not a valid look command")

	@property
	def current(self):
		return self.rooms[self._current_name]

	def __str__(self):
		return "World:\n{0}".format("\n%%\n".join([name+": "+str(room) for name,room in self.rooms.items()]))


