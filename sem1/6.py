import random
from faker import Faker


def create_file(path, count):
    fake = Faker("ru_RU")

    with open(path, "w", encoding="utf-8") as file:
        for i in range(count):
            name = fake.name()
            score = random.randint(0, 100)

            file.write(f"{name};{score}\n")


def read_scores(path):
    total = 0
    count = 0
    passed = 0

    min_score = None
    max_score = None
    best_name = ""

    with open(path, encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split(";")

            if len(parts) != 2:
                print("Неверная строка:", line.strip())
                continue

            name = parts[0].strip()

            try:
                score = int(parts[1])
            except ValueError:
                print("Неверный балл:", line.strip())
                continue

            if name == "" or score < 0 or score > 100:
                print("Неверные данные:", line.strip())
                continue

            total += score
            count += 1

            if score >= 60:
                passed += 1

            if min_score is None or score < min_score:
                min_score = score

            if max_score is None or score > max_score:
                max_score = score
                best_name = name

    if count == 0:
        print("Нет корректных записей.")
        return

    print("Средний балл:", total / count)
    print("Минимум:", min_score)
    print("Максимум:", max_score)
    print("Сдали:", passed)
    print("Лучший студент:", best_name)


def main():
    try:
        create_file("6.txt", 1000)
        read_scores("6.txt")

    except OSError as error:
        print("Ошибка работы с файлом:", error)

    except UnicodeDecodeError:
        print("Не удалось прочитать файл в UTF-8.")


main()