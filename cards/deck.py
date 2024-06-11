#cards/deck.py

from dataclasses import dataclass 
from cards.playing_card import PlayingCard
from cards.tables import Tables
from loguru import logger
from cards.cardExceptions import *
import random
import copy


#logger = logger.getLogger(__name__)

standard_deck = list(Tables().rankings_single_level.keys())
rankings = Tables().rankings_single_level

class Deck:
	def __init__(self, name='default_name'):
		self.cards = []
		self.deck = {}
		self.name = name
		self.numCards = 0
		self.hand = {}
		self.graveyard = {}
	
		logger.info("Deck class instantiated")


	def generate_deck(self, face_up=False):
		# Creates a regular set of cards with 2-A of every suit
		# This must be blocked if Deck becomes a parent class that players can inherit 
		temp = []
		for i in standard_deck:
			card = PlayingCard(suit=i[0], face=i[1], face_up=True )
			self.cards.append([card,i[0],i[1]])


		
		this_deck = []
		randomized_index = random.sample(range(self.count()+1,self.count()+1+len(standard_deck)+1),len(standard_deck))
		logger.debug("Temporary deck created")
		for index in range(len(standard_deck)):
			i = standard_deck[index]
			cId = randomized_index[index]
			crd = PlayingCard(i[0],i[1])
			self.add_card(crd_id=cId, playing_card=crd)	
		logger.info("Deck has been generated")
		logger.debug(self.deck)	
		

	def just_draw(self, num_cards):
		# Draw a specified number of cards from deck
		drawn = random.sample(range(1,len(self.deck)+1), num_cards)
		logger.debug(drawn)
		return drawn
	

	def shuffle(self):
		# Some algorithm to rearrange our list of cards
		if self.cards is not None:
			for i in range(len(self.cards)-1, 0, -1):
				r = random.randint(0, i)
				self.cards[r], self.cards[i] = self.cards[i], self.cards[r]
				return True
		return False


	def count(self):
		# Get the number of cards in deck
		return len(self.deck)


	def add_card(self, crd_id=None, playing_card=None):
		# Utility to add a card into the deck  
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
						self.numCards += 1
						assert len(self.deck) == self.count()
						return True
					else:
						return False


	def remove_card(self, crd_id):
		# Remove a card from this des
		try:
			if crd_id is not None:
				obj = self.deck[crd_id]
				self.graveyard[crd_id] = obj
				self.deck.pop(crd_id)
				logger.info(f"{crd_id=} was removed from deck")
				self.numCards -= 1
				return obj

		except: 
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
		bins = {
			"Club": {},
			"Diamond": {},
			"Heart": {},
			"Spade": {},
		}
		#print("this was broken by introduction of face up concept")
		
		for card in self.deck:
			crd = self.deck[card]
			bins[crd._suit][crd._face] = crd
		return bins
		


	def deal(self, numCards=0, receiving_deck=None):
		# This is uses remove_card and add_card methods that callks
		# remove from the current deck and add from the recipient deck

		if numCards < 1:
			logger.exception(CountException("Number of cards to distribute is required. "))
		if receiving_deck is None:
			logger.exception(DeckException("A 'destination' deck was not specified"))
		if isinstance(receiving_deck, Deck) is False:
			logger.exception(DeckException("Something was wrong with the destination deck provided"))
		backup_deck = copy.deepcopy(self.deck)
		backup_rec_deck = copy.deepcopy(receiving_deck.deck)

		try: 
			drawn = self.just_draw(numCards)
			for i in drawn:
				receiving_deck.add_card(i, self.deck[i])
				self.remove_card(i)
		except:	
			self.deck = backup_deck
			receiving_deck.deck = backup_rec_deck
			logger.exception(DeckException("Something went wrong womp womp"))


	def compare_2_cards(self, card1, card2):
		results = []
		for i in [card1, card2]:
			rasults
		a = self.rankings[(card1.suit, card1.face)]
		b = self.rankings[(card2.suit, card2.face)] 
