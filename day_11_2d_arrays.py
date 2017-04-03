def solve(A):
    pattern = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 1, 1],
    ]
    pattern_len_row = len(pattern)
    pattern_len_col = len(pattern[0])
    max_value = -999999
    A_len_row= len(A)
    A_len_col = len(A[0])

    for row in range(A_len_row - pattern_len_row + 1):
        for col in range(A_len_col - pattern_len_col + 1):
            pattern_sum = 0

            for p_row in range(pattern_len_row):
                pattern_sum += sum(
                    [a * b for a, b in zip(
                        pattern[p_row], A[row + p_row][col:col + pattern_len_col])])

            if max_value < pattern_sum:
                max_value = pattern_sum

    return max_value


def main():
    A = []
    for _ in range(6):
        A.append(list(map(int, input("").strip().split())))

    print(solve(A))


if __name__ == '__main__':
    main()
