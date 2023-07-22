menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Escolha operação:  '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += '{0:17} {1:5} {2:10} {3:1}'.format("*    Deposito: ", "R$    ", f"{valor:10.2f}", "*\n")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += '{0:17} {1:5} {2:10} {3:1}'.format("*       Saque:", "R$ (-)", f"{valor:10.2f}", "*\n")
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n*************************************")
        print("*                                   *")
        print("*         EXTRATO BANCARIO          *")
        print("*                                   *")
        print("*   Sem movimentações realizadas    *" if not extrato else extrato+"*                                   *") 
        print("*                                   *")
        print("*                                   *")
        print("*************************************")
        print("*                                   *")
        print('{0:21} {1:2} {2:10} {3:1}'.format("*       Saldo:", "R$", f"{saldo:10.2f}", "*"))
        print("*                                   *")
        print("*************************************")


    elif opcao == "q":
        break

    else:
        print("Operação inválida, escolha outra opção.")