import unittest
from unittest.mock import patch
from CheckPart import isFatherAlive
from spouseOrParentShares import calculate_and_deduct,SpouseWithSonsOrDaughters


class TestFamilyStatus(unittest.TestCase):

    @patch('CheckPart.isFatherAlive')
    def test_isFatherAlive(self, mock_isFatherAlive):
        mock_isFatherAlive.return_value = True
        result = isFatherAlive('y')
        self.assertTrue(result)

        mock_isFatherAlive.return_value = False
        result = isFatherAlive('n')
        self.assertFalse(result)

    @patch('spouseOrParentShares.calculate_and_deduct')
    def test_distribute_amount(self, mock_calculate_and_deduct):
        mock_calculate_and_deduct.return_value = (250.0, 750.0)
        part, remaining = calculate_and_deduct(1000, 0.25, 1)
        self.assertEqual(part, 250.0)
        self.assertEqual(remaining, 750.0)

    @patch('spouseOrParentShares.SpouseWithSonsOrDaughters')
    def test_amount_with_sons_and_daughters(self, mock_SpouseWithSonsOrDaughters):
        mock_SpouseWithSonsOrDaughters.return_value = (1000.0)
        remaining = SpouseWithSonsOrDaughters(1200, 'y','n',0)
        self.assertEqual(remaining, 1000.0)

if __name__ == '__main__':
    unittest.main()