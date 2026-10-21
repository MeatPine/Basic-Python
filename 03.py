import csv

total = 0
count = 0
max_score = None
best_name = ""

group_total = {}
group_count = {}

with open("3.csv", encoding="utf-8", newline="") as file:
    students = csv.DictReader(file)

    for student in students:
        name = student["name"]
        group = student["group"]
        score = int(student["score"])

        total += score
        count += 1

        if max_score is None or score > max_score:
            max_score = score
            best_name = name

        if group not in group_total:
            group_total[group] = 0
            group_count[group] = 0

        group_total[group] += score
        group_count[group] += 1

if count > 0:
    print("Средний балл всех студентов:", total / count)
    print("Лучший студент:", best_name)
    print("Его балл:", max_score)

    for group in group_total:
        average = group_total[group] / group_count[group]
        print("Группа:", group, "Средний балл:", average)
else:
    print("В файле нет студентов.")
