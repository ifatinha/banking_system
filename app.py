import os

def menu():
    menu = """ 
    ################ MENU ################
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [n] Nova Conta
    [l] Listar Contas
    [c] Novo Cliente
    [p] Listar Clientes
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


def verificar_cliente(*, codigo, clientes):
    for cliente in clientes:
        if(cliente["codigo"] == codigo):
            return cliente
    return False

## Cadastrar novo cliente
def cadastrar_cliente(clientes):
    codigo = input("Código: ")
    
    if(verificar_cliente(codigo=codigo, clientes=clientes)):
        
        print('@@@ Erro! Já existe um cliente com o código informado. @@@')
    
    else:
        nome = input("Nome: ")
        cliente = {
            "codigo": codigo,
            "nome": nome
        }
        
        clientes.append(cliente)
        cliente = {}
        print("### Cliente cadastrado com sucesso! ###")
    
    return clientes

def listar_clientes(clientes):
    
    if(len(clientes) > 0):
        print("Clientes Cadastrados".center(40, "#").upper()+"\n")

        for cliente in clientes:
            print(f"Código: {cliente["codigo"]}")
            print(f"Cliente: {cliente["nome"]}\n")
              
    else:
        print("\n@@@ Nenhum Cliente Cadastrado @@@".upper())

def cadastrar_conta(*, agencia, numero_conta, clientes, contas):
    codigo_cliente = input("Informe o código do cliente: ")
    cliente = verificar_cliente(codigo=codigo_cliente, clientes=clientes)
    
    if cliente:
        conta = {
            "agencia": agencia,
            "numero_conta":numero_conta,
            "cliente": cliente,
            "ativo": True
        }
        
        if conta:
            
            contas.append(conta)
            print("### Conta cadastrada com sucesso. ###")
    
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")    

    return contas

def listar_contas(contas):
    
    if(len(contas) > 0):
        print("Contas Cadastradas".center(40, "#").upper()+"\n")

        for conta in contas:
            situacao = "Ativa" if conta["ativo"] else "Desativada"
            print(f"Agência: {conta["agencia"]}")
            print(f"Número: {conta["numero_conta"]}")
            print(f"Titular: {conta["cliente"]["codigo"]} - {conta["cliente"]["nome"]}")
            print(f"Situação: {situacao}\n")
            print("=" * 50)

    else:
        print("\n@@@ Não existem contas Cadastrada @@@".upper())
    
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
            
        elif opcao == "n":
            
            contas = cadastrar_conta(
                agencia=AGENCIA, 
                numero_conta=numero_conta, 
                clientes=clientes, 
                contas=contas)
            numero_conta += 1
        
        elif opcao == "l":
            
            listar_contas(contas=contas)
            
        elif opcao == "c":
            
            clientes = cadastrar_cliente(clientes)
            
        elif opcao == "p":
            
            listar_clientes(clientes)
            
        elif opcao == "q":
            
            print("Encerrando aplicação!!!")
            break
        
        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
