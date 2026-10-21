count_lines = 0
count_words = 0
count_chars = 0
max_length = 0

with open("1.txt", encoding="utf-8") as file:
    for line in file:
        count_lines += 1
        count_words += len(line.split())
        count_chars += len(line)

        length = len(line.rstrip("\n"))

        if length > max_length:
            max_length = length

print("Количество строк:", count_lines)
print("Количество слов:", count_words)
print("Количество символов:", count_chars)
print("Самая длинная строка:", max_length)