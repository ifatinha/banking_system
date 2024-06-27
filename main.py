from util.menu import menu
from classes.FisicalPerson import FisicalPerson
from database.Database import Database


def main():
    clientes = []

    while True:
        opcao = menu()

        if opcao == "d":
            #deposito
            pass
        elif opcao == "s":
            #saque
            pass
        elif opcao == "e":
            ##historico
            pass
        elif opcao == "n":
            ##nova conta
            pass
        elif opcao == "l":
            ##listar contas
            pass
        elif opcao == "c":

            print("Informe os dados abaixo para cadatrar um novo Cliente\n")
            cpf = input("CPF: ")
            Database.save_client(cpf)

        elif opcao == "p":
            Database.list_clients()
        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
