import Transaction


class Deposit(Transaction.Transaction):

    def __init__(self, value) -> None:
        super().__init__()
        self.__value = value

    @property
    def value(self):
        return self.__value

    def register(self, account):
        account.deposit(self.value)
