""" Sistema Bancário VGOMES - V2 """

# Funções
def sacar(*, valor, saldo, nsaques, limsaques, extrato):
    if nsaques < limsaques:
        
        if valor <= saldo and valor <= 500:
            saldo -= valor
            nsaques += 1
            extrato.append(f"Saque: + {valor:.2f} R$")
            print(f"Saque no valor de R$ {valor:.2f} realizado. \n")
        
        elif valor > saldo:
            print("Saldo insuficiente para realizar a operação! Tente novamente.\n")
        
        elif valor > 500:
            print("Limite de saque excedido! O limite é 500.00 R$\n")

        else:
            print("Digite um valor válido. \n")
    else:
        print("Limite de saques diários atingido! Tente novamente amanhã. \n")

    return saldo, nsaques, extrato

def depositar(valor, saldo, extrato):

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: - {valor:.2f} R$")
        print(f"Depósito no valor de R$ {valor:.2f} realizado. \n")

    else:
        print("Digite um valor válido. \n")

    return saldo, extrato

def vExtrato(saldo, extrato):
    print("Extrato".center(18, "-"))

    print("Operações: ")
    if len(extrato) == 0:
        print("Nenhuma operação realizada. \n") 
    else:
        for nop, operacao in enumerate(extrato):
            print(f"{nop+1}. {operacao}")

    print(f"Saldo: {saldo:.2f} R$ \n")

def criarUsuario(clientes):
    cpf = input("Digite seu cpf: ")
    used = [cpf for cliente in clientes if cliente["cpf"] == cpf]
    nome = input("Digite seu nome: ")
    dataNasc = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")

    if used:
        print("CPF já cadastrado no sistema. Tente outro CPF!")
    else:
        # clientes é uma lista de dicionários
        clientes.append({"cpf": cpf, "nome": nome, "dataNasc": dataNasc, "endereco": endereco})

    return clientes

def listarUsuario(clientes):
    for ncli, cliente in enumerate(clientes):
        print("\nCliente", (ncli+1))
        print("CPF:", cliente["cpf"])
        print("Nome:", cliente["nome"])
        print("Data nascimento:", cliente["dataNasc"])
        print("Endereço: ", cliente["endereco"])

def criarCC(contas, ncontas, agencia, clientes):
    cpfcli = input("Entre com o cpf do cliente cuja conta vai pertencer: ")
    cpf = [cpfcli for cliente in clientes if cliente["cpf"] == cpfcli]

    contas.append({"n_conta": (ncontas+1), "agencia": agencia, "cliente": cpfcli})
    print("Conta cadastrada com sucesso!")

    return contas, ncontas

def listarCC(contas):
    cpfcli = input("CPF do cliente: ")

    for conta in contas:
        if conta['cliente'] == cpfcli :
            print(f"\nContas do cliente de CPF {conta['cliente']}:" )
            print("Número CC: ", conta["n_conta"])
            print("Agência: ", conta["agencia"])
        else:
            print("Cliente não encontrado!")

#MENU
def opMenu():  
    op = int(input("""\nOPERAÇÃO: 
                1 - Depósito
                2 - Saque
                3 - Extrato
                4 - Criar usuário
                5 - Listar usuários
                6 - Criar conta corrente (CC)
                7 - Lista CC por usuário
                0 - Sair
        """))
    
    return op    

def main():
    
    usuarios = []
    contasCC = []
    numcontas = 0

    balanca = 300
    deposito = 0
    saque = 0
    nsaques = 0

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    operacoes = []
    menu = 8

    while menu != 0:
        menu = opMenu()

        if menu == 1:
            deposito = float(input("Digite o valor a ser depositado, em R$: "))
            balanca, operacoes = depositar(deposito, balanca, operacoes)       

        elif menu == 2:
            saque = float(input("Digite o valor a ser sacado, em R$: "))
            balanca, nsaques, operacoes = sacar(valor=saque, saldo=balanca, nsaques=nsaques, limsaques=LIMITE_SAQUES, extrato=operacoes)

        elif menu == 3:
            vExtrato(balanca, extrato=operacoes)

        elif menu == 4:
            usuarios = criarUsuario(usuarios)
            
        elif menu == 5:
            listarUsuario(usuarios)

        elif menu == 6:
            contasCC, numcontas = criarCC(contasCC, numcontas, AGENCIA, usuarios)
            
        elif menu == 7:
            listarCC(contasCC)

        elif menu == 0:
            break

        else:
            print("Digite um valor válido!")
       
    print("Aplicação finalizada.")

main()