# Logan Barnes
# Unit testing for grandAdventure.py

import unittest

from grandAdventure import readRoute, adventure

class TestGrandAdventure(unittest.TestCase):
        
            def test_adventure(self):
                routes = [["$", "|", "*"]]
                self.assertEqual(adventure(0, routes), "NO")

            def test_adventure2(self):
                routes = [["*", "*", "*", "t", "t", "t"]]
                self.assertEqual(adventure(0, routes), "NO")
                
            def test_adventure3(self):
                routes = [["$", "|", "*", "j", "t", "b"]]
                self.assertEqual(adventure(0, routes), "YES")

            def test_adventure4(self):
                routes = [[".", ".", ".", ".", ".", "."]]
                self.assertEqual(adventure(0, routes), "YES")

if __name__ == '__main__':
    unittest.main(verbosity=2)
