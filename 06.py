from pathlib import Path

folder = Path(__file__).parent / "6"

count_files = 0
count_folders = 0
total_size = 0

if folder.is_dir():
    for item in folder.iterdir():
        if item.is_file():
            count_files += 1
            total_size += item.stat().st_size

            if item.suffix == ".py":
                print("Файл Python:", item.name)

        elif item.is_dir():
            count_folders += 1

    print("Файлов:", count_files)
    print("Папок:", count_folders)
    print("Размер файлов:", total_size, "байт")
else:
    print("Папка 6 не найдена.")
