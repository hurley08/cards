# practice.py
 
from cards.deck import Deck
from cards.deck import standard_deck
from cards.playing_card import PlayingCard, suits, faces
from cardExceptions import *

from dataclasses import dataclass
import random
import logging

'''
def generate_std_deck(suits, faces):
	std_deck = []
	for i in suits:
		for j in faces:
			tup =f"('{i}', '{j}')"
			std_deck.append(tup)
	return std_deck



def distribute_to_players(decks):


	count = d.count()
	while count >= 1:
		for i in decks:
			d.deal_card(1, i)
		count = d.count()

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
		logging.info("Game object instantiated")
		self.dealer.generate_deck()


	def distribute_cards(self, decks):
		# Alternate dealing a single card until
		# dealer's deck is empty

		count = self.dealer.count()
		while count > 0:
			for i in decks:
				self.dealer.deal_card(1, i)
			count = self.dealer.count()
		logging.debug(f"{self.p1.count()=}, {self.p2.count()=}")



	def begin(self):
		# Loops until one of the players have 0 cards

		self.gameover = False
		self.winner = False
		self.turn = 0
		logging.info("The game has begun")

		while (self.p1.count() > 0 and self.p2.count() > 0):
			for playr in self.players:
				temp = playr.just_draw(1)
				playr.hand = temp[0]
			logging.debug(f"{self.p1.hand=} vs {self.p2.hand=}")
			if self.p1.hand > self.p2.hand:
				self.p1.add_card(self.p2.hand)
				self.p2.remove_card(self.p2.hand)
			else:
				self.p2.add_card(self.p1.hand)
				self.p1.remove_card(self.p1.hand)
			
			self.turn += 1 

			self.update_counts()
		self.gameover = True
		self.winner = self.p1 if self.p1_cards > self.p2_cards else self.p2
		logging.info(f"{self.winner=}, {self.turn}")
		print("\nwinner: ", self.winner.name, "\nturn: ", self.turn)
		print(f"")


	def update_counts(self):
		# Update the count attribute for each player deck

		logging.debug("Updating cards of he deck")

		self.p1_cards = self.p1.count()
		self.p2_cards = self.p2.count()





game = Game()
game.distribute_cards([game.p1, game.p2])
game.begin()
