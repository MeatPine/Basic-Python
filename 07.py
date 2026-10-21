from pathlib import Path

folder = Path(__file__).parent / "7"
extension = input("Введите расширение, например .py: ").strip()

if extension and not extension.startswith("."):
    extension = "." + extension

if not extension:
    print("Расширение не введено.")

elif not folder.is_dir():
    print("Папка 7 не найдена.")

else:
    try:
        for item in folder.rglob("*"):
            if item.is_file() and item.suffix == extension:
                print(item, "-", item.stat().st_size, "байт")

    except OSError as error:
        print("Ошибка:", error)
