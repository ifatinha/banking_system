from classes.Transaction import Transaction
from util.Decoratores import log_operations


class Withdraw(Transaction):

    def __init__(self, value) -> None:
        super().__init__()
        self.__value = value

    @property
    def value(self):
        return self.__value

    @log_operations("Withdraw")
    def register(self, account):
        success_transaction = account.withdraw(self.value)

        if success_transaction:
            account.historic.addTransaction(self)
