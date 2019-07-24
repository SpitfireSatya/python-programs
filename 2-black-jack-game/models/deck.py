
from random import shuffle
from models.card import Card


class Deck:

    __suites = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    __names = ('ACE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN',
               'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING')


    def __init__(self):
        self.__cards = []
        self.__initialize_deck()

    def __initialize_deck(self):
        for suite in self.__suites:
            for count, name in enumerate(self.__names, start=1):
                if name == 'ACE':
                    card = Card(suite, name, 'ACE', 10)
                elif name == 'JACK' or name == 'QUEEN' or name == 'KING':
                    card = Card(suite, name, 'FACE_CARD', 10)
                else:
                    card = Card(suite, name, 'RANKS', count)

                self.__cards.append(card)

    def get_cards(self):
        return self.__cards

    def shuffle(self):
        shuffle(self.__cards)

    def draw_card(self):
        return self.__cards.pop()