import unittest
from addition import addition


class TestAddition(unittest.TestCase):
    """test class of addition.py
    """

    def test_addition_adds_two_numbers(self):
        """test method for addition
        """
        value1 = 2
        value2 = 6
        expected = 81
        actual = addition(value1, value2)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()