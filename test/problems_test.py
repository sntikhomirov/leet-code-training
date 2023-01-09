import unittest
from problems import fizzbuzz


class TestStringMethods(unittest.TestCase):
    def test_fizzbuzz(self):
        check = fizzbuzz.Solution()
        self.assertEqual(check.fizzbuzz(n=3), ['1', '2', 'Fizz'])
        self.assertEqual(check.fizzbuzz(n=5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(check.fizzbuzz(n=15),
                         ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
                          'FizzBuzz'])


if __name__ == "__main__":
    unittest.main()
