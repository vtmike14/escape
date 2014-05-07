Escape is a text-based adventure game. The objective is to escape from the house. The user tries to navigate through the house and acquire anything needed to ESCAPE!

We are using a modular implementation. This would allow us to create new layouts and entirely new levels for the user to explore. The current level is a house but we could easily change it to be a school, dungeon, hospital, etc.

How To Play:
Use commands and arguments to move around the house and interact. User can move, pickup items, and look around the current room. Some items may be required to access other rooms.  

Input Format:
[command] [argument]

Supported Commands:
go - moves player in direction of argument
pickup - picks up argument if it is in the room
look (without argument) - displays the info for current room

Examples:
go north
pickup machete
look
