from random import randint

class Card(object):
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def get_suit(self):
        if self.suit == 0:
            return 'clubs'
        elif self.suit == 1:
            return 'hearts'
        elif self.suit == 2:
            return 'diamonds'
        elif self.suit == 3:
            return 'spades'

    def get_value(self):
        if self.value < 8:
            return str(self.value +2)
        elif self.value == 8:
            return 'jack'
        elif self.value == 9:
             return 'Queen'
        elif self.value == 10:
             return 'King'
        elif self.value == 11:
             return 'Ace'


    def __str__(self):
        return self.get_value() +' of ' + self.get_suit()

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for value in range(13):
                self.cards.append(Card(suit, value))

    def shuffle(self):
        pass

    def deal_hand(self):
        pass

deck = Deck()

my_cards = deck.cards[randint(0, 51)]
print(my_cards)
