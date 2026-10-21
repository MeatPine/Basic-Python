def find_string():
    best = None
    max_count = 0

    while True:
        text = input("Введите строку или STOP: ")

        if text == "STOP":
            break

        count = len(set(text.lower()))

        if best is None or count > max_count:
            best = text
            max_count = count

    return best, max_count


def main():
    text, count = find_string()

    if text is None:
        print("Ни одной строки не введено.")
    else:
        print("Строка:", text)
        print("Различных символов:", count)


main()