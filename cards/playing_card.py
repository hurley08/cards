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
    def __init__(self, suit, face, faced_down=True, in_hand=False, in_deck=None):
        self.suit = suit
        self.face = face
        self.id = faces[face]+ 10* suits[suit]
        self.faced_down = faecd_down
        self.in_hand = in_hand
        self.in_deck = in_deck

        print(f"The card {self.suit=} of {self.face=} with a value of {self.id} has been created")

    def show(self):
        if self.in_hand is True or self.faced_down is False:
            print(f"{self.id=} (value), {self,suit=}, {self.face=}")
        else:
            raise CardNotVisible("A card must be faced up or in hand to be visible")
    
    def face_up(self):
        if self.faced_down is True:
            try:
                self.faced_down = False
                return True
            except DeckException as e:
                print(e, "Something is wrong")
