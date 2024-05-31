#cards/deck.py

from dataclasses import dataclass 
from cards.playing_card import suits, faces
from cards.playing_card import PlayingCard
from cardExceptions import *
import random


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


class Deck:
	def __init__(self, name='Standard'):
		self.deck = []
		self.name = name
		print("Deck class instantiated")


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
			this_deck.append(crd)
		for j in this_deck:
			self.add_card(j)

		#self.deck = self.index

	def draw_hand(self, num_cards, source_deck=None):
		if not self.hand:
			self.hand = Deck()
		drawn = random.sample(sorted(self.deck), num_cards)
		for i in drawn:
			self.hand.add

	def add_card(self, playing_card=None):
		if playing_card is not None:
			playing_card.in_deck = True
			self.deck.append(playing_card)
		if playing_card in self.deck:
			print(f"Card {playing_card}, was added to the deck")
			return True
		else:
			return False

	def add_joker(self, num_joker=0):
		# Allows the addition of Jokers which can be played as wildcards

		for i in range(num_joker):
			self.deck.append(PlayingCard(None, "Joker"))

	def dealer_peek_deck(self):
		# Allows a player to view the whole of the deck
		# Intended for very special decks (like Dealers)
		print(self.deck)


	def binned(self, suitsReturn=suits):
		bins = {
			"Club": {},
			"Diamond": {},
			"Heart": {},
			"Spade": {},
		}
		for card in self.deck:
			bins[card.__suit][card.__face] = card
		return bins

	def count(self):
		print(f"This deck contains {len(self.deck):} cards")
		return len(self.deck)


	def deal_card(self, numCards=0, receiving_deck=None):
		if numCards < 1:
			raise CountException("Number of cards to distribute is required. ")
		if deck is None:
			raise DeckException("A 'destination' deck was not specified")
		if isinstance(deck, DeckCards) is False:
			raise DeckException("Something was wrong with the destination deck provided")


		cards_to_distribute = []
		for i in range(numCards):
			chosen = random.sample(self.deck, numCards)
