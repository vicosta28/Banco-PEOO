print("Bem vindo(a) ao Banco DAHORA\n")

conta = input("Você já tem uma conta(sim/não)? ")
lista = []

if(conta=="não"):
    criar_conta = input("Digite seu nome: ")
    n_conta = input("Digite o numero da conta: ")
    saldo = float(input("Digite quanto quer depositar: "))
    lista.append(criar_conta)
    lista.append(n_conta)
    lista.append(saldo)
    print(lista)


if(conta=="sim"):
    cont = input("Qual o numero da sua conta? ")
    menu = int(input("(1)Sacar\n(2)Depositar\n(3)Transferir\n(4)Extrato\n(5)Sair\nO que deseja acessar: "))

    if(menu==1):
        def sacar():
            saque = int(input("QUanto deseja sacar: "))
            if(saldo<saque):
                print("Saldo insuficiente")

            if(saldo>saque):
                saldo=-saque
                print("Retirada com sucesso!")

            
    elif(menu==2):
        def depositar():
            deposito = int(input("Digite seu deposito: "))
            saldo=+deposito
            print("Deposito realizado com sucesso!")

    if(menu==3):
        def transferir():
            tranferencia = input("Informe o numero da conta que deseja transferir: ")
            print("Seu saldo é",saldo)
            valor = int(input("Quanto deseja transferir: "))

            if(valor>saldo):
                print("Saldo insuficiente")
            
            if(valor<saldo):
                print("Transferencia realizada com sucesso!")

    elif(menu==4):
        def extrato():
            print("Saldo atual: ",saldo)

            return menu

    if(menu==5):
        s = input("Tem certerza que deseja sair(sim/não): ")