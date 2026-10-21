from faker import Faker


def create_file(path, count):
    fake = Faker("ru_RU")

    with open(path, "w", encoding="utf-8") as file:
        for i in range(count):
            name = fake.first_name()
            city = fake.city()
            words = " ".join(fake.words(nb=5))

            file.write(f"{name}, город {city}: {words}!\n")


def count_words(path):
    counts = {}

    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.lower()

            for sign in ".,!?:;":
                line = line.replace(sign, " ")

            for word in line.split():
                if word not in counts:
                    counts[word] = 0

                counts[word] += 1

    return counts


def show_top(counts):
    words = counts.copy()

    for i in range(10):
        if len(words) == 0:
            break

        best = ""
        max_count = 0

        for word in words:
            if words[word] > max_count:
                best = word
                max_count = words[word]

        print(best, "-", max_count)

        del words[best]


def main():
    try:
        create_file("7.txt", 10000)
        counts = count_words("7.txt")

        if len(counts) == 0:
            print("В файле нет слов.")
        else:
            show_top(counts)

    except OSError as error:
        print("Ошибка работы с файлом:", error)

    except UnicodeDecodeError:
        print("Не удалось прочитать файл в UTF-8.")


main()