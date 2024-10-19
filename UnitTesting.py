import unittest
from unittest.mock import patch
from AreFatherMotherWifeAlive import is_father_alive
from SpouseAndParentSharesCalculation import calculate_and_deduct, spouse_with_sons_or_daughters

class TestFamilyStatus(unittest.TestCase):

    @patch('AreFatherMotherWifeAlive.is_father_alive')
    def test_isFatherAlive(self, mock_isFatherAlive):
        mock_isFatherAlive.return_value = True
        self.assertTrue(is_father_alive('y'))  # Expect True for 'y'

        mock_isFatherAlive.return_value = False
        self.assertFalse(is_father_alive('n'))  # Expect False for 'n'

    def test_distribute_amount(self):
        part, remaining = calculate_and_deduct(1000, 0.25, 1)
        self.assertEqual(part, 250.0)  # Check if the part is 250.0
        self.assertEqual(remaining, 750.0)  # Check if the remaining amount is 750.0

    @patch('SpouseAndParentSharesCalculation.spouse_with_sons_or_daughters')
    def test_amount_with_sons_and_daughters(self, mock_SpouseWithSonsOrDaughters):
        mock_SpouseWithSonsOrDaughters.return_value = 1000.0
        remaining = spouse_with_sons_or_daughters(1200, 'y', 'n', 0)
        self.assertEqual(remaining, 1000.0)  # Check the expected remaining amount

if __name__ == '__main__':
    unittest.main()
