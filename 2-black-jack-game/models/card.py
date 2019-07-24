
class Card:

    def __init__(self, suite, name, card_type, value):
        self.suite = suite
        self.name = name
        self.card_type = card_type
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

