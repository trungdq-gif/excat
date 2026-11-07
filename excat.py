from pyfiglet import figlet_format
from blessed import Terminal
from termcolor import cprint

import random
import os

term = Terminal()

running = 1
greet = figlet_format("Exploding kitten")

deckDictStd = {
	"Bomb":0,
	"TimeBomb":0,
	"Defuse":0,
	"Attack":5,
	"Targeted Attack":3,
	"Slap":3,
	"Triple Self Slap":2,
	"Double Self Slap":2,
	"Double Slap":2,
	"Tripple Slap":2,
	"Nope":5,
	"Skip":5,
	"Reverse":4,
	"Steal":6,
	"Return":2,
	"Potato":3,
	"Rainbow":3,
	"Taco":3,
	"Human":3,
	"Melon":3,
	"Favor":3,
	"Dummy":1,
	"See the future x3":5,
	"See the future x5":2,
	"Shuffle":3,
	"Anti-shuffle":3,
}

deckDictEx = {
	"Deadman's hand":1,
	"Kamikaze":1,
	"Aircraft carrier":1,
	"Embago":1,
	"Deadman's hand":1,
	"Lend Lease Aids":1,
	"Blitzkrieg":1
}

deckStd = []

class Deck(object):
	"""
	An object represent a deck (list)

	Deck(cards)

	"""
	def __init__(self, cards=deckStd):
		super(Deck, self).__init__()
		self.deck = []
		for cardDeck in cards:
			self.addCard(cardDeck, shuffle=True)
		random.shuffle(self.deck)
		print(self.deck)

	def deckFrom(self):
		deck = self.drawfrom(5)
		return Deck(deck)

	def drawfrom(self, n, bottom=False):
		deck = ["Defuse"]
		for _ in range(n,len(self.deck)):
			deck += [self.deck.pop(0)]
		return deck

	def addCard(self,deck,shuffle=False):
		for key in deck.keys():
			self.deck += [key]*deck[key]
		if shuffle: random.shuffle(self.deck)

	def deckAddBombs(self, norm=6, time=2, nuke=1):
		deckBombs = {
			"Bomb":norm,
			"Time":time,
			"Nuke":nuke
		}
		addCard(deckBombs, shuffle=True)
		




def gameInit(bomb = 10, ww2=1, coldwar=1, addDefuse=3):
	addDeck = {}
	if ww2: addDeck |= {"Kamikaze":2, "Lend Lease Aids":2, "Aircraft carrier":1, "Blitzkrieg":2}
	if coldwar: addDeck |= {"Embago":2, "Deadman's hand":1, "Weapon races":1}
	if addDefuse: addDeck |= {"Defuse":addDefuse}
	drawDeck = Deck((deckDictStd, addDeck))

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