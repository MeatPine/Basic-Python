import csv

with open("products.csv", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    with open(
        "expensive.csv", "w", encoding="utf-8", newline=""
    ) as new_file:
        writer = csv.DictWriter(
            new_file,
            fieldnames=reader.fieldnames
        )

        writer.writeheader()

        for product in reader:
            price = float(product["price"])

            if price > 100:
                writer.writerow(product)

print("Готово.")
