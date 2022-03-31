import unittest
import string


def alphabet_position(text):
    alphabet = list(string.ascii_lowercase)
    return ' '.join(str(alphabet.index(n.lower()) + 1) for n in text if n.isalpha())


class TestString(unittest.TestCase):
    def test_equals(self):
        given_input = alphabet_position("The sunset sets at twelve o' clock.")
        expected = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
        self.assertEqual(expected, given_input)

        given_input = alphabet_position("The narwhal bacons at midnight.")
        expected = "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"
        self.assertEqual(given_input, expected)
