import re
import json
import logging

logging.basicConfig(
    filename="18.log",
    level=logging.INFO,
    encoding="utf-8"
)

pattern = (
    r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} "
    r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) "
    r"([A-Z]+) (\S+) (\d{3})\s*$"
)

methods = {}
urls = {}
count_errors = 0

try:
    logging.info("Начало обработки файла")

    with open("access.log", encoding="utf-8") as file:
        for line in file:
            result = re.search(pattern, line)

            if result is None:
                logging.warning("Пропущена строка: " + line.strip())
                continue

            ip = result.group(1)
            method = result.group(2)
            url = result.group(3)
            code = int(result.group(4))

            if method not in methods:
                methods[method] = 0

            methods[method] += 1

            if url not in urls:
                urls[url] = 0

            urls[url] += 1

            if 400 <= code < 500:
                count_errors += 1

    best_url = None
    max_count = 0

    for url in urls:
        if urls[url] > max_count:
            max_count = urls[url]
            best_url = url

    data = {
        "methods": methods,
        "errors_4xx": count_errors,
        "most_popular_url": best_url,
        "url_count": max_count
    }

    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    logging.info("Обработка завершена")
    print("Результат записан в result.json")

except UnicodeDecodeError:
    logging.error("Ошибка кодировки файла")
    print("Не удалось прочитать текст в UTF-8.")

except OSError as error:
    logging.error(str(error))
    print("Ошибка работы с файлом:", error)