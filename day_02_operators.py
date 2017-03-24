"""
https://www.hackerrank.com/challenges/30-operators
"""


def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent / 100.0
    tax = meal_cost * tax_percent / 100.0
    cost = round(meal_cost + tip + tax)

    return "The total meal cost is %d dollars." % cost


def main():
    meal_cost = float(input(""))
    tip_percent = int(input(""))
    tax_percent = int(input(""))

    print(solve(meal_cost, tip_percent, tax_percent))


if __name__ == '__main__':
    main()


import unittest


class TestSolve(unittest.TestCase):
    def test_solve(self):
        inputs = [
            12.00,
            20,
            8,
        ]

        self.assertEqual(
            "The total meal cost is 15 dollars.",
            solve(inputs[0], inputs[1], inputs[2])
        )
