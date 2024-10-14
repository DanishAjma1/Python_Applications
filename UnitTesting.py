import unittest
from CheckPart import isFatherAlive
from spouseOrParentShares import calculate_and_deduct, SpouseWithSonsOrDaughters

class TestFamilyStatus(unittest.TestCase):

    def test_isFatherAlive(self):

        self.assertTrue(isFatherAlive('y'))  # Expect True for 'y'
        self.assertFalse(isFatherAlive('n'))  # Expect False for 'n'

    def test_distribute_amount(self):
        part, remaining = calculate_and_deduct(1000, 0.25, 1)
        self.assertEqual(part, 250.0)  # Check if the part is 250.0
        self.assertEqual(remaining, 750.0)  # Check if the remaining amount is 750.0

    def test_amount_with_sons_and_daughters(self):
        remaining = SpouseWithSonsOrDaughters(1200, 'y', 'n', 0)
        self.assertEqual(remaining, 1000.0)  # Check the expected remaining amount

if __name__ == '__main__':
    unittest.main()
