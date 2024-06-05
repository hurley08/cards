# cards/cards.py

from dataclasses import dataclass
from cards.tables import Tables 
from cards.cardExceptions import *
import logging

logger = logging.getLogger(__name__)


ranking = Tables().rankings_single_level

@dataclass
class PlayingCard:
    def __init__(self, suit, face, face_up=False, in_hand=False):
        # Initialize a playing card object. 
        self.__Suit = suit
        self.__Face = face
        self.face = "Hidden"
        self.suit = "Hidden"
        self.face_up = face_up
        self.in_hand = in_hand
        self.rankings = ranking
        logging.info(f"Instantiated {suit:} of {face:}")

    def __gt__(self, other):
        if self.face_up or self.in_hand:
            if other.face_up or other.in_hand:
                return self.rankings[(self.suit, self.face)] > other.rankings[(other.suit, other.face)]
        raise cardNotViewable("One or both cards are hidden")




    def show(self):
        # Reveals the card if it is face up
        logging.debug(f"Show card {self.face_up=}, {self.in_hand=}]")
        if self.face_up is True or self.in_hand is True:
            return self.suit, self.face
        else:
            print("This card is not visible")
            


    
    def flip(self):
        logging.debug("Flipping card")
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
