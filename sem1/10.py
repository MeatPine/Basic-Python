def log_command(function):
    def wrapper(*args, **kwargs):
        print("Начало выполнения команды.")

        try:
            result = function(*args, **kwargs)
        except ValueError as error:
            print("Ошибка:", error)
            raise

        print("Команда выполнена.")
        return result

    return wrapper


class Command:
    def execute(self, value, number):
        pass


class AddCommand(Command):
    def execute(self, value, number):
        return value + number


class MultiplyCommand(Command):
    def execute(self, value, number):
        return value * number


class SubtractCommand(Command):
    def execute(self, value, number):
        return value - number


class DivideCommand(Command):
    def execute(self, value, number):
        if number == 0:
            raise ValueError("Нельзя делить на ноль.")

        return value / number


class CommandProcessor:
    def __init__(self):
        self.value = 0
        self.history = []

        self.commands = {
            "add": AddCommand(),
            "multiply": MultiplyCommand(),
            "subtract": SubtractCommand(),
            "divide": DivideCommand()
        }

    @log_command
    def execute_command(self, name, number):
        command = self.commands[name]

        result = command.execute(self.value, number)

        self.value = result
        self.history.append(f"{name} {number} -> {result}")

        return result

    def show_history(self):
        if len(self.history) == 0:
            print("История пуста.")
        else:
            for line in self.history:
                print(line)

    def run(self):
        print("Начальное значение:", self.value)
        print("Команды: add, multiply, subtract, divide")
        print("Также: history и exit")

        while True:
            text = input("> ")
            parts = text.split()

            if len(parts) == 0:
                print("Введите команду.")
                continue

            if parts == ["exit"]:
                break

            if parts == ["history"]:
                self.show_history()
                continue

            name = parts[0]

            if name in ["history", "exit"]:
                print("Эта команда вводится без числа.")
                continue

            if name not in self.commands:
                print("Неизвестная команда.")
                continue

            if len(parts) != 2:
                print("Нужно ввести команду и одно число.")
                continue

            try:
                number = float(parts[1])
            except ValueError:
                print("После команды должно быть число.")
                continue

            try:
                result = self.execute_command(name, number)
                print("Результат:", result)
            except ValueError:
                continue


def main():
    processor = CommandProcessor()
    processor.run()


main()