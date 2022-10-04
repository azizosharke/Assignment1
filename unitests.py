from calculator import operation
import unittest

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

unittest.main()
