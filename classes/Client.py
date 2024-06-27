class Client:

    def __init__(self, address) -> None:
        self.address = address
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def create_account(self, account):
        self.accounts.append(account)
