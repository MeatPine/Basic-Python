def spiral(n, m, reverse=False):
    if n <= 0 or m <= 0:
        raise ValueError("Размеры должны быть больше нуля.")

    matrix = []

    for i in range(n):
        matrix.append([0] * m)

    top = 0
    bottom = n - 1
    left = 0
    right = m - 1

    number = 1
    step = 1

    if reverse:
        number = n * m
        step = -1

    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            matrix[top][j] = number
            number += step

        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = number
            number += step

        right -= 1

        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = number
                number += step

            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = number
                number += step

            left += 1

    return matrix


def main():
    sizes = [(3, 3), (3, 5), (4, 2)]

    for n, m in sizes:
        print(f"\nМатрица {n} * {m}:")

        matrix = spiral(n, m)

        for row in matrix:
            print(*row)

        print("Обратное заполнение:")

        matrix = spiral(n, m, True)

        for row in matrix:
            print(*row)


main()