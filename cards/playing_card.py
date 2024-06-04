# cards/cards.py

from dataclasses import dataclass
from cards import cardExceptions
import logging

logger = logging.getLogger(__name__)

@dataclass
class PlayingCard:
    def __init__(self, suit, face, face_up=False, in_hand=False, in_deck=None):
        # Initialize a playing card object. 
        self.__Suit = suit
        self.__Face = face
        self.face = "Hidden"
        self.suit = "Hidden"
        self.face_up = face_up
        self.in_hand = in_hand
        self.in_deck = in_deck
        logging.info(f"The card {self.__Suit:} of {self.__Face:}")


    def __repr__(self):
        # Wraps the show method
        self.show()

    def show(self):
        # Reveals the card if it is face up
        if self.face_up is False:
            print("The card is face down and cannot be seen")
        logging.debug(f"Show card {self.face_up=}, {self.in_hand=}]")
        return (self.face, self.suit)
    
    def flip(self):
        logging.info("Flipping card")
        if self.face_up is False:
            self.face = self.__Face
            self.suit = self.__Suit
            self.face_up = True
            logging.info("Revealing card")
        else:
            self.face = "Hidden"
            self.suit = "Hidden"
            self.face_up = False
            logging.info("Card hidden")
