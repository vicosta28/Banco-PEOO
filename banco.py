print("\nBEM VINDO(A) AO BANCO DAHORA!")

contas_bancarias = []

def criar_conta():
    nome = input("Digite o nome do titular da conta: ")
    numero_conta = input("Digite o número da conta: ")


    for conta in contas_bancarias:
        if (conta["numero_conta"] == numero_conta):
            print("Essa conta já existe. Por favor escolha um numero de conta diferente.")
            return

    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    senha = input("Crie uma senha de 3 digitos: ")

    if len(senha)!=3:
        print("A senha deve conter somente 3 digitos. Tente novamente.")
        return

    conta = {
        "nome": nome,
        "numero_conta": numero_conta,
        "saldo": saldo_inicial,
        "senha":senha
    }

    contas_bancarias.append(conta)
    print("Conta criada com sucesso!")

def verificar_senha(numero_conta):
    senha = input("Digite sua senha de 3 digitos: ")

    for conta in contas_bancarias:
        if conta["numero_conta"] == numero_conta and  conta["senha"] == senha:
            return True
            
    return False

def sacar():
    numero_conta = input("Digite o número da conta: ")

    if verificar_senha(numero_conta):
        valor = float(input("Digite o valor que deseja sacar: "))
        for conta in contas_bancarias:
            if conta["numero_conta"] == numero_conta:
                if conta["saldo"] >= valor:
                    conta["saldo"] -= valor
                    print(f"Saque de R${valor} realizado com sucesso.")
                    return
                else:
                    print("Saldo insuficiente para realizar o saque.")
                    return
                
    else:
        print("Senha incorreta. Tente novamente.")


def depositar():
    numero_conta = input("Digite o número da conta: ")

    if verificar_senha(numero_conta):
        valor = float(input("Digite o valor que deseja depositar: "))
        for conta in contas_bancarias:
            if conta["numero_conta"] == numero_conta:
                conta["saldo"] += valor
                print(f"Depósito de R${valor} realizado com sucesso.")
                return
            
    else:
        print("Senha incorreta. Tente novamente.")

def transferir():
    conta_origem = input("Digite o número da conta de origem: ")
    conta_destino = input("Digite o número da conta de destino: ")

    if not verificar_senha(conta_origem):
        print("senha da conta de origem incorreta. Operação de transferencia recusada.")
        return
    
    valor = float(input("Digite o valor que deseja transferir: "))
    
    for origem in contas_bancarias:
        if origem["numero_conta"] == conta_origem:
            for destino in contas_bancarias:
                if destino["numero_conta"] == conta_destino:
                    if origem["saldo"] >= valor:
                        origem["saldo"] -= valor
                        destino["saldo"] += valor
                        print(f"Transferência de R${valor} realizada com sucesso.")
                        return
                    else:
                        print("Saldo insuficiente para realizar a transferência.")
                        return
                        

    print("Conta de origem ou destino não encontrada.")
    
def extrato_bancario():
    numero_conta = input("Digite o número da conta: ")

    if verificar_senha(numero_conta):
         for conta in contas_bancarias:
            if conta["numero_conta"] == numero_conta:
                print(f"Extrato bancário para a conta de {conta['nome']}:")
                print(f"Número da conta: {conta['numero_conta']}")
                print(f"Saldo atual: R${conta['saldo']}")
                return 
    else:
        print("Senha incorreta. Tente novamente")

    
   
while True:
    print("\nMenu:")
    print("1 - Criar Conta")
    print("2 - Sacar")
    print("3 - Depositar")
    print("4 - Transferir")
    print("5 - Ver Extrato Bancário")
    print("6 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        sacar()
    elif opcao == '3':
        depositar()
    elif opcao == '4':
        transferir()
    elif opcao == '5':
        extrato_bancario()
    elif opcao == '6':
        print("Saindo do menu.\nVolte sempre ao banco DAHORA!")
        break
    else:
        print("Opção inválida. Tente novamente.")
