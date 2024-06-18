#cards/game_war.py

from cards.deck import Deck
from loguru import logger

import time

class War:
	# Class to manage objects and rules 

	def __init__(self, Player1=None, Player2=None, Dealer=None):
		# Initilize game objects (mostly decks)

		self.dealer = Deck(name=Dealer)
		self.gameover = None
		self.winner = None
		self.p1 = Deck(name=Player1)
		self.p2 = Deck(name=Player2)
		self.p1.hand = None
		self.p2.hand = None
		self.p1_cards = self.p1.count()
		self.p2_cards = self.p2.count()
		self.players = [self.p1, self.p2]
		logger.success("Game object instantiated")
		self.dealer.generate_deck()

		

	def info(self, message=None, slp=5):
		# Just to explain the rules of the game

		if message is None:
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
				self.dealer.deal(1, i)
			count = self.dealer.count()
		logger.debug(f"{self.p1.count()=}, {self.p2.count()=}")


	def begin(self, rounds=1):
		# Loops until one of the players have 0 cards

		self.gameover = False
		self.winner = False
		self.turn = 0
		self.rounds = rounds
		logger.info("The game has begun")

		while (self.p1.count() > 0 and self.p2.count() > 0):
			time.sleep(.005)
			for playr in self.players:
				temp = playr.just_draw(1)
				playr.hand = (temp, playr.deck[temp])
			logger.debug(f"turn: {self.turn}, {self.p1.hand[1]._face} of {self.p1.hand[1]._suit}s ({self.p1.hand[1]._id}) vs , {self.p2.hand[1]._face} of {self.p2.hand[1]._suit}s ({self.p2.hand[1]._id})")
			if self.p1.hand[1] > self.p2.hand[1]:
				logger.info(f"{self.p1.hand[1]._face} of {self.p1.hand[1]._suit}s  is greater")
				self.p1.add_card(self.p2.hand[0], self.p2.hand[1])
				self.p2.remove_card(self.p2.hand[0])
			else:
				logger.info(f"{self.p2.hand[1]._face} of {self.p2.hand[1]._suit}s is greater")
				self.p2.add_card(self.p1.hand[0], self.p1.hand[1])
				self.p1.remove_card(self.p1.hand[0])
			
			self.turn += 1 

			self.update_counts()
		self.gameover = True
		self.winner = self.p1 if self.p1_cards > self.p2_cards else self.p2
		logger.success(f"{self.winner.name=} won in {self.turn} turns")
		print("\nwinner: ", self.winner.name, "\nturn: ", self.turn)


	def update_counts(self):
		# Update the count attribute for each player deck
		pre1 = self.p1_cards
		pre2 = self.p2_cards
		self.p1_cards = self.p1.count()
		self.p2_cards = self.p2.count()
		logger.debug(f"Counts updated | \t p1: {pre1} >> {self.p1_cards}, p2: {pre2} >> {self.p2_cards}")