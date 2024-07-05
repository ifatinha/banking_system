from util.menu import menu
from database.Database import Database


def main():

    while True:
        opcao = menu()

        if opcao == "d":

            cpf = input("Informe o CPF do cliente: ")
            Database.save_deposit(cpf=cpf)

        elif opcao == "s":

            cpf = input("Informe o CPF do cliente: ")
            Database.save_withdraw(cpf=cpf)

        elif opcao == "e":

            cpf = input("Informe o CPF do cliente: ")
            Database.list_historic(cpf)

        elif opcao == "n":

            print("Informe os dados abaixo para cadatrar um novo Cliente\n")
            cpf = input("Informe o CPF do cliente: ")
            Database.save_account(cpf=cpf)

        elif opcao == "l":

            print("Listar Contas do Cliente\n")
            cpf = input("Informe o CPF do cliente: ")
            Database.list_accounts_client(cpf=cpf)

        elif opcao == "m":

            print("Contas Cadastradas")
            Database.list_bank_accounts()

        elif opcao == "c":

            print("Informe os dados abaixo para cadatrar um novo Cliente\n")
            cpf = input("CPF: ")
            Database.save_client(cpf)

        elif opcao == "p":

            Database.list_clients()

        elif opcao == "q":
            break
        else:
            print("Operação inválida, selecione novamente.")


main()
