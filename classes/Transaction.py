from abc import ABC, abstractmethod


class Transaction(ABC):

    @abstractmethod
    def register(self, account):
        pass
