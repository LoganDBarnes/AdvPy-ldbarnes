# Logan Barnes
# Unit testing for noThanks.py

import unittest

from noThanks import readCards, sortCards, calcScore

class TestNoThanks(unittest.TestCase):
    
        def test_sortCards(self):
            cards = [5, 4, 3, 2, 1]
            sortCards(cards)
            self.assertEqual(cards[0], 1)
            self.assertEqual(cards[1], 2)
            self.assertEqual(cards[2], 3)
            self.assertEqual(cards[3], 4)
            self.assertEqual(cards[4], 5)
    
        def test_calcScore(self):
            cards = [1, 2, 3, 4, 5]
            calcScore(cards)
            self.assertEqual(calcScore(cards), 1)

        def test_calcScore2(self):
            cards = [1, 2, 4, 6, 7]
            calcScore(cards)
            self.assertEqual(calcScore(cards), 11)

if __name__ == '__main__':
    unittest.main(verbosity=2)
