import operator
import unittest

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.floordiv}

ops["+"](1, 1)  # prints 2


def zero(args=None):  # your code here
    local = 0
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def one(args=None):  # your code here
    local = 1
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def two(args=None):  # your code here
    local = 2
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def three(args=None):  # your code here
    local = 3
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def four(args=None):  # your code here
    local = 4
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def five(args=None):  # your code here
    local = 5
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def six(args=None):  # your code here
    local = 6
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def seven(args=None):  # your code here
    local = 7
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def eight(args=None):  # your code here
    local = 8
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def nine(args=None):  # your code here
    local = 9
    if args:
        number, operation = args
        return ops[operation](local, number)
    else:
        return local


def plus(return_value):  # your code here
    return [return_value, '+']


def minus(return_value):  # your code here
    return [return_value, '-']


def times(return_value):  # your code here
    return [return_value, '*']


def divided_by(return_value):  # your code here
    return [return_value, '/']


class test(unittest.TestCase):
    def test_nums(self):
        self.assertEqual(seven(times(five())), 35)
        self.assertEqual(four(plus(nine())), 13)
        self.assertEqual(eight(minus(three())), 5)
        self.assertEqual(six(divided_by(two())), 3)


# def zero(arg=""):  return eval("0" + arg)
# def one(arg=""):   return eval("1" + arg)
# def two(arg=""):   return eval("2" + arg)
# def three(arg=""): return eval("3" + arg)
# def four(arg=""):  return eval("4" + arg)
# def five(arg=""):  return eval("5" + arg)
# def six(arg=""):   return eval("6" + arg)
# def seven(arg=""): return eval("7" + arg)
# def eight(arg=""): return eval("8" + arg)
# def nine(arg=""):  return eval("9" + arg)
#
# def plus(n):       return "+%s" % n
# def minus(n):      return "-%s" % n
# def times(n):      return "*%s" % n
# def divided_by(n): return "/%s" % n