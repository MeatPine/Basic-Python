import time
from functools import wraps


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        try:
            result = function(*args, **kwargs)
            return result
        finally:
            end = time.perf_counter()
            print("Время:", end - start, "секунд")

    return wrapper


@measure_time
def hello():
    print("Привет!")


@measure_time
def add(a, b):
    return a + b


@measure_time
def calculate(n):
    total = 0

    for i in range(n):
        total += i

    return total


def main():
    hello()

    print("Сумма:", add(10, b=5))
    print("Результат:", calculate(100000))


main()