import unittest
from problems import fizzbuzz, reduce_number_to_zero


class TestStringMethods(unittest.TestCase):
    def test_fizzbuzz(self):
        check = fizzbuzz.Solution()
        self.assertEqual(check.fizzbuzz(n=3), ['1', '2', 'Fizz'])
        self.assertEqual(check.fizzbuzz(n=5), ['1', '2', 'Fizz', '4', 'Buzz'])
        self.assertEqual(check.fizzbuzz(n=15),
                         ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14',
                          'FizzBuzz'])

    def test_reduce_number_to_zero(self):
        check = reduce_number_to_zero.Solution()
        self.assertEqual(check.number_of_steps(num=14), 6)
        self.assertEqual(check.number_of_steps(num=8), 4)
        self.assertEqual(check.number_of_steps(num=123), 12)


if __name__ == "__main__":
    unittest.main()
