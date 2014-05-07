#!/usr/bin/env python3

import world
import yaml
import sys

data = yaml.load(open('rooms.yaml', 'r'))

myworld = world.World(data, "SURGE 104C")

#print(myworld)

while True:
	line = input(">>")
	if line == 'exit':
		break	
	action, argument = line.partition(' ')[::2]
	getattr(myworld, action)(argument)
		
	



