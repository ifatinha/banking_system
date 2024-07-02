from datetime import datetime


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
                "date": datetime.now(),
            }
        )

    def check_daily_withdrawal(self):
        now = datetime.now().strftime("%d-%m-%Y")
        transactions_day = []
        for transaction in self.transactions:
            if now == transaction["date"].strftime("%d-%m-%Y"):
                transactions_day.append(transaction)
        return transactions_day
