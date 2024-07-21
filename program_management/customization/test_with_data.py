

import frappe
import unittest
from unittest.mock import patch
from program_management.program_management.customization.my_custom_function import add_numbers

class TestMyCustomFunctionWithMocking(unittest.TestCase):

    @patch('frappe.db.get_value')
    def test_add_numbers_with_mocking(self, mock_get_value):
        mock_get_value.return_value = 10
        result = add_numbers(mock_get_value(), 5)
        self.assertEqual(result, 15)

    def test_add_numbers_edge_cases(self):
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-1, -1), -2)
        self.assertEqual(add_numbers(1e10, 1e10), 2e10)
        self.assertEqual(add_numbers(-1e10, 1e10), 0)

if __name__ == '__main__':
    unittest.main()
