def menu():
    menu = """ 
    ################ MENU ################
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair

    => """

    return input(menu)


def deposito(valor, saldo):
    saldo += valor
    print("Operação efetuada com sucesso!")
    return saldo


def saque(valor, saldo):
    saldo -= valor
    print("Operação efetuada com sucesso!")
    return saldo


def atualizar_numero_saques(numero_saques):
    numero_saques += 1
    return numero_saques


def salvar_extrato(msg):
    return msg


def mostrar_extrato(saldo, extrato):
    print(" Extrato ".upper().center(40, "#"))
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("#".center(40, "#"))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 1000
    extrato = ""
    numero_saques = 0
    clientes = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valorDeposito = float(input("Informe quanto você quer depositar: "))

            if valorDeposito > 0:
                saldo = deposito(valorDeposito, saldo)
                extrato += salvar_extrato(f"Deposito: R$ {valorDeposito:.2f}\n")
            else:
                print("Operação falhou! O valor informado é inválido!")
        elif opcao == "s":
            if numero_saques < LIMITE_SAQUES:
                valorSaque = float(input("Informe quanto você quer sacar: "))
                if valorSaque > 0:
                    if valorSaque <= 1000:
                        if valorSaque <= saldo:
                            saldo = saque(valorSaque, saldo)
                            numero_saques = atualizar_numero_saques(numero_saques)
                            extrato += salvar_extrato(f"Saque: R$ {valorSaque:.2f}\n")
                            extrato += salvar_extrato(
                                f"Saques diários: {numero_saques}\n"
                            )
                        else:
                            print(f"Operação falhou! Você não tem saldo suficiente!")
                    else:
                        print("Operação falhou! O valor do saque excede o limite!")
                else:
                    print("Operação falhou! Valor inválido!")
            else:
                print("Operação falhou! Número máximo de saques excedido!!")
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            print("Saindo!!!")
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
