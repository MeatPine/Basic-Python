def read_file(path):
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print("Файл не найден.")

    except PermissionError:
        print("Нет прав доступа.")

    except IsADirectoryError:
        print("Вместо файла указана папка.")

    except UnicodeDecodeError:
        print("Не удалось прочитать текст в UTF-8.")

    except OSError as error:
        print("Ошибка операционной системы:", error)

    return None


path = input("Введите путь к файлу: ")
text = read_file(path)

if text is not None:
    print(text)