from io import StringIO


def count_lines(stream):
    count = 0

    for line in stream:
        count += 1

    return count


with open("15.txt", encoding="utf-8") as file:
    print("Строк в файле:", count_lines(file))

with StringIO("first\nsecond\nthird") as file:
    print("Строк в StringIO:", count_lines(file))