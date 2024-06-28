from classes.FisicalPerson import FisicalPerson


class ClientList:

    _clients = []

    @classmethod
    def add_clients(cls):
        person1 = FisicalPerson("1", "Ana Silva", "1990-05-12", "Rua A, 123, São Paulo")
        person2 = FisicalPerson(
            "2", "Carlos Souza", "1985-08-23", "Av. B, 456, Rio de Janeiro"
        )
        person3 = FisicalPerson(
            "3", "Mariana Lima", "1992-12-30", "Rua C, 789, Belo Horizonte"
        )
        person4 = FisicalPerson(
            "4", "João Mendes", "1980-01-15", "Av. D, 101, Porto Alegre"
        )
        person5 = FisicalPerson(
            "5", "Fernanda Costa", "1995-07-09", "Rua E, 202, Salvador"
        )
        person6 = FisicalPerson(
            "6", "Lucas Pereira", "1988-03-11", "Rua F, 303, Curitiba"
        )
        person7 = FisicalPerson(
            "7", "Rafaela Santos", "1991-11-25", "Av. G, 404, Recife"
        )
        person8 = FisicalPerson(
            "8", "Gabriel Martins", "1993-06-18", "Rua H, 505, Brasília"
        )
        person9 = FisicalPerson(
            "9", "Juliana Almeida", "1987-09-05", "Av. I, 606, Manaus"
        )
        person10 = FisicalPerson(
            "10", "Fernando Rodrigues", "1996-02-27", "Rua J, 707, Florianópolis"
        )

        cls._clients.append(person1)
        cls._clients.append(person2)
        cls._clients.append(person3)
        cls._clients.append(person4)
        cls._clients.append(person5)
        cls._clients.append(person6)
        cls._clients.append(person7)
        cls._clients.append(person8)
        cls._clients.append(person9)
        cls._clients.append(person10)

    @classmethod
    def export_list(cls):
        ClientList.add_clients()
        return cls._clients
