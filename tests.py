import unittest
from main import fib

class TestFib(unittest.TestCase):
    def test_fib_negative_number_is_zero(self):
        self.assertEqual(fib(-1), 0)

    def test_fib_zero_is_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fib_one_is_one(self):
        self.assertEqual(fib(1), 1)

    def test_fib_two_is_one(self):
        self.assertEqual(fib(2), 1)

    def test_fib_big_number_returns(self):
        self.assertEqual(fib(20), 6765)


if __name__ == '__main__':
    unittest.main()