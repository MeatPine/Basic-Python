import re

text = """
Встречи состоятся 15.09.2026, 21.09.2026 и 03.10.2026.
Следующая встреча запланирована на 1.11.2026.
"""

pattern = r"\b[0-9]{2}\.[0-9]{2}\.[0-9]{4}\b"

dates = re.findall(pattern, text)

for date in dates:
    print(date)
