# Sistema de Banco

# Variáveis
saldo = 0.0

# Lista para armazenar as operações
extrato = []

# Dicionário com os dados da conta
conta = {
    "titular": "Cliente",
    "numero": "001",
    "saldo": saldo
}

while True:
    print("\n===== BANCO =====")
    print("1 - Acessar conta / Ver extrato")
    print("2 - Fazer depósito")
    print("3 - Fazer saque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # Ver extrato
    if opcao == "1":
        print("\n===== EXTRATO =====")
        print(f"Titular: {conta['titular']}")
        print(f"Conta: {conta['numero']}")
        print(f"Saldo: R$ {conta['saldo']:.2f}")

        if len(extrato) == 0:
            print("Nenhuma movimentação realizada.")
        else:
            print("\nMovimentações:")
            for operacao in extrato:
                print(operacao)

    # Depósito
    elif opcao == "2":
        deposito = float(input("Digite o valor do depósito: R$ "))

        if deposito > 0:
            conta["saldo"] += deposito

            extrato.append(
                f"Depósito: + R$ {deposito:.2f}"
            )

            print(f"Depósito realizado!")
            print(f"Novo saldo: R$ {conta['saldo']:.2f}")
        else:
            print("O valor do depósito deve ser maior que zero.")

    # Saque
    elif opcao == "3":
        saque = float(input("Digite o valor do saque: R$ "))

        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")

        elif saque > conta["saldo"]:
            print("Saldo insuficiente!")

        else:
            conta["saldo"] -= saque

            extrato.append(
                f"Saque: - R$ {saque:.2f}"
            )

            print("Saque realizado!")
            print(f"Novo saldo: R$ {conta['saldo']:.2f}")

    # Sair
    elif opcao == "4":
        print("Obrigado por utilizar nosso banco!")
        print("Até logo!")
        break

    # Opção inválida
    else:
        print("Opção inválida! Escolha uma opção de 1 a 4.")