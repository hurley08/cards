# cards/practice.py
 
from cards.deck import Deck
from cards.playing_card import PlayingCard, suits, faces
from loguru import logger
from dataclasses import dataclass
from cardExceptions import *

import random
import sys
import time


logger = logging.getLogger(__name__)
logging.basicConfig(filename="cards.log", filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
stdout = logging.StreamHandler(stream=sys.stdout)



'''
def generate_std_deck(suits, faces):
	std_deck = []
	for i in suits:
		for j in faces:
			tup =f"('{i}', '{j}')"
			std_deck.append(tup)
<<<<<<< HEAD
=======
			logging.debug(tup,',')
>>>>>>> main
	return std_deck



<<<<<<< HEAD
def distribute_to_players(decks):


	count = d.count()
=======
def seq():
	d = Deck(name="Ron")
	d.generate_deck
	d2 = Deck(name="Player2")
	tw = d.just_draw(3)
	for i in tw:
		d.remove_card(i)


d = Deck(name="Dealer")
d.generate_deck()
#print(d.deck)
#print(d.binned())
#
# print(d.count)
#L = d.binned(["Hearts"])
#for i in L:
#	print(i)
	#print(L[i], '\n')


d1 = Deck(name="Player1")
d2 = Deck(name="Player2")
#d.deal_card(d.count()/2,d1)
#d.deal_card(d.count(), d2)
d1.count
d2.count



def distribute_to_players(decks):
	count = d.count
>>>>>>> main
	while count >= 1:
		for i in decks:
			d.deal(1, i)
		count = d.count

'''

class Game:
	# Class to manage objects and rules 

	def __init__(self, Player1=None, Player2=None, Dealer=None):
		# Initilize game objects (mostly decks)

		self.dealer = Deck(name="Dealer")
		self.dealer.generate_deck()
		self.gameover = None
		self.winner = None
		self.p1 = Deck(name="Player1")
		self.p2 = Deck(name="Player2")
		self.p1.hand = None
		self.p2.hand = None
		self.p1_cards = self.p1.count()
		self.p2_cards = self.p2.count()
		self.players = [self.p1, self.p2]
		logger.success("Game object instantiated")
		self.dealer.generate_deck()

	def info(self, slp=5):
		# Just to explain the rules of the game
		message=((
		"This game is called War."
		" It begins with 2 players receiving half of the dealers deck"
		" and ends when one of the players have no cards left to play."
		" A card is drawn every round by each player. The player whose"
		" card has the higher value gets to keep and shuffle both cards"
		" into their deck"
	))
		logger.debug(f"Displaying game info {message} for {slp} seconds")
		print(f"\n{message:}")
		time.sleep(slp)

	def distribute_cards(self, decks):
		# Alternate dealing a single card until
		# dealer's deck is empty

		count = self.dealer.count()
		while count > 0:
			for i in decks:
				self.dealer.deal_card(1, i)
			count = self.dealer.count()
		logger.debug(f"{self.p1.count()=}, {self.p2.count()=}")


	def begin(self):
		# Loops until one of the players have 0 cards

		self.gameover = False
		self.winner = False
		self.turn = 0
		logger.info("The game has begun")

		while (self.p1.count() > 0 and self.p2.count() > 0):
			time.sleep(.005)
			for playr in self.players:
				temp = playr.just_draw(1)
				playr.hand = temp[0]
			logger.debug(f"turn: {self.turn}, {self.p1.hand._face} of {self.p1.hand._suit}s ({self.p1.hand._id}) vs , {self.p2.hand._face} of {self.p2.hand._suit}s ({self.p2.hand._id})")
			if self.p1.hand > self.p2.hand:
				logger.info(f"{self.p1.hand._face} of {self.p1.hand._suit}s  is greater")
				self.p1.add_card(self.p2.hand)
				self.p2.remove_card(self.p2.hand)
			else:
				logger.info(f"{self.p2.hand._face} of {self.p2.hand._suit}s is greater")
				self.p2.add_card(self.p1.hand)
				self.p1.remove_card(self.p1.hand)
			
			self.turn += 1 

			self.update_counts()
		self.gameover = True
		self.winner = self.p1 if self.p1_cards > self.p2_cards else self.p2
		logger.success(f"{self.winner.name=} won in {self.turn} turns")
		print(f"\nwinner: ", self.winner.name, "\nturn: ", self.turn)


	def update_counts(self):
		# Update the count attribute for each player deck
		pre1 = self.p1_cards
		pre2 = self.p2_cards
		self.p1_cards = self.p1.count()
		self.p2_cards = self.p2.count()
		logger.debug(f"Counts updated | \t p1: {pre1} >> {self.p1_cards}, p2: {pre2} >> {self.p2_cards}")


if __name__ == "__main__": 

	logger.remove()
	logger.add(sys.stderr, colorize=True, format="{time:MM-DD-YYYY HH:mm:X} [{level}] {message}", diagnose=False)
	logger.add("{time:YYYY-MM-DD}.log", diagnose=False)
	logger.success("Successfully changed format")
	logger.level("DEBUG", color="<blue>")
	logger.level("INFO", color="<white>")
	logger.level("SUCCESS", color="<green>")
	logger.level("ERROR", color="<red>")
	logger.level("CRITICAL", color="<magenta")
	game = Game()
	game.info()
	game.distribute_cards([game.p1, game.p2])
	game.begin()

