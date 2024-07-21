
import frappe
import unittest
from program_management.program_management.customization.my_custom_function import add_numbers

class TestMyCustomFunction(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(1.5, 2.5), 4.0)

    def test_add_numbers_invalid_input(self):
        with self.assertRaises(ValueError):
            add_numbers(1, "a")

if __name__ == '__main__':
    unittest.main()
