min_number = None
max_number = None
total = 0
count = 0

with open("2.txt", encoding="utf-8") as file:
    for line in file:
        try:
            number = int(line)
        except ValueError:
            print("Не число:", line.strip())
            continue

        if min_number is None or number < min_number:
            min_number = number

        if max_number is None or number > max_number:
            max_number = number

        total += number
        count += 1

with open("result.txt", "w", encoding="utf-8") as file:
    if count > 0:
        file.write(f"Минимум: {min_number}\n")
        file.write(f"Максимум: {max_number}\n")
        file.write(f"Среднее: {total / count}\n")
    else:
        file.write("В файле нет чисел.\n")