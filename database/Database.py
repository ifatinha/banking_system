from classes.FisicalPerson import FisicalPerson
from classes.CurrentAccount import CurrentAccount
from classes.Deposit import Deposit
from classes.Withdraw import Withdraw
from database.ClientsList import ClientList
from util.Decoratores import log_operations
from util.Generators import report_generator
from util.AccountIterator import AccountIterator


class Database:

    _clients = ClientList.export_list()

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
            print(
                """
            ### Clientes Cadastrados ### 
            """
            )
            for client in cls._clients:
                print(client)
        else:
            print("@@@ Nenhum Cliente Cadastrado. @@@")

    @classmethod
    @log_operations("Created Account")
    def save_account(cls, cpf):
        client = Database.find_client(cpf=cpf)

        if client:
            client.create_account(CurrentAccount(client))
            print("### Conta cadastrada com sucesso. ###")
            return True
        else:
            print(
                "\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@"
            )
            return False

    @classmethod
    def list_accounts_client(cls, cpf):
        client = Database.find_client(cpf=cpf)

        if client:
            if len(client.accounts) > 0:
                print(f"Contas do Titular {client.name} ")
                for account in client.accounts:
                    print(account)
            else:
                print(
                    f"\n@@@ Não existem contas Cadastrada para o titular {client.name} @@@".upper()
                )

        else:
            print(
                "\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@"
            )

    @classmethod
    def list_bank_accounts(cls):
        for client in cls._clients:
            accounts = AccountIterator(client.accounts)
            for account in accounts:
                print(account)

    @classmethod
    def find_account(cls, accounts, number_account):
        return [a for a in accounts if a.number == number_account]

    @classmethod
    @log_operations("Deposit")
    def save_deposit(cls, cpf):
        client = Database.find_client(cpf=cpf)

        if client:
            number_account = int(input("Digite o número da conta: "))
            account = Database.find_account(client.accounts, number_account)

            if len(account) > 0:
                value = float(input("Valor do Deposito: "))
                depoist = Deposit(value)
                return depoist.register(account[0])
            else:
                print("\n@@@ Conta não encontrada, fluxo de operação encerrado! @@@")
        else:
            print("\n@@@ Cliente não encontrado, fluxo de operação encerrado! @@@")

        return False

    @classmethod
    @log_operations("Withdraw")
    def save_withdraw(cls, cpf):
        client = Database.find_client(cpf=cpf)

        if client:
            number_account = int(input("Digite o número da conta: "))
            account = Database.find_account(client.accounts, number_account)

            if len(account) > 0:
                value = float(input("Valor do Saque: "))
                withdraw = Withdraw(value)
                return withdraw.register(account[0])
            else:
                print("\n@@@ Conta não encontrada, fluxo de operação encerrado! @@@")
        else:
            print("\n@@@ Cliente não encontrado, fluxo de operação encerrado! @@@")

        return False

    @classmethod
    @log_operations("Extract")
    def list_historic(cls, cpf):
        client = Database.find_client(cpf=cpf)

        if client:
            number_account = int(input("Digite o número da conta: "))
            account = Database.find_account(client.accounts, number_account)

            if len(account) > 0:
                type_extract = int(
                    input(
                        "Qual tipo de extrado você deseja: \n 1 - Deposit, 2 - Withdraw, 3 - Completed: "
                    )
                )
                report = report_generator(
                    account[0].historic.transactions, type_extract
                )

                print("=== Bank Statement ===")
                for i in report:
                    print(
                        f"""
                    Type: {i["type"]}
                    Value: {i["value"]}
                    Date: {i["date"]}
                    """
                    )
            else:
                print("\n@@@ Conta não encontrada, fluxo de operação encerrado! @@@")
        else:
            print("\n@@@ Cliente não encontrado, fluxo de operação encerrado! @@@")
