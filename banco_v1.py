# Variáveis
menu = ""

balanca = 300
operacoes = []
deposito = 0
saque = 0
nsaques = 0
LIMITE_SAQUES = 3

#Menu

print("Bem vindo ao sistema bancário VGOmes!\n")

# Operações
while menu != 0:
    menu = int(input("""OPERAÇÃO: 
            1 - Depósito
            2 - Saque
            3 - Extrato
            0 - Sair
      """))
    
    if menu == 1:
        deposito = float(input("Digite o valor a ser depositado, em R$: "))
        if deposito > 0:
            balanca += deposito
            operacoes.append(f"Deposito: + {deposito:.2f} R$")
            print(f"Depósito no valor de R$ {deposito:.2f} realizado. \n")

        else:
            print("Digite um valor válido. \n")

    elif menu == 2:
        if nsaques < LIMITE_SAQUES:
            saque = float(input("Digite o valor a ser sacado, em R$: "))
            if saque <= balanca and saque <= 500:
                balanca -= saque
                nsaques += 1
                operacoes.append(f"Saque: - {saque:.2f} R$")
                print(f"Saque no valor de R$ {saque:.2f} realizado. \n")
            
            elif saque > balanca:
                print("Saldo insuficiente para realizar a operação! Tente novamente.\n")
            
            elif saque > 500:
                print("Limite de saque excedido! O limite é 500.00 R$\n")

            else:
                print("Digite um valor válido. \n")
        else:
            print("Limite de saques diários atingido! Tente novamente amanhã. \n")

    elif menu == 3:
        print("Extrato".center(18, "-"))

        print("Operações: ")
        if len(operacoes) == 0:
            print("Nenhuma operação realizada. \n") 
        else:
            for nop, operacao in enumerate(operacoes):
                print(f"{nop+1}. {operacao}")

        print(f"Saldo: {balanca:.2f} R$ \n")

    elif menu == 0:
        break

    else:
        print("Digite um valor válido!")

print("Aplicação finalizada.")