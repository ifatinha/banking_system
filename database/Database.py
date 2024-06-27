from classes.FisicalPerson import FisicalPerson


class Database:

    _clients = []

    @classmethod
    def find_client(cls, *, cpf):
        for client in cls._clients:
            if client.cpf == cpf:
                return client
        return False

    @classmethod
    def save_client(cls, cpf):

        exist = Database.find_client(cpf=cpf)

        if not exist:
            name = input("Name: ")
            birthday = input("Birthday: ")
            address = input("Address: ")
            client = FisicalPerson(cpf, name, birthday, address)
            cls._clients.append(client)
            print("### Cliente cadastrado com sucesso! ###")
        else:
            print("@@@ Erro! Já existe um cliente com o código informado. @@@")

    @classmethod
    def list_clients(cls):
        if len(cls._clients) > 0:
            print("Clientes Cadastrados")
            for client in cls._clients:
                print(
                    f"""
                Client: {client.name}
                CPF: {client.cpf}
                Birthday: {client.birthday}
                Address: {client.address}
                Contas: {client.accounts}
                """
                )
        else:
            print("@@@ Nenhum Cliente Cadastrado. @@@")

    @classmethod
    def save_account(account):
        pass
