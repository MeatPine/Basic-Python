class log_operation:
    def __init__(self, path, name):
        self.path = path
        self.name = name

    def __enter__(self):
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(f"START: {self.name}\n")

        return self

    def __exit__(self, error_type, error, traceback):
        with open(self.path, "a", encoding="utf-8") as file:
            if error_type is None:
                file.write(f"END: {self.name}\n")
            else:
                file.write(f"ERROR: {self.name}\n")

        return False


with log_operation("operation.log", "Data processing"):
    numbers = [1, 2, 3]
    print(sum(numbers))