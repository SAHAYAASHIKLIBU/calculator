# test/addition_test.py
import unittest
import sys
import os

# Add the parent directory to the system path so we can import addition.py
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from addition import additon  # Import the function to test

class TestAddition(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(additon(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(additon(-2, -3), -5)

    def test_add_positive_and_negative(self):
        self.assertEqual(additon(5, -3), 8)

    def test_add_zero(self):
        self.assertEqual(additon(0, 0), 0)
        self.assertEqual(additon(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
