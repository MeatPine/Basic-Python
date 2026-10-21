total = 0
count = 0
min_number = None
max_number = None

with open("17.txt", encoding="utf-8") as file:
    for line in file:
        number = int(line)

        total += number
        count += 1

        if min_number is None or number < min_number:
            min_number = number

        if max_number is None or number > max_number:
            max_number = number

print("Сумма:", total)
print("Количество:", count)

if count > 0:
    print("Минимум:", min_number)
    print("Максимум:", max_number)
    print("Среднее:", total / count)
else:
    print("Файл пуст.")
