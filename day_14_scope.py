class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        from itertools import combinations

        self.maximumDifference = 0

        for i, j in combinations(self.__elements, 2):
            difference = abs(i - j)
            if self.maximumDifference < difference:
                self.maximumDifference = difference


if __name__ == '__main__':
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
