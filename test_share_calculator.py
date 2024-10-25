import unittest
from unittest.mock import patch
from shares_calculator_application_main import is_father_alive,calculate_and_deduct,calculate_shares_for_spouse_with_sons_or_daughters

class TestFamilyStatus(unittest.TestCase):

    @patch('SharesApplicationMain.is_father_alive')
    def test_is_father_alive(self, mock_isFatherAlive):
        mock_isFatherAlive.return_value = True
        result = is_father_alive('y')
        self.assertTrue(result)

        mock_isFatherAlive.return_value = False
        result = is_father_alive('n')
        self.assertFalse(result)

    @patch('SharesApplicationMain.calculate_and_deduct')
    def test_distribute_amount(self, mock_calculate_and_deduct):
        mock_calculate_and_deduct.return_value = (250.0, 750.0)
        part, remaining = calculate_and_deduct(1000, 0.25, 1)
        self.assertEqual(part, 250.0)
        self.assertEqual(remaining, 750.0)

    @patch('SharesApplicationMain.calculate_shares_for_spouse_with_sons_or_daughters')
    def test_amount_with_sons_and_daughters(self, mock_SpouseWithSonsOrDaughters):
        mock_SpouseWithSonsOrDaughters.return_value = 1000.0
        remaining = calculate_shares_for_spouse_with_sons_or_daughters(1200, 'y', 'n', 0)
        self.assertEqual(remaining, 1000.0)

class TestFamilyStatus(unittest.TestCase):

    def test_is_father_alive(self):
        result = is_father_alive('y')
        self.assertTrue(result)
        result = is_father_alive('n')
        self.assertFalse(result)

    def test_calculate_and_deduct(self):
        part, remaining = calculate_and_deduct(1000, 0.25, 1)
        self.assertEqual(part, 250.0)
        self.assertEqual(remaining, 750.0)
        part, remaining = calculate_and_deduct(500, 0.5, 2)
        self.assertEqual(part, 250.0)
        self.assertEqual(remaining, 0.0)

    def test_calculate_shares_for_spouse_with_sons_or_daughters(self):
        remaining = calculate_shares_for_spouse_with_sons_or_daughters(1200, 'y', 'n', 1)
        self.assertGreaterEqual(remaining, 0)
        remaining = calculate_shares_for_spouse_with_sons_or_daughters(1200, 'n', 'n', 0)
        self.assertGreaterEqual(remaining, 0)


if __name__ == '__main__':
    unittest.main()

