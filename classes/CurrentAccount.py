import Account


class CurrentAccount(Account.Account):

    def __init__(self, number, client) -> None:
        super().__init__(number, client)
        self.__limit = 5000
        self.__withdrawal_limit = 5

    @property
    def limit(self):
        return self.__limit

    @property
    def withdraw_limit(self):
        return self.__withdrawal_limit
