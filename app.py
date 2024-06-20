menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite_saque_valor = 500
LIMITE_SAQUES = 3
extrato = """
========== Extrato ==========

"""
quantidade_saques = 0

while True:

    opcao = input(menu).lower()

    if opcao == "d":

        deposito = float(input("Digite o valor do depósito:"))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: {deposito:.2f}\n"
        else: 
            print("valor invalido")

    elif opcao == "s":
        
        if quantidade_saques == LIMITE_SAQUES:
            print("Voce atingiu a quantidade máxima de saques diarios")
        else:
            valor_saque = float(input("Digite o valor que deseja sacar: "))
            if valor_saque > saldo:
                print("Voce nao possui saldo suficiente para sacar")
            elif valor_saque > limite_saque_valor:
                print("Este valor excede o limite de valor do saque")
            else: 
                saldo -= valor_saque
                quantidade_saques += 1
                extrato += f"Saque: {valor_saque:.2f}\n"
                print(f"Voce sacou R${valor_saque:.2f}. Seu novo saldo é R${saldo:.2f}")


    elif opcao == "e":
        print(extrato)
        print(f"Saldo: {saldo}")
    
    elif opcao == "q":
        break

    else: 
        print("Opcao invalida, escolha novamente:")
    
    
