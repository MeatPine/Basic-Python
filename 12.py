import re

text = """
Контакты:
alice@example.com
bob@test.org
alice@example.com
admin@company.ru
"""

pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}\b"

emails = re.findall(pattern, text)
result = []

for email in emails:
    if email not in result:
        result.append(email)

for email in result:
    print(email)