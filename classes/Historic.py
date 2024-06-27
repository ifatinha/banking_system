class Historic:

    def __init__(self) -> None:
        self.__historics = []

    @property
    def historics(self):
        return self.__historics

    def addTransaction(self, transaction):
        self.historics.append(transaction)
