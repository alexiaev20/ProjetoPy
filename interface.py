# interface.py

from banco import Banco

def menu():
    """Exibe o menu principal do sistema bancário."""
    print("\nBem-vindo ao Sistema Bancário")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Emitir Extrato")
    print("5. Sair")

def criar_conta(banco: Banco):
    """Cria uma nova conta bancária e exibe mensagem de sucesso ou erro."""
    try:
        titular = input("Digite o nome do titular: ")
        saldo_inicial = float(input("Digite o saldo inicial: "))
        mensagem = banco.criar_conta(titular, saldo_inicial)
        print(mensagem)
    except ValueError as e:
        print(e)

def realizar_deposito(banco: Banco):
    """Realiza um depósito e exibe mensagem de sucesso ou erro."""
    try:
        titular = input("Digite o nome do titular: ")
        valor = float(input("Digite o valor do depósito: "))
        mensagem = banco.realizar_deposito(titular, valor)
        print(mensagem)
    except ValueError as e:
        print(e)

def realizar_saque(banco: Banco):
    """Realiza um saque e exibe mensagem de sucesso ou erro."""
    try:
        titular = input("Digite o nome do titular: ")
        valor = float(input("Digite o valor do saque: "))
        mensagem = banco.realizar_saque(titular, valor)
        print(mensagem)
    except ValueError as e:
        print(e)

def emitir_extrato(banco: Banco):
    """Emite o extrato da conta e exibe ou exibe mensagem de erro."""
    try:
        titular = input("Digite o nome do titular: ")
        extrato = banco.emitir_extrato(titular)
        print(extrato)
    except ValueError as e:
        print(e)
