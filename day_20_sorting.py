"""
Day 20: Sorting

https://www.hackerrank.com/challenges/30-sorting
"""
import unittest


def sorting(arr):
    num_of_swaps = 0

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                num_of_swaps += 1

        if num_of_swaps == 0:
            break

    return """Array is sorted in {} swaps.
First Element: {}
Last Element: {}""".format(num_of_swaps, arr[0], arr[-1])


if __name__ == '__main__':
    n = int(input().strip())
    a = [int(a_temp) for a_temp in input().strip().split(' ')]

    print(sorting(a))


class TestSorting(unittest.TestCase):
    def test_sorting(self):
        self.assertEqual(
            """Array is sorted in 0 swaps.
First Element: 1
Last Element: 3""",
            sorting([1, 2, 3])
        )

        self.assertEqual(
            """Array is sorted in 3 swaps.
First Element: 1
Last Element: 3""",
            sorting([3, 2, 1])
        )
