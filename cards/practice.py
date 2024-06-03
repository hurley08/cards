# practice.py
 
from cards.deck import Deck
from cards.deck import standard_deck
from cards.playing_card import PlayingCard, suits, faces
from cardExceptions import *

from dataclasses import dataclass
from typing import List
import random



def generate_std_deck(suits, faces):
	std_deck = []
	for i in suits:
		for j in faces:
			tup =f"('{i}', '{j}')"
			std_deck.append(tup)
			print(tup,',')
	return std_deck



d = Deck()
d.generate_deck()
print(d.deck)
print(d.binned())
print(d.count())
L = d.binned()
for i in L:
	print(i)
	print(L[i], '\n')


d2 = Deck(name="Player")
d2.count()
d.deal_card(2, d2)
