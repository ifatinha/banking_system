from classes.Account import Account
from classes.Withdraw import Withdraw


class CurrentAccount(Account):

    def __init__(self, client, limit=5000, transaction_limit=10) -> None:
        super().__init__(client)
        self.__limit = limit
        self.__transaction_limit = transaction_limit

    @property
    def limit(self):
        return self.__limit

    @property
    def transaction_limit(self):
        return self.__transaction_limit

    def exceeded_limit_transactions(self):
        total = len(
            [transaction for transaction in self.historic.check_day_transactions()]
        )

        return total >= self.transaction_limit

    def withdraw(self, value):

        exceeded_limit = value > self.limit

        if exceeded_limit:
            print("@@@ Operação falhou! O valor excede o limite! @@@")
        elif self.exceeded_limit_transactions():
            print(
                "@@@ Operação falhou! Número máximo de transações diárias excedido! @@@"
            )
        else:
            return super().withdraw(value)

        return False

    def deposit(self, value):

        if self.exceeded_limit_transactions():
            print(
                "@@@ Operação falhou! Número máximo de transações diárias excedido! @@@"
            )
        elif value > 0:
            return super().deposit(value)

        return False

    def __str__(self) -> str:
        return f"""\
            Titular: {self.client.name}
            Agency: {self.agency}
            C/C: {self.number}
            Saldo: $ {self.balance}
        """
