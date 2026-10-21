import re

text = "Это   строка    с     большим    количеством   пробелов."

text = re.sub(r" {2,}", " ", text)
print(text)

text = "   Текст   с   пробелами   "

text = re.sub(r" {2,}", " ", text)
text = text.strip()

print(text)