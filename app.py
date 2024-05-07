menu = """ 

   [d] Depositar
   [s] Sacar
   [e] Extrato
   [q] Sair

=> """

saldo = 0
limite = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valorDeposito = float(input("Informe quanto você quer depositar: "))

        if valorDeposito > 0:
            saldo += valorDeposito
            print("Operação efetuada com sucesso!")
            extrato += f"Deposito: R$ {valorDeposito:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido!")
    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valorSaque = float(input("Informe quanto você quer sacar: "))
            if valorSaque > 0:
                if valorSaque <= 1000:
                    if valorSaque <= saldo:
                        saldo -= valorSaque
                        numero_saques += 1
                        print("Operação efetuada com sucesso!")
                        extrato += f"Saque: R$ {valorSaque:.2f}\n"
                        extrato += f"Saques diários: {numero_saques}\n"
                    else:
                        print(f"Operação falhou! Você não tem saldo suficiente!")
                else:
                    print("Operação falhou! O valor do saque excede o limite!")
            else:
                print("Operação falhou! Valor inválido!")
        else:
            print("Operação falhou! Número máximo de saques excedido!!")
    elif opcao == "e":
        print(" Extrato ".upper().center(40, "#"))
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#".center(40, "#"))
    elif opcao == "q":
        print("Saindo!!!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
