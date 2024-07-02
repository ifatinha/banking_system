from classes.FisicalPerson import FisicalPerson


class ClientList:

    _clients = []

    @classmethod
    def add_clients(cls):
        cls._clients.append(
            FisicalPerson("1", "Ana Silva", "1990-05-12", "Rua A, 123, Sousa")
        )
        cls._clients.append(
            FisicalPerson("2", "Carlos Souza", "1985-08-23", "Av. B, 456, Emas")
        )
        cls._clients.append(
            FisicalPerson("3", "Mariana Lima", "1992-12-30", "Rua C, 789, Itaporanga")
        )
        cls._clients.append(
            FisicalPerson("4", "João Mendes", "1980-01-15", "Av. D, 101, Cajazeiras")
        )
        cls._clients.append(
            FisicalPerson("5", "Fernanda Costa", "1995-07-09", "Rua E, 202, Cajazeiras")
        )
        cls._clients.append(
            FisicalPerson("6", "Lucas Pereira", "1988-03-11", "Rua F, 303, Curitiba")
        )
        cls._clients.append(
            FisicalPerson("7", "Rafaela Santos", "1991-11-25", "Av. G, 404, Recife")
        )
        cls._clients.append(
            FisicalPerson("8", "Gabriel Martins", "1993-06-18", "Rua H, 505, Brasília")
        )
        cls._clients.append(
            FisicalPerson("9", "Juliana Almeida", "1987-09-05", "Av. I, 606, Manaus")
        )
        cls._clients.append(
            FisicalPerson("10", "Fernando Rodrigues", "1996-02-27", "Rua J, 707, Viana")
        )

    @classmethod
    def export_list(cls):
        ClientList.add_clients()
        return cls._clients
