# Variáveis

menu = 0

balanca = 300
operacoes = []
deposito = 0
saque = 0
nsaques = 0
LIMITE_SAQUES = 3

#Menu

print("Bem vindo ao sistema bancário VGOmes!\n")

# Operações
while menu != 4:
    menu = int(input("""OPERAÇÃO: 
            1 - Depósito
            2 - Saque
            3 - Extrato
            4 - Sair
      """))
    
    if menu == 1:
        deposito = float(input("Digite o valor a ser depositado, em R$: "))
        if deposito > 0:
            balanca += deposito
            print(f"Depósito no valor de R$ {deposito:.2f} realizado. \n")
            operacoes.append(deposito)

    elif menu == 2:
        if nsaques < LIMITE_SAQUES:
            saque = float(input("Digite o valor a ser sacado, em R$: "))
            if saque <= balanca:
                balanca -= saque
                nsaques += 1
                print(f"Saque no valor de R$ {saque:.2f} realizado. \n")
                operacoes.append(saque*(-1))
        else:
            print("Limite de saques diários atingido! Tente novamente amanhã. \n")

    elif menu == 3:
        print("Extrato".center(18, "-"))

        print("Ações: ")
        for operacao in operacoes:
            if operacao > 0:
                print(f"{(operacoes.index(operacao))+1}. Depósito = + {operacao:.2f} R$")
            else:
                print(f"{(operacoes.index(operacao))+1}. Saque = {operacao:.2f} R$")

        print(f"Saldo: {balanca:.2f} R$ \n")

    elif menu == 4:
        break

    else:
        print("Digite um valor válido!")

print("Aplicação finalizada.")