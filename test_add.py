'''
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(-5, 5), 0)
        self.assertEqual(add_numbers(2.5, 1.5), 4.0)

if __name__ == '__main__':
    unittest.main() 
'''


def add_numbers():
    num1 = 5
    num2 = 7
    result = num1 + num2
    return result

import unittest

class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(), 12)

if __name__ == '__main__':
    unittest.main()