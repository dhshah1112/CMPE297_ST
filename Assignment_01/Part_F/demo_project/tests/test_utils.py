import unittest
from src.utils import is_even, capitalize_words, fibonacci, safe_divide

class TestUtils(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertFalse(is_even(3))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(-1))

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")
        self.assertEqual(capitalize_words("PYTHON IS AWESOME"), "Python Is Awesome")
        self.assertEqual(capitalize_words(""), "")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), [])
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_safe_divide(self):
        self.assertEqual(safe_divide(10, 2), 5)
        self.assertEqual(safe_divide(7, 3), 7/3)
        self.assertEqual(safe_divide(5, 0), "Error: Division by zero")

if __name__ == '__main__':
    unittest.main()