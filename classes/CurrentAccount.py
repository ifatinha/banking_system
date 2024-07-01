from classes.Account import Account
from classes.Withdraw import Withdraw


class CurrentAccount(Account):

    def __init__(self, client, limit=5000, withdrawal_limit=10) -> None:
        super().__init__(client)
        self.__limit = limit
        self.__withdrawal_limit = withdrawal_limit

    @property
    def limit(self):
        return self.__limit

    @property
    def withdrawal_limit(self):
        return self.__withdrawal_limit

    def withdraw(self, value):
        number_withdrawals = len(
            [
                transaction
                for transaction in self.historic.transactions
                if transaction["type"] == Withdraw.__name__
            ]
        )

        exceeded_limit = value > self.limit
        exceeded_withdrawals = number_withdrawals >= self.withdrawal_limit

        if exceeded_limit:
            print("@@@ Operação falhou! O valor excede o limite! @@@")
        elif exceeded_withdrawals:
            print("@@@ Operação falhou! Número máximo de saques excedido! @@@")
        else:
            return super().withdraw(value)

        return False

    def __str__(self) -> str:
        return f"""\
            Titular: {self.client.name}
            Agency: {self.agency}
            C/C: {self.number}
            Saldo: $ {self.balance}
        """
