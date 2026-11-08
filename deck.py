import random

# Deck
deckDictStd = {
	"Bomb":0,
	"TimeBomb":0,
	"Defuse":0,
	"Black Hole":0,
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
	"Dumpster":3,
	"Blind":1,
	"Color Blind":1,         # Blind then shuffle, can still play
	"Feed the deads":1,      # Everyone give a card for each deads
	"Grave rob":1,           # Rob max 2 cards from a dead player
}

deckDictEx = {
	"Kamikaze":1,        # For each pairs of card you discard, destroy one of opponent's card
	"Aircraft carrier":1,# ...
	"Embago":1,          # Choose a player that can't draw or given card(s) by anyone (except steal)
	"Deadman's hand":1,  # Move bomb on top and force next player to draw the first card
	"Lend Lease Aids":1, # Send another player one card in you deck, they can refuse 
	"Blitzkrieg":1,      # Redirect turn to this player
	"God's rod":1,       # Destroy three card from draw deck
	"Communism":2,       # Two player exchange cards to be equal, opponent have >= you
}

deckStd = []

class Deck(object):
	"""
	An object represent a deck (list)

	Deck(cards=deckStd, name:str)

	deckFrom -> a new deck object from one
	drawFrom -> draw some cards from deck
	deckAddBombs -> Add std bomb
	addCards -> Add cards to deck
	check -> Print info about this deck
		- Deck name
		- Total cards
		- Five last card
	"""
	def __init__(self, cards=deckStd, name="drawDeck") -> None:
		"""
		Deck(cards, name) -> None
		"""
		self.deck = []
		self.name = name
		for cardDeck in cards:
			self.addCards(cardDeck, shuffle=True)

	def deckFrom(self, num=5) -> Deck:
		"""
		deckFrom(num) -> Deck
			- Return a deck from another deck
		"""
		print("deckFrom",self.deck)
		return Deck(self.drawFrom(n = num))

	def drawFrom(self, n=1, bottom=False) -> list:
		"""
		drawFrom(n, bottom) -> list
			- Return a list of cards
			- self.deck auto draw
		"""
		deck = []
		for _ in range(min(n,len(self.deck))):
			deck.append(self.deck.pop(0))
		return deck

	def addCards(self,deck,shuffle=False) -> None:
		"""
		addCards(deck,shuffle) -> None
			- Add card from a deck to self.deck
		"""
		for key in deck.keys():
			self.deck += [key]*deck[key]
		if shuffle: random.shuffle(self.deck)

	def deckAddBombs(self, norm=6, time=2, hole=1) -> None:
		"""
		deckAddBombs(norm, time, hole) -> None
		"""
		deckBombs = {
			"Bomb":norm,
			"Time":time,
			"Black Hole":hole
		}
		addCards(deckBombs, shuffle=True)

	def check(self, cardCheck=5) -> None:
		"""
		check(cardCheck) -> None
			- Name
			- Len deck
			- Upper cards
		"""
		print("<", self.name, len(self.deck), ">")
		for index, card in enumerate(self.deck[:cardCheck]):
			print(index + 1, ">", card)