#!/usr/bin/env python3

import house
import yaml
import sys

# Read in graphics and print map
f = open('intro.txt', 'r')
title = f.read()
f.close()
print(title)
f = open('house_map.txt', 'r')
map = f.read()
f.close()
print(map)
print("                       TYPE 'start' TO BEGIN...")
line = input("  >>")
while line != 'start':
	print("Invalid input: please type 'start' to begin...")
	line = input("  >>")

# Print directions
intro = "\n\nWelcome to the game ESCAPE! where you are stuck\nin a house until you can figure out what to do to get out.\n\nIn order to get out, you must collect the proper items\nas well as find the correct rooms to go through to get to your freedom,\nand if you don't make it through, well, it just sucks to suck.\n\nThe commands for the game are:\ngo [direction]\nlook\nlook items\nlook [direction]\npickup [item]\n\nFor those of you with weak constitutions and can't make it through\nthe game, well, you can type ""exit"" in order to get out of the game.\n\nGood Luck...\n\n"

print(intro)

# Load data
data = yaml.load(open('house.yaml', 'r'))

myhouse = house.House(data, "LOBBY")

print(myhouse.rooms["LOBBY"])

# Play game
while True:
	# Define end var so that a NameError is not received if an invalid command is giver first time through while loop
	end = ''
	line = input("  >>")
	if line == 'exit':
		break	
	action, argument = line.partition(' ')[::2]
	try:
		end = getattr(myhouse, action)(argument)
	except AttributeError:
		print("{0} is an invalid command...".format(action))	
	if end == 'endgame':
		break
