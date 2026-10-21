import numpy as np


def average(numbers, k):
    if type(k) is not int or k <= 0 or k > len(numbers):
        raise ValueError("Неверный размер окна.")

    result = []

    for i in range(len(numbers) - k + 1):
        total = 0

        for j in range(i, i + k):
            total += numbers[j]

        result.append(total / k)

    return result


def average_numpy(numbers, k):
    if type(k) is not int or k <= 0 or k > len(numbers):
        raise ValueError("Неверный размер окна.")

    result = []

    for i in range(len(numbers) - k + 1):
        window = numbers[i:i + k]
        result.append(float(np.mean(window)))

    return result


def average_fast(numbers, k):
    if type(k) is not int or k <= 0 or k > len(numbers):
        raise ValueError("Неверный размер окна.")

    total = 0

    for i in range(k):
        total += numbers[i]

    result = [total / k]

    for i in range(k, len(numbers)):
        total -= numbers[i - k]
        total += numbers[i]

        result.append(total / k)

    return result


def main():
    numbers = [2, 4, 6, 8, 10]

    for k in [1, 3, 5, 0, 6]:
        print("\nРазмер окна:", k)

        try:
            a = average(numbers, k)
            b = average_numpy(numbers, k)
            c = average_fast(numbers, k)

            print("Обычный вариант:", a)
            print("NumPy:", b)
            print("Быстрый вариант:", c)

            same = True

            for i in range(len(a)):
                if abs(a[i] - b[i]) > 0.000001:
                    same = False

                if abs(a[i] - c[i]) > 0.000001:
                    same = False

            print("Результаты совпадают:", same)

        except ValueError as error:
            print(error)


main()