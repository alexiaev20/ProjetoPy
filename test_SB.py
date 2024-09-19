import unittest
from banco import Banco
from transacoes import formatar_valor
from interface import criar_conta, realizar_deposito, realizar_saque, emitir_extrato

class TestBanco(unittest.TestCase):
    
    def setUp(self):
        """Cria uma instância do banco antes de cada teste."""
        self.banco = Banco()
    
    def test_criar_conta(self):
        """Testa a criação de uma nova conta."""
        mensagem = self.banco.criar_conta("Alexya", 1000)
        self.assertEqual(mensagem, "Conta criada para Alexya com saldo inicial de R$ 1000.00.")
        self.assertIn("Alexya", self.banco.contas)
    
    def test_criar_conta_existente(self):
        """Testa a criação de uma conta que já existe."""
        self.banco.criar_conta("Alexya", 1000)
        with self.assertRaises(ValueError):
            self.banco.criar_conta("Alexya", 500)
    
    def test_realizar_deposito(self):
        """Testa a realização de um depósito."""
        self.banco.criar_conta("Alexya", 1000)
        mensagem = self.banco.realizar_deposito("Alexya", 500)
        self.assertEqual(mensagem, "Depósito de R$ 500.00 realizado com sucesso.")
        self.assertEqual(self.banco.contas["Alexya"].saldo, 1500)
    
    def test_realizar_saque(self):
        """Testa a realização de um saque."""
        self.banco.criar_conta("Alexya", 1000)
        mensagem = self.banco.realizar_saque("Alexya", 500)
        self.assertEqual(mensagem, "Saque de R$ 500.00 realizado com sucesso.")
        self.assertEqual(self.banco.contas["Alexya"].saldo, 500)
    
    def test_saque_insuficiente(self):
        """Testa a tentativa de saque com saldo insuficiente."""
        self.banco.criar_conta("Alexya", 1000)
        with self.assertRaises(ValueError):
            self.banco.realizar_saque("Alexya", 1500)
    
    def test_emitir_extrato(self):
        """Testa a emissão do extrato da conta."""
        self.banco.criar_conta("Alexya", 1000)
        self.banco.realizar_deposito("Alexya", 500)
        self.banco.realizar_saque("Alexya", 200)
        extrato = self.banco.emitir_extrato("Alexya")
        esperado = (
            "\nExtrato da conta de Alexya:\n"
            "Abertura da conta: R$ 1000.00\n"
            "Depósito: R$ 500.00\n"
            "Saque: R$ -200.00\n"
            "Saldo atual: R$ 1300.00\n"
        )
        self.assertEqual(extrato, esperado)
    
    def test_formatar_valor(self):
        """Testa a formatação do valor monetário."""
        self.assertEqual(formatar_valor(1234.567), "R$ 1234.57")
        self.assertEqual(formatar_valor(0), "R$ 0.00")
        self.assertEqual(formatar_valor(-1234.56), "R$ -1234.56")

if __name__ == "__main__":
    unittest.main()
