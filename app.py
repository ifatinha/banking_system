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


## Passando parametros por posição
def depositar(valor, saldo, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"+ Deposito: R$ {valor:.2f}\n"
        print("=== Depósito efetuado com sucesso! ===")
    else:
        print("@@@ Operação falhou! O valor informado é inválido! @@@")

    return saldo, extrato

## Passagem de parametros de forma nomeada
def sacar(*, valor, saldo, extrato, numero_saques, limite, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("@@@ Operação falhou! Você não tem saldo suficiente! @@@")
    elif excedeu_limite:
        print("@@@ Operação falhou! O valor de saque excede o limite! @@@")
    elif excedeu_saques:
        print("@@@ Operação falhou! Número máximo de saques excedido! @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"- Saque: RS$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque efetuado com sucesso! ===")
    else:
        print("@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato, numero_saques

## Passagem de parametros de forma posicional e nomeada
def exibir_extrato(saldo, /, *, extrato):
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

            valor_saldo = float(input("Informe quanto você quer depositar: "))
            saldo, extrato = depositar(valor_saldo, saldo, extrato)

        elif opcao == "s":
            valor_saque = float(input("Informe quanto você quer sacar: "))

            saldo, extrato, numero_saques = sacar(
                valor=valor_saque,
                saldo=saldo,
                extrato=extrato,
                numero_saques=numero_saques,
                limite=limite,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "q":
            print("Encerrando aplicação!!!")
            break
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
