from pyfiglet import figlet_format
from blessed import Terminal
from termcolor import cprint
import atexit
import random
import time
import sys
import os

from playerc import Player, PlayerErr, checkPlayerExist
from deck import Deck, deckDictStd

os.chdir(os.path.dirname(os.path.abspath(__file__)))
startTime = time.time()
restart = 0
greet = figlet_format("Exploding Kitten") # Cli header
term = Terminal()						  # Create terminal
running = 1 							  # Init running
players = {}
drawDeck = object

def gameEnd():
	cprint(f"{time.time()-startTime:.2f}")

	if restart:
		print(os.getcwd())
		os.system(f"python {"excat.py"}")
		# os.execv(sys.argv[0], [sys.executable] + sys.argv) # Self-restart
atexit.register(gameEnd)

def gameInit(bomb = 10, ww2=1, coldwar=1, addDefuse=3):
	""""""
	# Card set up
	addDeck = {}
	if ww2: addDeck |= {"Kamikaze":2, "Lend Lease Aids":2, "Aircraft carrier":1, "Blitzkrieg":2}
	if coldwar: addDeck |= {"Embago":2, "Deadman's hand":1, "Weapon races":1}
	if addDefuse: addDeck |= {"Defuse":addDefuse}

	# Add to deck
	global drawDeck
	drawDeck = Deck((deckDictStd, addDeck))

	# Player setup
	global players
	players["Host"] = Player(host=True,deck=drawDeck.drawFrom(5))
	for i in range(1,5):
		playerName=f"No.{i}"
		players[playerName] = Player(deck=drawDeck.drawFrom(5), name=playerName)
	drawDeck.check()

def excatcli():
	os.system("cls")	
	gameInit()
	userInput = ""
	queue:list[str] = [""]*10
	historyIndex = 0 # History for console
	cursor = ""
	cursorBlink = 0

	# Loop terminal, hide cursor, full screen, have key
	with term.hidden_cursor(), term.fullscreen(), term.cbreak():
		while running: # Should be placed inside term context
			# Header
			print(term.home)
			for line in greet.split("\n"):
				cprint(line + term.clear_eol, (255,65,0))

			# Deck
			print(drawDeck.check(prt=False))

			# Player index
			for index, player in enumerate(players.keys()):
				cprint(f"{index}.{player}:{players[player].deck}{term.clear_eol}", (255,0,0))

			# Console control
			try:
				key = term.inkey(timeout=0.01)
				if key:
					if key.name == "KEY_ESCAPE":
						break
					elif key.name == "KEY_BACKSPACE":
						userInput = userInput[:-1]
					elif key.name == "KEY_UP":
						historyIndex = min(10,historyIndex+1)
						userInput = queue[-historyIndex]
					elif key.name == "KEY_DOWN":
						historyIndex = max(0,historyIndex-1)
						userInput = queue[-historyIndex]
					elif key.name == "KEY_ENTER":
						queue.append(userInput)
						args = userInput.split()
						if userInput == "exit":
							exit()
						if userInput == "re": # Auto restart code
							global restart
							restart = True
							exit()
						elif args[0] == "draw":
							# Draw card or discard
							if len(args) == 1: # Discard
								queue.append(f"Discard: {str(drawDeck.drawFrom(1))}")
							else:
								checkPlayerExist(players, args[1])
								players[args[1]].draw(drawDeck.drawFrom())
						elif args[0] == "check":
							# Check draw deck
							if len(args) == 1:
								queue.append(drawDeck.check(prt=0))
							else:
								checkPlayerExist(players, args[1])
								queue.append(str(players[args[1]].deck.copy())) # Copy so it don't update every check
						userInput = ""
					elif not key.is_sequence: # Valid chr
						userInput += key
			except Exception as Err:
				userInput = ""
				queue.append(f"Err: {Err}")

			# Cursor
			if time.time() - cursorBlink > 0.5:
				cursor = "|" if cursor == "" else ""
				cursorBlink = time.time()

			# Print console out + History
			for history in queue[-10:]:
				cprint("> " + history + term.clear_eol, (128,128,128))
			cprint(f">>> {userInput+cursor if len(userInput) else f"{cursor}{" "*abs(len(cursor)-1)}Type some thing..."}" + term.clear_eol, (255,255,255) if len(userInput) else (128,128,128))


if __name__ == "__main__":
	excatcli()
	gameInit()