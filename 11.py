import re

all_users = []
error_lines = []
error_users = []

with open("11.txt", encoding="utf-8") as file:
    for line in file:
        users = re.findall(r"User (\d+)", line)
        all_users.extend(users)

        if re.search(r"\bERROR\b", line):
            error_lines.append(line.rstrip("\n"))
            error_users.extend(users)

print("Все номера пользователей:", all_users)

print("Строки с ошибками:")
for line in error_lines:
    print(line)

print("Номера пользователей с ошибками:", error_users)