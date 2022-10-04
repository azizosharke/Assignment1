from calculator import is_operator
import unittest



class Operator(unittest.TestCase):
    def test_positive_input(self):
        testcase = "+"
        expected = True
        self.assertEqual(is_operator(testcase), expected)

    def test_with_int_input(self):
        testcase = 1324,
        msg = "please don't enter string token"
        expected = True
        self.assertEqual(is_number(testcase), expected, msg)

    def test_with_empty_input(self):
        testcase = " ",
        msg = "input can't be empty"
        expected = False
        self.assertEqual(is_number(testcase), expected, msg)




unittest.main()
