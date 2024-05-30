# practice.py
 
from cards.deck import Deck
from cards.playing_card import PlayingCard, suits, faces
from cards import cardExceptions


from dataclasses import dataclass
from typing import List
import random

d = Deck()
d.generate_deck()
print(d.deck)
print(d.binned())
print(d.count())

