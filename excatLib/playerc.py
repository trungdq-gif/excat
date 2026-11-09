class Player(object):
	"""docstring for Player"""
	def __init__(self, host=False, deck=object, name="Host"):
		self.host = host
		self.deck = ["Defuse"] + deck
		self.name = name
		print(self.name, self.deck)

	def draw(self, cards) -> None:
		self.deck += cards

	def play(self, cardIndex) -> str: # Start index from 1
		return self.deck.pop(max(0,min(cardIndex-1,len(self.deck)-1)))

class PlayerErr(Exception):
	...

def checkPlayerExist(playerList, name):
	if not name in playerList.keys(): raise PlayerErr(f"Player unknown: {name}")