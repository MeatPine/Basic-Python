from pathlib import Path


folder = Path(input("Введите путь к папке: ").strip())
extension = input("Введите расширение, например .py: ").strip()

if extension and not extension.startswith("."):
    extension = "." + extension

try:
    if not extension:
        print("Расширение не введено.")

    elif not folder.is_dir():
        print("Папка не найдена.")

    else:
        found = False

        for item in folder.rglob("*"):
            if item.is_file() and item.suffix == extension:
                print(item, "-", item.stat().st_size, "байт")
                found = True

        if not found:
            print("Файлы с таким расширением не найдены.")

except OSError as error:
    print("Ошибка работы с папкой:", error)
