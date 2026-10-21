import re

counts = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

error_users = []

pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} (INFO|WARNING|ERROR) User (\d+)\b"

with open("logs.txt", encoding="utf-8") as file:
    for line in file:
        result = re.search(pattern, line)

        if result:
            level = result.group(1)
            user = result.group(2)

            counts[level] += 1

            if level == "ERROR":
                if user not in error_users:
                    error_users.append(user)

for level in counts:
    print(f"{level}: {counts[level]}")

print("Пользователи с ошибками:", error_users)
