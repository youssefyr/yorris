import unittest
from yorris.utils import yr_uppercase

class TestUtils(unittest.TestCase):
    def test_yr_uppercase(self):
        # Test with lowercase string
        self.assertEqual(yr_uppercase("hello"), "HELLO")

        # Test with uppercase string
        self.assertEqual(yr_uppercase("WORLD"), "WORLD")

        # Test with mixed case string
        self.assertEqual(yr_uppercase("HeLLo"), "HELLO")

        # Test with empty string
        self.assertEqual(yr_uppercase(""), "")

        # Test with non-string input
        with self.assertRaises(TypeError):
            yr_uppercase(123)

        # Test with string containing non-alphabetic characters
        self.assertEqual(yr_uppercase("123abc!"), "123ABC!")

if __name__ == '__main__':
    unittest.main()