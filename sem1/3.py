def compress(numbers):
    result = []

    if len(numbers) == 0:
        return result

    number = numbers[0]
    count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == number:
            count += 1
        else:
            result.append((number, count))
            number = numbers[i]
            count = 1

    result.append((number, count))

    return result


def restore(groups):
    result = []

    for number, count in groups:
        for i in range(count):
            result.append(number)

    return result


def main():
    tests = [
        [1, 1, 1, 2, 2, 5, 5, 5, 5, 3],
        [],
        [7],
        [1, 2, 1]
    ]

    for numbers in tests:
        groups = compress(numbers)
        result = restore(groups)

        print("Исходный список:", numbers)
        print("Сжатый:", groups)
        print("Восстановленный:", result)
        print("Совпадают:", numbers == result)
        print()


main()