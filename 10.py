class BankError(Exception):
    pass


class InvalidAmountError(BankError):
    pass


class InsufficientFundsError(BankError):
    pass


class AccountBlockedError(BankError):
    pass


def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма должна быть больше нуля.")

    if amount > balance:
        raise InsufficientFundsError("Недостаточно денег.")

    return balance - amount


balance = 1000

try:
    amount = float(input("Сколько снять: "))
    balance = withdraw(balance, amount)
    print("Осталось:", balance)

except ValueError:
    print("Введите число.")

except BankError as error:
    print(error)