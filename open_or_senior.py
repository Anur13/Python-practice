import unittest


def open_or_senior(data):
    # for (age, handicap) in data:
    # return ["Senior" if age >= 55 and handicap > 7 else "Open"]
    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


class Test(unittest.TestCase):
    def test_check(self):
        self.assertEqual(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]),
                         ['Open', 'Senior', 'Open', 'Senior'])

        self.assertEqual(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]),
                         ['Open', 'Open', 'Senior', 'Open'])
