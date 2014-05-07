#!/usr/bin/env python3

import house
import yaml
import sys

data = yaml.load(open('house.yaml', 'r'))

myhouse = house.House(data, "LOBBY")

#print(myworld)

while True:
	line = input(">>")
	if line == 'exit':
		break	
	action, argument = line.partition(' ')[::2]
	getattr(myhouse, action)(argument)
		
	



