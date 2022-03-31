import unittest


def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


class Test(unittest.TestCase):
    def test_som(self):
        self.assertEquals("odd", odd_or_even([0, 1, 2]))
        self.assertEqual("even", odd_or_even([0, 1, 3]))
        self.assertEqual("even", odd_or_even([1023, 1, 2]))


def high_and_low(numbers):
    sorted_nums = sorted(list(map(int, numbers.split(" "))))
    return f"{sorted_nums[-1]} {sorted_nums[0]}"


class Test1(unittest.TestCase):
    def test_som(self):
        self.assertEqual("42 -9", high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
        self.assertEqual("3 1", high_and_low("1 2 3"))
