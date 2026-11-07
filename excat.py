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
	"Alter x3":3,
	"Alter x5":2,
	"Feral":3,
	"Draw from bottom":3,
	"Draw from any":3,
	"Splits":2,
	"Peek":2,
	"Barking":2,
	"Atomic":1,
	"I'll take that":2,
	"You will take that":2,
	"Create the future":1,
	"Mark":3,
	"Share":2,
	"Sip":1,
	"Swap":3,
	"Copy":2,
	"Garbage":3,
	"Blind":1,
	"Feed the dead":1,
	"Grave rob":1,
}

deckDictEx = {
	"Deadman's hand":1,
	"Kamikaze":1,
	"Aircraft carrier":1,
	"Embago":1,
	"Deadman's hand":1,
	"Lend Lease Aids":1,
	"Blitzkrieg":1,
	"God's rod":1,
}

deckStd = []

class Deck(object):
	"""
	An object represent a deck (list)

	Deck(cards)

	"""
	def __init__(self, cards=deckStd, name="drawDeck"):
		super(Deck, self).__init__()
		self.deck = []
		self.name = name
		for cardDeck in cards:
			self.addCard(cardDeck, shuffle=True)

	def deckFrom(self):
		print("deckFrom",self.deck)
		return Deck(self.drawfrom(n = 5))

	def drawfrom(self, n=1, bottom=False):
		deck = []
		for _ in range(min(n,len(self.deck))):
			deck.append(self.deck.pop(0))
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

	def check(self):
		print("<", self.name, len(self.deck), ">")
		for index, card in enumerate(self.deck[:5]):
			print(index + 1, ">", card)
		

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
	player = [Player(host=True,deck=drawDeck.drawfrom(5))]
	for i in range(1,5):
		player.append(Player(deck=drawDeck.drawfrom(5), name=f"Guest No.{i}"))
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