import datetime


class Historic:

    def __init__(self) -> None:
        self.__transactions = []

    @property
    def transactions(self):
        return self.__transactions

    def addTransaction(self, transaction):
        self.transactions.append(
            {
                "type": transaction.__class__.__name__,
                "value": transaction.value,
                "date": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

    def list_historic(self):
        for t in self.transactions:
            print(t)
