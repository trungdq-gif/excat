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
		

player = []

def gameInit(bomb = 10, ww2=1, coldwar=1, addDefuse=3):
	""""""
	# Card set up
	addDeck = {}
	if ww2: addDeck |= {"Kamikaze":2, "Lend Lease Aids":2, "Aircraft carrier":1, "Blitzkrieg":2}
	if coldwar: addDeck |= {"Embago":2, "Deadman's hand":1, "Weapon races":1}
	if addDefuse: addDeck |= {"Defuse":addDefuse}
	drawDeck = Deck((deckDictStd, addDeck))

	# Player setup
	player = [Player(host=True,deck=drawDeck.drawFrom(5))]
	for i in range(1,5):
		player.append(Player(deck=drawDeck.drawFrom(5), name=f"Guest No.{i}"))
	drawDeck.check()

	player[0].deck += drawDeck.drawFrom()
	print(player[0].deck)
	drawDeck.check()


def excatcli():
	os.system("cls")	
	with term.hidden_cursor(), term.fullscreen(), term.cbreak():
		while running: # Should be placed inside term context
			print(term.home)
			for i in greet.split("\n"):
				cprint(i+ term.clear_eol, (255,65,0))
			key = term.inkey(timeout=0.01)

if __name__ == "__main__":
	# excatcli()
	gameInit()