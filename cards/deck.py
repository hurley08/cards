#cards/deck.py

from dataclasses import dataclass 
from cards.playing_card import suits, faces
from cards.playing_card import PlayingCard
from loguru import logger
from cardExceptions import *
import random
import copy
import sys


standard_deck = [
		('Club', 'Two') ,
		('Club', 'Three') ,
		('Club', 'Four') ,
		('Club', 'Five') ,
		('Club', 'Six') ,
		('Club', 'Seven') ,
		('Club', 'Eight') ,
		('Club', 'Nine') ,
		('Club', 'Ten') ,
		('Club', 'Jack') ,
		('Club', 'Queen') ,
		('Club', 'King') ,
		('Club', 'Ace') ,
		('Diamond', 'Two') ,
		('Diamond', 'Three') ,
		('Diamond', 'Four') ,
		('Diamond', 'Five') ,
		('Diamond', 'Six') ,
		('Diamond', 'Seven') ,
		('Diamond', 'Eight') ,
		('Diamond', 'Nine') ,
		('Diamond', 'Ten') ,
		('Diamond', 'Jack') ,
		('Diamond', 'Queen') ,
		('Diamond', 'King') ,
		('Diamond', 'Ace') ,
		('Heart', 'Two') ,
		('Heart', 'Three') ,
		('Heart', 'Four') ,
		('Heart', 'Five') ,
		('Heart', 'Six') ,
		('Heart', 'Seven') ,
		('Heart', 'Eight') ,
		('Heart', 'Nine') ,
		('Heart', 'Ten') ,
		('Heart', 'Jack') ,
		('Heart', 'Queen') ,
		('Heart', 'King') ,
		('Heart', 'Ace') ,
		('Spade', 'Two') ,
		('Spade', 'Three') ,
		('Spade', 'Four') ,
		('Spade', 'Five') ,
		('Spade', 'Six') ,
		('Spade', 'Seven') ,
		('Spade', 'Eight') ,
		('Spade', 'Nine') ,
		('Spade', 'Ten') ,
		('Spade', 'Jack') ,
		('Spade', 'Queen') ,
		('Spade', 'King') ,
		('Spade', 'Ace') ,
]

logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")
logger.add("deck_{time}.log")
logger.level("DEBUG", color="<blue>")
logger.level("INFO", color="<white>")
logger.level("SUCCESS", color="<green>")
logger.level("ERROR", color="<red>")
logger.level("CRITICAL", color="<magenta")


class Deck:
	def __init__(self, name='Standard'):
		# Initializes I robably would be ab
		self.deck = {}
		self.name = name
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
		for i in list(standard_deck):
			crd = PlayingCard(i[0],i[1])
			self.add_card(playing_card=crd)	
		logger.info(f"{self.name} and dec")
		#print(self.deck)	
		

	def just_draw(self, num_cards):
		# Draw a specified number of cards from deck
	
		drawn = random.sample(sorted(self.deck), num_cards)
		card_list = []
		for i in drawn:
			card_list.append(self.deck[i])
		return card_list
			

	def add_card(self, playing_card=None):
		# Utility to add card to either hand or into deck 
		# Adds to deck first by default
		if playing_card is not None:
			if isinstance(playing_card, PlayingCard) == True:
				try:	
					crd_id = (playing_card._suit, playing_card._face)
					self.deck[crd_id] = playing_card
				except:
					raise DeckException("Something went wrong here")
				finally:
					if crd_id in self.deck:
						#print(f"Card {playing_card}, was added to the deck")
						return True
					else:
						return False

	def remove_card(self, playing_card=None):
		# remove a card from this desk

		try:
			if playing_card is not None and isinstance(playing_card, PlayingCard):
				crd_id = (playing_card._suit, playing_card._face)
				self.deck.pop(crd_id)
				#print("Card removed from deck")
		except: 
			raise DeckException("COULDN'T REMOVE MATE")




	def add_joker(self, num_joker=0):
		# Allows the addition of Jokers which can be played as wildcards

		for i in range(num_joker):
			self.deck.append(PlayingCard(None, "Joker"))

	def dealer_peek_deck(self):
		# Allows a player to view the whole of the deck
		# Intended for very special decks (like Dealers)
		print(self.deck)


	def binned(self, suitsReturn=suits):
		# Bins cards for analysis. Should typically be disabled
		self.count()
		bins = {
			"Club": {},
			"Diamond": {},
			"Heart": {},
			"Spade": {},
		}
		for card in self.deck:
			crd = self.deck[card]
			bins[crd._suit][crd._face] = crd
		return bins

	def count(self):
		#print(f"{self.name}'s deck contains {len(self.deck):} cards")
		return len(self.deck)


	def deal_card(self, numCards=0, receiving_deck=None):
		if numCards < 1:
			raise CountException("Number of cards to distribute is required. ")
		if receiving_deck is None:
			raise DeckException("A 'destination' deck was not specified")
		if isinstance(receiving_deck, Deck) is False:
			raise DeckException("Something was wrong with the destination deck provided")
		backup_deck = copy.deepcopy(self.deck)
		backup_rec_deck = copy.deepcopy(receiving_deck.deck)

		try: 
			drawn = self.just_draw(numCards)
			for i in drawn:
				receiving_deck.add_card(i)
				self.remove_card(i)
		except:	
			raise DeckException("Something went wrong womp womp")
			self.deck = backup_deck
			receiving_deck.deck = backup_rec_deck



