from random import shuffle

class Card:

    def __init__(self,value,suit):
        self.value = value 
        self.suit = suit
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        """Creates a deck of 52 cards"""
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [ Card(value,suit) for value in values for suit in suits ]
    
    def __repr__(self):
        """Returns the remaining cards in the deck"""
        return f"Deck of {self.count()} cards"
       
    def count(self):
        """Count the cards in the deck"""
        return len(self.cards)

    def _deal(self, nums_of_card):
        """Deal a number of card from the deck"""
        card_count = self.count()
        cards_left = card_count - nums_of_card
        if card_count == 0:
            raise ValueError ("All cards have been dealt")
        elif cards_left < 0: 
            raise ValueError (f"You can only deal {card_count} cards")
        card_dealt = self.cards[:nums_of_card]
        self.cards = self.cards[nums_of_card:]
        return card_dealt

    def shuffle(self):
        """Shuffles a full 52 cards in a deck"""
        if self.count() < 52:
            raise ValueError ("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        """Deal a card to play i guess :)"""
        return self._deal(1)

    def deal_hand(self,hand):
        """Deal gatau juga dah gangerti main poker :)"""
        return self._deal(hand)
 
d = Deck()
# print(d)
# print(d.deal_hand(1000))