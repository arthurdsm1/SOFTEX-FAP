import ttkbootstrap 
from datetime import datetime
import mysql.connector

# Conexão com o MySQL
db_config = {
    'user': 'root',
    'password': '4471',
    'host': 'localhost',
    'database': 'banco_db'
}

# Classe que representa uma conta bancária
class ContaBancaria:
    def __init__(self, nome_usuario, numero_conta, data_abertura, tipo_conta):
        self._nome_usuario = nome_usuario
        self._numero_conta = numero_conta
        self._data_abertura = data_abertura
        self._tipo_conta = tipo_conta
        self._saldo = 0.0

    # @property permite acessar os metódos como atributos, invés de métodos
    @property
    def nome_usuario(self):
        return self._nome_usuario

    @property
    def numero_conta(self):
        return self._numero_conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def tipo_conta(self):
        return self._tipo_conta

    # Metodo para depositar o dinheiro
    def depositar(self, valor):
        self._saldo += valor
        self._registrar_movimentacao("Depósito", valor)
    # Metodo para sacar o dinheiro
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            self._registrar_movimentacao("Saque", -valor)
            return True
        return False

    # Metodo pra registrar as movimentações no banco
    def _registrar_movimentacao(self, tipo, valor):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = ("INSERT INTO movimentacoes "
                 "(numero_conta, tipo, valor, data) "
                 "VALUES (%s, %s, %s, %s)")
        data = (self._numero_conta, tipo, valor, datetime.now())
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()

    # Metodo que retorna o extrato da conta
    def extrato(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT tipo, valor, data FROM movimentacoes WHERE numero_conta = %s"
        cursor.execute(query, (self._numero_conta,))
        movimentos = cursor.fetchall()
        cursor.close()
        conn.close()
        return movimentos

# Classe que gerencia as contas bancárias
class GerenciadorContas:
    def __init__(self):
        self._contas = {}

    def cadastrar_conta(self, nome_usuario, numero_conta, tipo_conta):
        if numero_conta in self._contas:
            return False
        
        data_abertura = datetime.now()
        conta = ContaBancaria(nome_usuario, numero_conta, data_abertura, tipo_conta)
        self._contas[numero_conta] = conta

        # Coloca a conta no banco de dados
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = ("INSERT INTO contas_bancarias "
                 "(numero_conta, nome_usuario, data_abertura, tipo_conta, saldo) "
                 "VALUES (%s, %s, %s, %s, %s)")
        data = (numero_conta, nome_usuario, data_abertura, tipo_conta, conta.saldo)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        return True

    def editar_conta(self, numero_conta, novo_nome):
        if numero_conta in self._contas:
            self._contas[numero_conta]._nome_usuario = novo_nome

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "UPDATE contas_bancarias SET nome_usuario = %s WHERE numero_conta = %s"
            cursor.execute(query, (novo_nome, numero_conta))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        return False

    def excluir_conta(self, numero_conta):
        if numero_conta in self._contas:
            del self._contas[numero_conta]

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "DELETE FROM contas_bancarias WHERE numero_conta = %s"
            cursor.execute(query, (numero_conta,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        return False

    def depositar(self, numero_conta, valor):
        if numero_conta in self._contas:
            self._contas[numero_conta].depositar(valor)

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "UPDATE contas_bancarias SET saldo = saldo + %s WHERE numero_conta = %s"
            cursor.execute(query, (valor, numero_conta))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        return False

    def sacar(self, numero_conta, valor):
        if numero_conta in self._contas and self._contas[numero_conta].sacar(valor):

            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "UPDATE contas_bancarias SET saldo = saldo - %s WHERE numero_conta = %s"
            cursor.execute(query, (valor, numero_conta))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        return False

    def extrato(self, numero_conta):
        if numero_conta in self._contas:
            return self._contas[numero_conta].extrato()
        return None

# Menu principal do sistema
def menu():
    print("\n=== GERENCIAMENTO DE CONTAS BANCÁRIAS ===")
    print("1. Cadastrar nova conta")
    print("2. Listar contas")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Extrato")
    print("6. Editar conta")
    print("7. Excluir conta")
    print("0. Sair")
    return input("Digite a opção desejada: ")

# Função que roda o programa
def main():
    gerenciador = GerenciadorContas()

    while True:
        opcao = menu()

        if opcao == "1":
            # Cadastra uma conta
            nome = input("Nome do usuario: ")
            numero = input("Número da conta: ")
            tipo = input("Tipo de conta (1 = Poupança, 2 = Corrente): ")
            if gerenciador.cadastrar_conta(nome, numero, tipo):
                print("Conta cadastrada com sucesso!")
            else:
                print("Erro ao cadastrar conta. Verifique os dados.")

        elif opcao == "2":
            # Lista as contas cadastradas
            print("\nContas cadastradas:")
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            query = "SELECT numero_conta, nome_usuario, tipo_conta, saldo FROM contas_bancarias"
            cursor.execute(query)
            contas = cursor.fetchall()
            for conta in contas:
                tipo = 'Poupança' if conta['tipo_conta'] == '1' else 'Corrente'
                print(f"Número: {conta['numero_conta']}, Nome: {conta['nome_usuario']}, Tipo: {tipo}, Saldo: R${conta['saldo']:.2f}")
            cursor.close()
            conn.close()

        elif opcao == "3":
            # Realiza um depósito em uma conta
            numero = input("Número da conta: ")
            try:
                valor = float(input("Valor do depósito: ").replace(',', '.'))
                if gerenciador.depositar(numero, valor):
                    print("Depósito realizado com sucesso!")
                else:
                    print("Erro ao realizar depósito. Verifique o número da conta.")
            except ValueError:
                print("Valor inválido. Por favor, use apenas números.")

        elif opcao == "4":
            # Realiza um saque em uma conta
            numero = input("Número da conta: ")
            try:
                valor = float(input("Valor do saque: ").replace(',', '.'))
                if gerenciador.sacar(numero, valor):
                    print("Saque realizado com sucesso!")
                else:
                    print("Erro ao realizar saque. Verifique o número da conta ou o saldo disponível.")
            except ValueError:
                print("Valor inválido. Por favor, use apenas números.")

        elif opcao == "5":
            # Mostra o extrato de uma conta
            numero = input("Número da conta: ")
            extrato = gerenciador.extrato(numero)
            if extrato:
                print("\nExtrato:")
                for mov in extrato:
                    print(f"Tipo: {mov['tipo']}, Valor: R${mov['valor']:.2f}, Data: {mov['data']}")
            else:
                print("Conta não encontrada.")

        elif opcao == "6":
            # Edita o nome de uma conta
            numero = input("Número da conta: ")
            novo_nome = input("Novo nome do usuario: ")
            if gerenciador.editar_conta(numero, novo_nome):
                print("Conta editada com sucesso!")
            else:
                print("Erro ao editar conta. Verifique o número da conta.")

        elif opcao == "7":
            # Exclui uma conta
            numero = input("Número da conta: ")
            if gerenciador.excluir_conta(numero):
                print("Conta excluída com sucesso!")
            else:
                print("Erro ao excluir conta. Verifique o número da conta.")

        elif opcao == "0":
            # Encerra o programa
            print("Obrigado por usar o sistema.")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()