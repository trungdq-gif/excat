class Player(object):
	"""docstring for Player"""
	def __init__(self, host=False, deck=object, name="host"):
		self.host = host
		self.deck = ["Defuse"] + deck
		self.name = name
		print(self.name, self.deck)

	def draw(self, cards) -> None:
		self.deck += cards

	def push(self, cardIndex, deckPushTo=None) -> str: # Start index from 1
		# Add check total of last cards
		cardPlay = self.deck.pop(max(0,min(cardIndex-1,len(self.deck)-1)))
		if deckPushTo is not None:
			deckPushTo.addCards({cardPlay:1})
		return cardPlay

	def change(self, cardIndex, changeTo=None) -> str: # Start index from 1
		# Add check total of last cards + raise Err if who change to not existed
		cardChange = self.deck.pop(max(0,min(cardIndex-1,len(self.deck)-1)))
		if changeTo is not None:
			changeTo.draw([cardChange])
		return cardChange

class PlayerErr(Exception):
	...

def checkPlayerExist(playerList, name):
	if not name in playerList.keys(): raise PlayerErr(f"Player unknown: {name}")