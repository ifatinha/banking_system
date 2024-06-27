import Account
import Withdraw


class CurrentAccount(Account.Account):

    def __init__(self, number, client, limit=5000, withdrawal_limit=5) -> None:
        super().__init__(number, client)
        self.__limit = limit
        self.__withdrawal_limit = withdrawal_limit

    @property
    def limit(self):
        return self.__limit

    @property
    def withdraw_limit(self):
        return self.__withdrawal_limit

    def withdraw(self, value):
        number_withdrawals = len(
            [
                transaction
                for transaction in self.historic.transactions
                if transaction["type"] == Withdraw.Withdraw.__name__
            ]
        )

        exceeded_limit = value > self.withdrawal_limit
        exceeded_withdrawals = number_withdrawals >= self.withdraw_limit

        if exceeded_limit:
            print("@@@ Operação falhou! O valor de saque excede o limite! @@@")
        elif exceeded_withdrawals:
            print("@@@ Operação falhou! Número máximo de saques excedido! @@@")
        else:
            return super().withdraw(value)

        return False

    def __str__(self) -> str:
        return f"""\
            Agency: {self.agency}
            C/C:\t\t{self.number}
            Titular: {self.client.name}
        """
