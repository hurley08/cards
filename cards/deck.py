#cards/deck.py

from dataclasses import dataclass 
from cards.playing_card import PlayingCard
from cards.tables import Tables
from cards.cardExceptions import *
import random
import copy
import logging

logger = logging.getLogger(__name__)

tables = Tables()
standard_deck = list(tables.rankings_single_level_dict.keys())

class Deck:
	def __init__(self, name='default_name'):
		self.deck = {}
		self.name = name
		self.count = 0 
		logger.info("Deck class instantiated")


	def generate_deck(self):
		# Creates a regular set of cards with 2-A of every suit
		# This must be blocked if Deck becomes a parent class that players can inherit 
		'''
		this_deck = {}
		for i in suits:
			for j in faces:
				card = PlayingCard(i,j)
				this_deck.update({card.id:card})
		self.deck = {}
		for i in this_deck:
			self.deck[(this_deck[i].suit, this_deck[i].face)] = this_deck[i].id
		'''
		this_deck = []
		randomized_index = random.sample(range(1,len(standard_deck)+1),len(standard_deck))
		logger.debug("Temporary deck created")
		for index in range(len(list(standard_deck))):
			i = standard_deck[index]
			cId = randomized_index[index]
			crd = PlayingCard(i[0],i[1])
			self.add_card(crd_id=cId, playing_card=crd)	
		logger.info("Deck has been generated")
		logger.debug(self.deck)	
		

	def just_draw(self, num_cards):
		# Draw a specified number of cards from deck

		drawn = random.sample(sorted(self.deck), num_cards)
		logger.debug(drawn)
		card_list = []
		for i in drawn:
			card_list.append(self.deck[i])
		return card_list
		logger.debug(card_list)
			

	def add_card(self, crd_id=None, playing_card=None):
		# Utility to add card to either hand or into deck 
		# Adds to deck first by default

		if (playing_card and crd_id) is not None:
			if isinstance(playing_card, PlayingCard) == True:
				try:	
					self.deck[crd_id] = playing_card
					logger.info(f"A card was added to the deck")

				except Exception as e:
					logging.exception(f"Something went wrong here {e=} ")
				finally:
					if crd_id in self.deck:
						logger.debug(f"{playing_card} verified to be in the deck self.count + 1")
						self.count += 1 
						return True
					else:
						return False


	def remove_card(self, crd_id):
		# remove a card from this desk

		try:
			if playing_card is not None and isinstance(playing_card, PlayingCard):
				crd_id
				self.deck.pop(crd_id)
				logging.info(f"{crd_id=} was removed from deck")
				self.count -= 1

		except: 
			logging.exception(DeckException("COULDN'T REMOVE MATE"))

	def add_joker(self, num_joker=0):
		# Allows the addition of Jokers

		for i in range(num_joker):
			self.add_card(len(standard_deck)+i, PlayingCard("Joker", i))



	def dealer_peek_deck(self):
		# Allows a player to view the whole of the deck
		# Intended for very special decks (like Dealers)
		print(self.deck)


	def binned(self, suitsReturn):
		# Bins cards for analysis. Should typically be disabled
	
		self.count()
		bins = {
			"Club": {},
			"Diamond": {},
			"Heart": {},
			"Spade": {},
		}
		print("this was broken by introduction of face up concept")
		'''
		for card in self.deck:
			crd = self.deck[card]
			bins[crd._suit][crd._face] = crd
		return bins
		'''


	def deal_card(self, numCards=0, receiving_deck=None):
		if numCards < 1:
			logging.exception(CountException("Number of cards to distribute is required. "))
		if receiving_deck is None:
			logging.exception(DeckException("A 'destination' deck was not specified"))
		if isinstance(receiving_deck, Deck) is False:
			logging.exception(DeckException("Something was wrong with the destination deck provided"))
		backup_deck = copy.deepcopy(self.deck)
		backup_rec_deck = copy.deepcopy(receiving_deck.deck)

		try: 
			drawn = self.just_draw(numCards)
			for i in drawn:
				receiving_deck.add_card(i)
				self.remove_card(i)
		except:	
			self.deck = backup_deck
			receiving_deck.deck = backup_rec_deck
			logging.exception(DeckException("Something went wrong womp womp"))




