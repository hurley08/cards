# cards/cards.py

from dataclasses import dataclass
from cards import cardExceptions




suits = {
 'Club': 0,
 'Diamond': 2,
 'Heart': 4,
 'Spade': 6,
}

faces = {
 'Two': 2,
 'Three': 3,
 'Four': 4,
 'Five': 5,
 'Six': 6,
 'Seven': 7,
 'Eight': 8,
 'Nine': 9,
 'Ten':10,
 'Jack': 11,
 'Queen': 12,
 'King': 13,
  'Ace': 14,
}

@dataclass
class PlayingCard:
    def __init__(self, suit, face, face_up=False, in_hand=False, in_deck=None):
        self.__suit = suit
        self.__face = face
        self.__id = faces[face]+ 10 * suits[suit]
        self.face_up = face_up
        self.in_hand = in_hand
        self.in_deck = in_deck

        print(f"The card {self.__suit:} of {self.__face:} with a value of {self.__id:} has been created")

    def show(self):
        if self.in_hand is True or self.face_up is False:
            print(f"{self.__id=} (value), {self,__suit=}, {self.__face=}")
        else:
            raise CardNotViewable("A card must be faced up or in hand to be visible")
    
    def flip(self):
        pre_val = self.face_up
        try:
            self.face_up = True if self.face_up is False else False
            if self.face_up is not pre_val:
                return True
        except DeckException as e:
            raise(e, "Something is wrong")
        return False
