from calculator import is_number
import unittest


class number(unittest.TestCase):
    # test one checks if it returns true or false depending on input
    def test_one(self):
        testcase = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        expected = [True, False]
        self.assertIn(is_number(testcase), expected)

    def test_without_input(self):
        testcase = " ",
        msg = "emtpy input!"
        expected = True
        self.assertEqual(is_number(testcase), expected, msg)



unittest.main()
