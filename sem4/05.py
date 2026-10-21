import json

with open("students.json", encoding="utf-8") as file:
    students = json.load(file)

best_student = None

for student in students:
    student["passed"] = student["score"] >= 60

    if best_student is None:
        best_student = student
    elif student["score"] > best_student["score"]:
        best_student = student

if best_student is not None:
    print("Лучший студент:", best_student["name"])
    print("Его балл:", best_student["score"])
else:
    print("Список студентов пуст.")

with open("new_students.json", "w", encoding="utf-8") as file:
    json.dump(students, file, ensure_ascii=False, indent=4)
