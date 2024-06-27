from classes.Client import Client


class FisicalPerson(Client):

    def __init__(self, cpf, name, birthday, address) -> None:
        super().__init__(address)
        self.__cpf = cpf
        self.__name = name
        self.__birthday = birthday

    @property
    def cpf(self):
        return self.__cpf

    @property
    def name(self):
        return self.__name

    @property
    def birthday(self):
        return self.__birthday
