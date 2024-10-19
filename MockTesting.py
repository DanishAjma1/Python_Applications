import unittest
from unittest.mock import patch
from AreFatherMotherWifeAlive import is_father_alive
from SpouseAndParentSharesCalculation import calculate_and_deduct, spouse_with_sons_or_daughters

class TestFamilyStatus(unittest.TestCase):

    @patch('AreFatherMotherWifeAlive.is_father_alive')
    def test_is_father_alive(self, mock_isFatherAlive):
        mock_isFatherAlive.return_value = True
        result = is_father_alive('y')
        self.assertTrue(result)

        mock_isFatherAlive.return_value = False
        result = is_father_alive('n')
        self.assertFalse(result)

    @patch('SpouseAndParentSharesCalculation.calculate_and_deduct')
    def test_distribute_amount(self, mock_calculate_and_deduct):
        mock_calculate_and_deduct.return_value = (250.0, 750.0)
        part, remaining = calculate_and_deduct(1000, 0.25, 1)
        self.assertEqual(part, 250.0)
        self.assertEqual(remaining, 750.0)

    @patch('SpouseAndParentSharesCalculation.spouse_with_sons_or_daughters')
    def test_amount_with_sons_and_daughters(self, mock_SpouseWithSonsOrDaughters):
        mock_SpouseWithSonsOrDaughters.return_value = 1000.0
        remaining = spouse_with_sons_or_daughters(1200, 'y', 'n', 0)
        self.assertEqual(remaining, 1000.0)

if __name__ == '__main__':
    unittest.main()
