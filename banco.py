# banco.py

from typing import Dict
from transacoes import validar_valor, validar_titular, registrar_transacao

class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.transacoes = []
        self.adicionar_transacao("Abertura da conta", saldo_inicial)

    def depositar(self, valor: float):
        """Realiza um depósito na conta."""
        validar_valor(valor)
        self.saldo += valor
        self.adicionar_transacao("Depósito", valor)
        registrar_transacao(self.titular, "Depósito", valor, 'transacoes.log')

    def sacar(self, valor: float):
        """Realiza um saque da conta."""
        validar_valor(valor)
        if valor <= self.saldo:
            self.saldo -= valor
            self.adicionar_transacao("Saque", -valor)
            registrar_transacao(self.titular, "Saque", -valor, 'transacoes.log')
        else:
            raise ValueError("Saldo insuficiente.")

    def extrato(self) -> str:
        """Gera o extrato da conta."""
        extrato = [f"\nExtrato da conta de {self.titular}:"]
        extrato.extend([f"{transacao['descricao']}: R$ {transacao['valor']:.2f}" for transacao in self.transacoes])
        extrato.append(f"Saldo atual: R$ {self.saldo:.2f}\n")
        return "\n".join(extrato)

    def adicionar_transacao(self, descricao: str, valor: float):
        """Adiciona uma transação à lista de transações da conta."""
        self.transacoes.append({"descricao": descricao, "valor": valor})

class Banco:
    def __init__(self):
        self.contas: Dict[str, ContaBancaria] = {}

    def criar_conta(self, titular: str, saldo_inicial: float = 0) -> str:
        """Cria uma nova conta bancária."""
        if titular not in self.contas:
            self.contas[titular] = ContaBancaria(titular, saldo_inicial)
            return f"Conta criada para {titular} com saldo inicial de R$ {saldo_inicial:.2f}."
        else:
            raise ValueError("Já existe uma conta com este titular.")

    def realizar_deposito(self, titular: str, valor: float) -> str:
        """Realiza um depósito na conta especificada."""
        validar_titular(self, titular)
        conta = self.contas[titular]
        conta.depositar(valor)
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."

    def realizar_saque(self, titular: str, valor: float) -> str:
        """Realiza um saque da conta especificada."""
        validar_titular(self, titular)
        conta = self.contas[titular]
        conta.sacar(valor)
        return f"Saque de R$ {valor:.2f} realizado com sucesso."

    def emitir_extrato(self, titular: str) -> str:
        """Emite o extrato da conta especificada."""
        validar_titular(self, titular)
        conta = self.contas[titular]
        return conta.extrato()
