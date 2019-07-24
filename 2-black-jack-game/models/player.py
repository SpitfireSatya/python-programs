
class Player:

    def __init__(self):
        self.__cards = []
        self.__score = 0

    def hit(self, card):
        self.__cards.append(card)
        self.__score = self.__score + card.value
        if self.is_player_bust() and 'ACE' in [x.name for x in self.__cards]:
            for card in self.__cards:
                if(card.name == 'ACE' and card.value == 10):
                    card.value = 1
                    self.__score = self.__score - 9
                    break

    def is_player_bust(self):
        if self.__score > 21:
            return True
        else:
            return False

    def get_cards(self):
        return [card.name for card in self.__cards]

    def get_score(self):
        return self.__score
