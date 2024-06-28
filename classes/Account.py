from classes.Historic import Historic
import random


class Account:

    def __init__(self, client) -> None:
        self.__balance = float()
        self.__number = random.randint(1, 100)
        self.__client = client
        self.__agency = "0001"
        self.__historic = Historic()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def number(self):
        return self.__number

    @property
    def client(self):
        return self.__client

    @property
    def agency(self):
        return self.__agency

    @property
    def historic(self):
        return self.__historic

    @classmethod
    def new_account(cls, number, client):
        return cls(number, client)

    def withdraw(self, value):
        exceeded_balance = value > self.balance

        if exceeded_balance:
            print("@@@ Operação falhou! Você não tem saldo suficiente! @@@")
        elif value > 0:
            self.balance -= value
            print("\n=== Saque efetuado com sucesso! ===")
            return True
        else:
            print("@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def deposit(self, value):
        if value > 0:
            self.balance += value
            print("=== Depósito efetuado com sucesso! ===")
        else:
            print("@@@ Operação falhou! O valor informado é inválido! @@@")
            return False

        return True
