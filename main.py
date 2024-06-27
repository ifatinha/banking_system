from util.menu import menu
from classes.Client import Client


def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            pass
        elif opcao == "s":
            pass
        elif opcao == "e":
            pass
        elif opcao == "n":
            pass
        elif opcao == "l":
            pass
        elif opcao == "c":
            pass
        elif opcao == "p":
            pass
        elif opcao == "q":
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
