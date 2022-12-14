#Logan Barnes
#Unit testing for rightOfWay.py

import unittest
from rightOfWay import goingStraight, turningLeft, vehicleAhead, vehicleRight

class TestRightOfWay(unittest.TestCase):
    
        def test_goingStraight(self):
            goingStraight('South', 'North')
            self.assertTrue(goingStraight('South', 'North'))

        def test_turningLeft(self):
            turningLeft('South', 'West')
            self.assertTrue(turningLeft('South', 'West'))

        def test_vehicleAhead(self):
            vehicleAhead('South', 'North')
            self.assertTrue(vehicleAhead('South', 'North'))

        def test_vehicleRight(self):
            vehicleRight('South', 'East')
            self.assertTrue(vehicleRight('South', 'East'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
    