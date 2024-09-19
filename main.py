# main.py

from banco import Banco

def menu():
    print("\nBem-vindo ao Sistema Bancário")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Emitir Extrato")
    print("5. Sair")

def executar_sistema():
    banco = Banco()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titular = input("Digite o nome do titular: ")
            saldo_inicial = float(input("Digite o saldo inicial: "))
            banco.criar_conta(titular, saldo_inicial)
        
        elif opcao == "2":
            titular = input("Digite o nome do titular: ")
            valor = float(input("Digite o valor do depósito: "))
            banco.realizar_deposito(titular, valor)

        elif opcao == "3":
            titular = input("Digite o nome do titular: ")
            valor = float(input("Digite o valor do saque: "))
            banco.realizar_saque(titular, valor)

        elif opcao == "4":
            titular = input("Digite o nome do titular: ")
            banco.emitir_extrato(titular)

        elif opcao == "5":
            print("Obrigado por usar o Sistema Bancário.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    executar_sistema()
