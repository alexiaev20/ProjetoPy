# banco.py

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacoes = []
        self.adicionar_transacao("Abertura da conta", saldo_inicial)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.adicionar_transacao("Depósito", valor)
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.adicionar_transacao("Saque", -valor)
        else:
            print("Saldo insuficiente ou valor de saque inválido.")

    def extrato(self):
        print(f"\nExtrato da conta de {self.titular}:")
        for transacao in self.transacoes:
            print(f"{transacao['descricao']}: R$ {transacao['valor']:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}\n")

    def adicionar_transacao(self, descricao, valor):
        self.transacoes.append({"descricao": descricao, "valor": valor})

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular, saldo_inicial=0):
        if titular not in self.contas:
            self.contas[titular] = ContaBancaria(titular, saldo_inicial)
            print(f"Conta criada para {titular} com saldo inicial de R$ {saldo_inicial:.2f}.")
        else:
            print("Já existe uma conta com este titular.")

    def realizar_deposito(self, titular, valor):
        conta = self.contas.get(titular)
        if conta:
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")

    def realizar_saque(self, titular, valor):
        conta = self.contas.get(titular)
        if conta:
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    def emitir_extrato(self, titular):
        conta = self.contas.get(titular)
        if conta:
            conta.extrato()
        else:
            print("Conta não encontrada.")
