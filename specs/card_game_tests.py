import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_game = CardGame()
        self.card_1 = Card("Diamonds", 1)
        self.card_3 = Card("Clubs", 4)
        self.card_2 = Card("Spades", 10)
        self.cards = [self.card_1, self.card_2, self.card_3]

    def test_check_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_1))

    def test_check_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_2))

    def test_highest_card(self):
        self.assertEqual(
            self.card_2, self.card_game.highest_card(self.card_2, self.card_3)
        )

    def test_cards_total(self):
        self.assertEqual(
            "You have a total of 15", self.card_game.cards_total(self.cards)
        )
