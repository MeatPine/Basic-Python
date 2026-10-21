class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным.")

        self.owner = owner
        self.__balance = balance
        self.history = [f"Открытие счета: {balance}"]

    def deposit(self, amount):
        if amount <= 0:
            self.history.append(f"Отказ в пополнении: {amount}")
            raise ValueError("Сумма должна быть больше нуля.")

        self.__balance += amount
        self.history.append(f"Пополнение: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            self.history.append(f"Отказ в снятии: {amount}")
            raise ValueError("Сумма должна быть больше нуля.")

        if amount > self.__balance:
            self.history.append(f"Отказ в снятии: {amount}")
            raise ValueError("Недостаточно денег.")

        self.__balance -= amount
        self.history.append(f"Снятие: {amount}")

    def get_balance(self):
        return self.__balance

    def get_history(self):
        return self.history.copy()


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, minimum):
        if minimum < 0 or minimum > balance:
            raise ValueError("Неверный минимальный остаток.")

        super().__init__(owner, balance)
        self.minimum = minimum

    def withdraw(self, amount):
        if self.get_balance() - amount < self.minimum:
            self.history.append(f"Отказ в снятии: {amount}")
            raise ValueError("Нельзя нарушать минимальный остаток.")

        super().withdraw(amount)


class CreditAccount(BankAccount):
    def __init__(self, owner, balance, limit):
        if limit <= 0:
            raise ValueError("Лимит должен быть больше нуля.")

        super().__init__(owner, balance)
        self.limit = limit

    def withdraw(self, amount):
        if amount > self.limit:
            self.history.append(f"Отказ в снятии: {amount}")
            raise ValueError("Превышен лимит снятия.")

        super().withdraw(amount)


def main():
    accounts = [
        BankAccount("Иван", 1000),
        SavingsAccount("Петр", 1000, 500),
        CreditAccount("Анна", 1000, 300)
    ]

    for account in accounts:
        print("\nВладелец:", account.owner)

        account.deposit(100)

        for amount in [700, 200, -10]:
            try:
                account.withdraw(amount)
                print("Снято:", amount)
            except ValueError as error:
                print(error)

        print("Баланс:", account.get_balance())

        for operation in account.get_history():
            print(operation)


main()