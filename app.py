import textwrap

def main():
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: R$"))
            
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: R$"))

            saldo, extrato = saque(saldo= saldo,
                                   limite= limite,
                                   extrato= extrato,
                                   quant_saques=numero_saques,
                                   limite_saques=LIMITE_SAQUES                     
                                   )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
     

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)


def menu():
    menu = """

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito R${valor:.2f}"
        print(f"Depósito no valor de R${valor}")
    else: 
        print("Operacao falhou, o valor informado é inválido")
    return saldo, extrato

def saque(*, saldo, valor, limite, extrato, quant_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = quant_saques >= limite_saques

    if excedeu_saldo:
        print("O valor excede o saldo disponível na conta")
    elif excedeu_limite:
        print("O valor excedeu o valor limite do saque")
    elif excedeu_saques:
        print("Voce atingiu o limite de saques diários. Nao será possível sacar o valor")
    else:
        saldo -= valor
        print(f"Operacao realizada com sucesso! Voce sacou R${valor:.2f}")
        extrato += f"Saque: R${valor:.2f}"

    return saldo, extrato

def exibir_extrato(saldo,/,*, extrato):
    print("============EXTRATO===========")
    print("Nao foram realizadas movimentacoes" if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}")
    print("==============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

main()