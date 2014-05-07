#!/usr/bin/env python3

import house
import yaml
import sys

intro = "Welcome to the game ESCAPE! where you are stuck\nin a house until you can figure out what to do to get out.\n\nIn order to get out, you must collect the proper items\nas well as find the correct rooms to go through so get to your freedom,\nand if you don't make it through, well, it just sucks to suck.\n\nThe commands for the game are:\ngo [direction]\nlook [direction]\npickup [item]\nfight [enemy]\n\nFor those of you with weak constitutions and can't make it through\nthe game, well, you can type ""exit"" in order to get out of the game.\n\nGood Luck...\n\n"

print(intro)

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
	



