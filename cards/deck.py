#cards/deck.py

from cards.playing_card import PlayingCard
from cards.tables import Tables
from loguru import logger
from cards.cardExceptions import DeckException, CountException
import random
import copy



tables = Tables()
standard_deck = list(tables.rankings_single_level_dict.keys())



class Deck:
	def __init__(self, name='default_name'):
		self.deck = {}
		self.name = name
		self.numCards = 0
		self.hand = {}
		self.graveyard = {}
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
		logger.debug("Generating Deck")
		randomized_index = random.sample(range(self.numCards+1,self.numCards+1+len(standard_deck)+1),len(standard_deck))
		for index in range(len(standard_deck)):
			i = standard_deck[index]					# Adds cards sequentially
			cId = randomized_index[index]				# Assigning a random id between 0 and size of deck
			crd = PlayingCard(i[0],i[1])				# Creates the PlayingCard object								
			self.add_card(crd_id=cId, playing_card=crd)	# Adds to the self deck and uses random id as the key											
		logger.info("Deck has been generated")		 	# This is to obfuscate the value of the card
		logger.debug(self.deck)	


	def just_draw(self, num_cards):
		# Draw a specified number of cards from deck
		drawn = []
		for i in range(num_cards):
			choice = random.choice(list(self.deck.keys()))
			drawn.append(choice)
		if len(drawn) == 1:
			drawn = drawn[0]
		return drawn
		
	def count(self):
		# How many cards are in a deck
		return len(self.deck)
			

	def add_card(self, crd_id=None, playing_card=None):
		# Utility to add card to either hand or into deck 
		# Adds to deck first by default

		if (playing_card and crd_id) is not None:
			if isinstance(playing_card, PlayingCard) is True:
				try:	
					self.deck[crd_id] = playing_card
					logger.info("A card was added to the deck")

				except Exception as e:
					logger.exception(f"Something went wrong here {e=} ")
				finally:
					if crd_id in self.deck:
						logger.debug(f"{playing_card} verified to be in the target deck, self.count + 1")
						self.numCards += 1
						assert len(self.deck) == self.count()
						return True
					else:
						return False


	def remove_card(self, crd_id):
		# remove a card from this desk

		try:
			if crd_id is not None:
				obj = self.deck[crd_id]
				self.graveyard[crd_id] = obj
				self.deck.pop(crd_id)
				self.numCards -= 1
				logger.debug(f"{obj._suit=}, {obj._face=}")
				logger.success(f"{crd_id=} was removed from deck")
				return obj

		except DeckException: 
			logger.exception(DeckException("COULDN'T REMOVE MATE"))
			return False

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
	
		self.count
		print("this was broken by introduction of face up concept")
		'''
		for card in self.deck:
			crd = self.deck[card]
			bins[crd._suit][crd._face] = crd
		return bins
		'''


	def deal(self, numCards=0, receiving_deck=None):
		if numCards < 1:
			logger.exception(CountException("Number of cards to distribute is required. "))
		if receiving_deck is None:
			logger.exception(DeckException("A 'destination' deck was not specified"))
		if isinstance(receiving_deck, Deck) is False:
			logger.exception(DeckException("Something was wrong with the destination deck provided"))
		backup_deck = copy.deepcopy(self.deck)
		backup_rec_deck = copy.deepcopy(receiving_deck.deck)
		for i in range(numCards):

			try: 
				choice = random.choice(list(self.deck))
				card = self.remove_card(choice)
				receiving_deck.add_card(choice, card)
				
			except DeckException:	
				self.deck = backup_deck
				receiving_deck.deck = backup_rec_deck
				logger.exception(DeckException("Something went wrong womp womp"))




