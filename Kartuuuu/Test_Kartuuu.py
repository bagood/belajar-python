from Kartuuuu import Card 
from Kartuuuu import Deck 
import unittest

class CardTests(unittest.TestCase):
    def setUp(self): 
        self.card = Card("A" , "Hearts")

    def test_init(self): 
        """test the self.value and self.suit in init fuction"""
        self.assertEqual(self.card.value, "A")
        self.assertEqual(self.card.suit, "Hearts")
    
    def test_repr(self):
        """repr should return A of Hearts"""
        self.assertEqual(f"{self.card.value} of {self.card.suit}", "A of Hearts")

class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_init(self):
        """should create a deck full of 52 cards"""
        self.assertEqual(isinstance(self.deck.cards, list),True)
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """Should return the remaining card in the deck"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """should count the cards in the deck"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_works(self):
        """should take a number of random card from a deck and substracted the amount of card in the deck"""
        cards = self.deck._deal(2)
        self.assertEqual(len(self.deck.cards),50)

    def test_deal_0_deck(self):
        """should return a value error cause there is no more card in the deck"""
        self.deck._deal(52)
        with self.assertRaises(ValueError):
            self.deck._deal(2)
    
    def test_deal_0_cardsleft(self):
        """should return a value error cause you dealt more cards than you have in the deck"""
        with self.assertRaises(ValueError):
            self.deck._deal(100)

    def test_shuffle_notwork(self):
        """should return a value error cause you shuffle a unfull deck"""
        self.deck._deal(12)
        with self.assertRaises(ValueError):
            self.deck.shuffle()  


if __name__  == "__main__": 
    unittest.main()
