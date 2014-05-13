# Holds items in a room. A person also has a list of items
class Item:	
	def __init__(self, data):
		self.item = data

	def __str__(self):
		return self.item

	def __eq__(self, other):
		return self.item == other.item

# Defines a room of a house
class Room:
	"""A single room"""

	# Initializer. Creates vars: var with name, var with description, list with items, dict with directions,
	# dict with lockes rooms and their unlocking item, and dict with enemy and item to defeat it
	def __init__(self, data, name):
		self.name = name
		self.description = data['desc']
		self._items = []
		for item in data['items']:
			self._items.append(Item(item))
		# Create dict of dirs with all key valyes that are not in otherthan_dir
		self.dirs = {}
		keys_otherthan_dir = ['items', 'desc', 'enemy', 'lock']
		for key in data:
			if key not in keys_otherthan_dir:
				self.dirs[key] = data[key]
		# Locked room
		self.locks = {}
		if 'lock' in data:
			for key,value in data['lock'].items():
				self.locks[key] = value
		# Enemy, if exists
		self.enemies = {}
		if 'enemy' in data:
			for key,value in data['enemy'].items():
				self.enemies[key] = value

	# Checks to see if there is a lock on the item, Anything can be locked but this is usually a direction
	# Parameter
	#	item	checks if item has a lock
	def isLocked(self, item):
		if item in self.locks:
			return True
		else:
			return False

	# Returns true if this room has an enemy and false if not
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

# Defines a person in a house. This is the user
class Person:
	"""Character playing the game"""
	
	def __init__(self):
		self._citems = []

	def __str__(self):
		str_items = [str(item) for item in self._citems]
		if not str_items:
			return "You do not have any items."
		else:
			return "You have these item(s): " + ", ".join(str_items)
		return str_items

# Defines a house with rooms and a person
class House:
	"""A house contains one or more rooms and a person"""

	# Initializer. Creates a dict of rooms, var with current room name, and person within the house
	def __init__(self, data, current_name):
		self.rooms = {}
		for key,value in data.items():
			self.rooms[key] = Room(data[key], key)
		self._current_name = current_name
		self.scared_person = Person()

	# Defines the movement of the person throughout the house
	# Parameter:
	#	direction	the direction to move. If there is no room in that direction, a statement is printed out
	def go(self, direction):
		cur_room = self.rooms[self._current_name]
		if direction in cur_room.dirs:
			# Room is locked and there is no enemy
			if not cur_room.isLocked(cur_room.dirs[direction]) and not cur_room.hasEnemy(cur_room.dirs[direction]):
				self._current_name = cur_room.dirs[direction]
				print(self.current)
			# Room is locked but person has item
			elif cur_room.isLocked(cur_room.dirs[direction]) and (cur_room.locks[cur_room.dirs[direction]] in self.scared_person._citems):
				self._current_name = cur_room.dirs[direction]
				print(self.current)
			# Room has an enemey and person has item to aly enemy
			elif cur_room.hasEnemy(cur_room.dirs[direction]) and (cur_room.enemies[cur_room.dirs[direction]] in self.scared_person._citems):
				print("Congratulations!!! You have slain the nasty rat with the machette and escaped the scary house!")
				print("Please stay tuned for more updates from the amazing escape game development team presented to you by:")
				print("Neil Singh, Caleb Stroud, Michael Burton, and Timothy Hogarty")
				return "endgame"			
			# Room has enemy but person does not have required item
			elif cur_room.hasEnemy(cur_room.dirs[direction]):
				print("You need to defeat the enemy before you can go outside.")
				print("You will need a blade of some kind to defeat the monster.")
			# Room is locked
			else:
				print("You need a " + cur_room.locks[cur_room.dirs[direction]] + " to access this direction " + direction + ".") 
		else:
			print("There is no room in the direction " + direction + ".")

	# Command to pickup and item in a room. If the item is not in hte room, prints out a message
	# Parameter
	#	item	item to be picked up
	def pickup(self, item):
		if Item(item) in self.rooms[self._current_name]._items:
			self.scared_person._citems.append(item)
			self.rooms[self._current_name]._items.remove(Item(item))
			print("You picked up a " + item + ".")
		else:
			print("Unable to pickup. " + item + " is not in the " + self._current_name + ".")

	# Command to look at certain things. There are three forms:
	#	look			descrip of current room
	#	look items		list of person's items
	#	look [direction]	descript of room in dir
	# Paremeter
	#	object	ojbect to be parsed
	def look(self, object):
		cur = self.rooms[self._current_name]

		if not object:
			print(self.rooms[self._current_name])
		elif object == 'items':
			print(self.scared_person)
		elif object not in cur.dirs:
			print("There is not a room in the chosen direction.") 
		elif cur.isLocked(cur.dirs[object]):
			if self.canAccess(object):
				print(self.rooms[self.rooms[self._current_name].dirs[object]])
			else:
				print("You cannot look in this direction.")
		elif object in cur.dirs:
			name_in_dir = self.rooms[self._current_name].dirs[object]
			print(self.rooms[name_in_dir])
		else:
			print("Not a valid look command.")

	# Returns true if there is a lock and the person has the item
	def canAccess(self, direction):
		cur_room = self.rooms[self._current_name]
		return (cur_room.isLocked(cur_room.dirs[direction]) and (cur_room.locks[cur_room.dirs[direction]] in self.scared_person._citems))
		

	@property
	def current(self):
		return self.rooms[self._current_name]

	def __str__(self):
		return "World:\n{0}".format("\n%%\n".join([name+": "+str(room) for name,room in self.rooms.items()]))
