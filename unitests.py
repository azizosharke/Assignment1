from functions import *
import unittest


class number(unittest.TestCase):
    # test one checks if it returns true or false depending on input
    def test_one(self):
        testcase = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        expected = [True, False]
        self.assertIn(is_number(testcase), expected)

    def test_without_input(self):
        testcase = " ",
        self.assertFalse(is_number(testcase))


class Operator(unittest.TestCase):
    def test_positive_input(self):
        testcase = "+"
        expected = True
        self.assertEqual(is_operator(testcase), expected)

    def test_empty_input(self):
        testcase = " "
        expected = False
        self.assertEqual(is_operator(testcase), expected)


class Operations(unittest.TestCase):
    def test_add(self):
        num1 = 3
        operator = "+"
        num2 = 7
        expected = 10
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_negative_number(self):
        num1 = -3
        operator = "+"
        num2 = 7
        msg = "enter a positive integer"
        expected = 10
        self.assertNotEqual(operation(num1, operator, num2), expected, msg)

    def test_multiply(self):
        num1 = 3
        operator = "*"
        num2 = 7
        expected = 21
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_subtract(self):
        num1 = 3
        operator = "-"
        num2 = 7
        expected = -4
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_divide(self):
        num1 = 3
        operator = "/"
        num2 = 7
        expected = 0.42857142857142855
        self.assertEqual(operation(num1, operator, num2), expected)

    def test_power_of_num(self):
        num1 = 7
        operator = "^"
        num2 = 2
        expected = 49
        self.assertEqual(operation(num1, operator, num2), expected)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)