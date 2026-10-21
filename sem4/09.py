def parse_number(value):
    return float(value)


value = input("Введите число: ")

try:
    number = parse_number(value)
    print("Ваше число:", number)

except ValueError:
    print("Невозможно преобразовать строку в число.")
