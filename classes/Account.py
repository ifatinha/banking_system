import Historic


class Account:

    def __init__(self, number, client) -> None:
        self.__number = number
        self.__agency = "0001"
        self.__client = client
        self.__balance = 0
        self.__historic = Historic.Historic()

    def __str__(self) -> str:
        return f"Conta {self.__number} - {self.__agency}"

    @property
    def balance(self):
        return self.__balance

    @property
    def historic(self):
        return self.__historic

    def new_account(number, client):
        return Account(number, client)

    def withdraw(self, value):
        if value <= self.balance() and value > 0:
            self.__balance -= value
            return True
        else:
            return False

    def deposit(self, value):
        if value > 0:
            self.__balance += value
            return True
        else:
            return False
