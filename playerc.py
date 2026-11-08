class Player(object):
	"""docstring for Player"""
	def __init__(self, host=False, deck=object, name="Host"):
		self.host = host
		self.deck = ["Defuse"] + deck
		self.name = name
		print(self.name, self.deck)

	def draw(self, cards):
		self.deck += cards

class PlayerErr(Exception):
	...

def checkPlayerExist(playerList, name):
	if not name in playerList.keys(): raise PlayerErr(f"Player unknown: {name}")