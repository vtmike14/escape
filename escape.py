#!/usr/bin/env python3

import house
import yaml
import sys

data = yaml.load(open('house.yaml', 'r'))

myhouse = house.House(data, "LOBBY")

print(myhouse.rooms["LOBBY"])
#print(myhouse)

while True:
	line = input(">>")
	if line == 'exit':
		break	
	action, argument = line.partition(' ')[::2]
	try:
		getattr(myhouse, action)(argument)
	except AttributeError:
		print("{0} is an invalid command...".format(action))	
	



