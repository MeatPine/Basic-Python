import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, error_type, error, traceback):
        end = time.perf_counter()
        print("Время:", end - self.start, "секунд")


def some_function():
    total = 0

    for number in range(100000):
        total += number

    return total


with Timer():
    result = some_function()

print("Результат:", result)