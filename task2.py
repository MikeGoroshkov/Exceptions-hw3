# Вы разрабатываете систему банковских транзакций. Необходимо написать программу, которая позволяет пользователям осуществлять переводы средств со своего банковского счета на другие счета.
# Однако, в системе существуют некоторые ограничения и возможные ошибки, которые нужно обрабатывать.
# Требования:
# При переводе средств, сумма должна быть положительной и не превышать доступный баланс на счете.
# Если сумма перевода отрицательная или равна нулю, выбрасывается исключение InvalidAmountException с сообщением "Некорректная сумма перевода".
# Если на балансе недостаточно средств для перевода, выбрасывается исключение InsufficientFundsException с сообщением "Недостаточно средств на счете".
# При успешном переводе, сумма должна списываться с текущего счета и зачисляться на целевой счет.

class InvalidAmountException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def transfer(self, target_account, amount):
        if amount <= 0:
            raise InvalidAmountException("Invalid transfer amount")
        if self.balance < amount:
            raise InsufficientFundsException("Insufficient funds in the account")
        self.balance -= amount
        target_account.balance += amount


def main():
    account1 = BankAccount(1000)
    account2 = BankAccount(500)
    try:
        amount = float(input("Enter transfer amount: "))
        account1.transfer(account2, amount)
        print(f"Transfer successful. Account 1 balance: {account1.balance}, Account 2 balance: {account2.balance}")
    except ValueError as e:
        print("Invalid input:", e)
    except InvalidAmountException as e:
        print(e)
    except InsufficientFundsException as e:
        print(e)

if __name__ == '__main__':
    main()