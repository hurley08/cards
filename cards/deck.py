#cards/deck.py

from dataclasses import dataclass 
from cards.playing_card import suits, faces
from cards.playing_card import PlayingCard
from cards import cardExceptions
import random


standard_deck = {

	('Club', 'Two'): 2,
	('Club', 'Three'): 3,
	('Club', 'Four'): 4,
	('Club', 'Five'): 5,
	('Club', 'Six'): 6,
	('Club', 'Seven'): 7,
	('Club', 'Eight'): 8,
	('Club', 'Nine'): 9,
	('Club', 'Jack'): 10,
	('Club', 'Queen'): 11,
	('Club', 'King'): 12,
	('Club', 'Ace'): 13,
	('Diamond', 'Two'): 22,
	('Diamond', 'Three'): 23,
	('Diamond', 'Four'): 24,
	('Diamond', 'Five'): 25,
	('Diamond', 'Six'): 26,
	('Diamond', 'Seven'): 27,
	('Diamond', 'Eight'): 28,
	('Diamond', 'Nine'): 29,
	('Diamond', 'Jack'): 30,
	('Diamond', 'Queen'): 31,
	('Diamond', 'King'): 32,
	('Diamond', 'Ace'): 33,
	('Heart', 'Two'): 42,
	('Heart', 'Three'): 43,
	('Heart', 'Four'): 44,
	('Heart', 'Five'): 45,
	('Heart', 'Six'): 46,
	('Heart', 'Seven'): 47,
	('Heart', 'Eight'): 48,
	('Heart', 'Nine'): 49,
	('Heart', 'Jack'): 50,
	('Heart', 'Queen'): 51,
	('Heart', 'King'): 52,
	('Heart', 'Ace'): 53,
	('Spade', 'Two'): 62,
	('Spade', 'Three'): 63,
	('Spade', 'Four'): 64,
	('Spade', 'Five'): 65,
	('Spade', 'Six'): 66,
	('Spade', 'Seven'): 67,
	('Spade', 'Eight'): 68,
	('Spade', 'Nine'): 69,
	('Spade', 'Jack'): 70,
	('Spade', 'Queen'): 71,
	('Spade', 'King'): 72,
	('Spade', 'Ace'): 73,


}






class Deck:
	def __init__(self):
		self.deck = []
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
		self.deck = standard_deck
		return self.deck
		#self.deck = self.index

	def draw_hand(self, num_cards, source_deck=None):
		if not self.hand:
			self.hand = Deck()


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
		for key, value in self.deck:
			bins[key][value] = self.deck[(key,value)]
		return bins

	def count(self):
		return len(self.in_hand)


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
