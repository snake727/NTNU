from test5 import valid_password
import unittest   # The test framework

class TestPassword(unittest.TestCase):

    def too_short_password(self):
        self.assertEqual(valid_password("ahjd"), True)

    def only_digits_in_pass(self):
        self.assertEqual(valid_password("ahjd"), True)

if __name__ == '__main__':
    unittest.main()
