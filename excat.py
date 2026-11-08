from pyfiglet import figlet_format
from blessed import Terminal
from termcolor import cprint

import random
import os

from deck import Deck, deckDictStd

greet = figlet_format("Exploding kitten") # Cli header
term = Terminal()						  # Create terminal
running = 1 							  # Init running
		

class Player(object):
	"""docstring for Player"""
	def __init__(self, host=False, deck=object, name="Host"):
		self.host = host
		self.deck = ["Defuse"] + deck
		self.name = name
		print(self.name, self.deck)
		

players = {}
drawDeck = object

def gameInit(bomb = 10, ww2=1, coldwar=1, addDefuse=3):
	""""""
	# Card set up
	addDeck = {}
	if ww2: addDeck |= {"Kamikaze":2, "Lend Lease Aids":2, "Aircraft carrier":1, "Blitzkrieg":2}
	if coldwar: addDeck |= {"Embago":2, "Deadman's hand":1, "Weapon races":1}
	if addDefuse: addDeck |= {"Defuse":addDefuse}
	global drawDeck
	drawDeck = Deck((deckDictStd, addDeck))

	# Player setup
	global players
	players["Host"] = Player(host=True,deck=drawDeck.drawFrom(5))
	for i in range(1,5):
		playerName=f"Guest No.{i}"
		players[playerName] = Player(deck=drawDeck.drawFrom(5), name=playerName)
	drawDeck.check()

	players["Host"].deck += drawDeck.drawFrom()
	print(players["Host"].deck)
	drawDeck.check()


def excatcli():
	os.system("cls")	
	gameInit()
	userInput = ""
	queue = [""]*10
	with term.hidden_cursor(), term.fullscreen(), term.cbreak():
		while running: # Should be placed inside term context
			print(term.home)
			for i in greet.split("\n"):
				cprint(i+ term.clear_eol, (255,65,0))

			# Player index
			for index, player in enumerate(players.keys()):
				cprint(f"{index}.{player}:{players[player].deck}{term.clear_eol}", (255,0,0))

			# Console control
			key = term.inkey(timeout=0.01)
			if key:
				if key.name == "KEY_ESCAPE":
					break
				elif key.name == "KEY_BACKSPACE":
					userInput = userInput[:-1]
				elif key.name == "KEY_ENTER":
					queue.append(userInput)
					args = userInput.split()
					if userInput == "exit":
						exit()
					elif args[0] == "draw":
						players[args[1]].deck += drawDeck.drawFrom()
					elif args[0] == "check":
						queue.append(drawDeck.check(prt=0))
					userInput = ""
				elif not key.is_sequence: # Valid chr
					userInput += key

			# Console out
			for history in queue[-10:]:
				print("> " + history + term.clear_eol)
			cprint(f">>> {userInput if len(userInput) else "Type some thing..."}" + term.clear_eol, (255,255,255) if len(userInput) else (128,128,128))


if __name__ == "__main__":
	excatcli()
	gameInit()