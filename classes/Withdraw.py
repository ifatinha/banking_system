from classes.Transaction import Transaction


class Withdraw(Transaction):

    def __init__(self, value) -> None:
        super().__init__()
        self.__value = value

    @property
    def value(self):
        return self.__value

    def register(self, account):
        success_transaction = account.withdraw(self.value)

        if success_transaction:
            account.historic.addTransaction(self)
