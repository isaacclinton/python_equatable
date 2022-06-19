import unittest
from src.python_equatable import Equatable


class WithoutEquatable:

    def __init__(self, num, letters):
        self.num = num
        self.letters = letters


class WithEquatableA(Equatable):

    def __init__(self, num, letters):
        self.num = num
        self.letters = letters

    def get_list(self):
        return [self.num, self.letters]


class WithEquatableB(Equatable):

    def __init__(self, num, letters):
        self.num = num
        self.letters = letters

    def get_list(self):
        return [self.num, self.letters]


class TestEquatable(unittest.TestCase):

    def test_equals(self):
        # default behavior
        without_equatable1 = WithoutEquatable(5, "Hello")
        without_equatable2 = WithoutEquatable(5, "Hello")
        self.assertNotEqual(without_equatable1, without_equatable2)

        with_equatable_1 = WithEquatableA(5, "Hello")
        with_equatable_2 = WithEquatableA(5, "Hello")
        self.assertEqual(with_equatable_1, with_equatable_2)

        # doesn't support different classes with same instances
        with_equatable_1 = WithEquatableB(5, "Hello")
        with_equatable_2 = WithEquatableA(5, "Hello")
        self.assertNotEqual(with_equatable_1, with_equatable_2)
