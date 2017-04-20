"""
Day 26: Nested Logic

https://www.hackerrank.com/challenges/30-nested-logic
"""
import unittest
from datetime import date


def solve(input1, input2):
    d1, m1, y1 = map(lambda x: int(x), input1.split(" "))
    d2, m2, y2 = map(lambda x: int(x), input2.split(" "))

    actual = date(year=y1, month=m1, day=d1)
    expected = date(year=y2, month=m2, day=d2)

    delta = actual - expected
    if delta.days <= 0:
        return 0

    if expected.year == actual.year and expected.month == actual.month:
        return delta.days * 15

    if actual.year == expected.year and actual.month > expected.month:
        return (actual.month - expected.month) * 500

    if actual.year > expected.year:
        return 10000

    return 0


if __name__ == '__main__':
    input1 = input("")
    input2 = input("")

    print(solve(input1, input2))


class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(
            45,
            solve("9 6 2017", "6 6 2017")
        )
