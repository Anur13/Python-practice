import string
import unittest


def find_missing_letter(chars: list) -> str:
    alphabet = string.ascii_letters
    index_of_prev = None
    for i in range(len(chars)):
        if i == 0:
            index_of_prev = alphabet.index(chars[i])
            continue
        if alphabet.index(chars[i]) - 1 != index_of_prev:
            return alphabet[index_of_prev + 1]
        index_of_prev = alphabet.index(chars[i])


class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual('e', find_missing_letter(['a', 'b', 'c', 'd', 'f']), )
        self.assertEqual('P', find_missing_letter(['O', 'Q', 'R', 'S']), )


