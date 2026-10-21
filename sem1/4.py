def find_point(points, x0, y0):
    if len(points) == 0:
        raise ValueError("Список точек пуст.")

    best = points[0]

    x, y = best
    min_square = (x - x0) ** 2 + (y - y0) ** 2

    for point in points:
        x, y = point

        square = (x - x0) ** 2 + (y - y0) ** 2

        # При одинаковом расстоянии сохраняем первую точку.
        if square < min_square:
            min_square = square
            best = point

    # Квадратный корень возрастает вместе с числом.
    # Поэтому для поиска минимума достаточно сравнивать
    # квадраты расстояний. Корень нужен только для ответа.
    distance = min_square ** 0.5

    return best, distance


def main():
    tests = [
        [(3, 4), (1, 0), (0, 1)],
        [(3, 4)],
        []
    ]

    for points in tests:
        try:
            point, distance = find_point(points, 0, 0)

            print("Ближайшая точка:", point)
            print("Расстояние:", distance)

        except ValueError as error:
            print(error)


main()
