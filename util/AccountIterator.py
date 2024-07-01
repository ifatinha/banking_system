class AccountIterator:

    def __init__(self, lista) -> None:
        self.lista = lista
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lista):
            account = self.lista[self.index]
            self.index += 1
            return account
        else:
            raise StopIteration
