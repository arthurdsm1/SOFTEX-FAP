import mysql.connector
from datetime import datetime, timedelta

class BibliotecaDB:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user='root',
            password='1234',
            database=database
        )
        self.cursor = self.conn.cursor()

    def adicionar_livro(self, titulo, autor, ano_publicacao, categoria):
        sql = """INSERT INTO livros (titulo, autor, ano_publicacao, categoria)
                 VALUES (%s, %s, %s, %s)"""
        values = (titulo, autor, ano_publicacao, categoria)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def adicionar_usuario(self, nome, limite_livros=3):
        sql = "INSERT INTO usuarios (nome, limite_livros) VALUES (%s, %s)"
        values = (nome, limite_livros)
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid

    def emprestar_livro(self, livro_id, usuario_id):
        self.cursor.execute("SELECT disponivel FROM livros WHERE id = %s", (livro_id,))
        disponivel = self.cursor.fetchone()[0]
        if not disponivel:
            return False, "Livro não disponível"

        self.cursor.execute("SELECT COUNT(*) FROM emprestimos WHERE usuario_id = %s AND data_devolucao_real IS NULL", (usuario_id,))
        livros_emprestados = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT limite_livros FROM usuarios WHERE id = %s", (usuario_id,))
        limite_livros = self.cursor.fetchone()[0]
        
        if livros_emprestados >= limite_livros:
            return False, "Usuário atingiu o limite de livros emprestados"

        data_emprestimo = datetime.now().date()
        data_devolucao_prevista = data_emprestimo + timedelta(days=14)
        sql = """INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista)
                 VALUES (%s, %s, %s, %s)"""
        values = (livro_id, usuario_id, data_emprestimo, data_devolucao_prevista)
        self.cursor.execute(sql, values)

        self.cursor.execute("UPDATE livros SET disponivel = FALSE WHERE id = %s", (livro_id,))
        self.conn.commit()
        return True, "Livro emprestado com sucesso"

    def devolver_livro(self, livro_id, usuario_id):
        sql = """UPDATE emprestimos
                 SET data_devolucao_real = %s
                 WHERE livro_id = %s AND usuario_id = %s AND data_devolucao_real IS NULL"""
        values = (datetime.now().date(), livro_id, usuario_id)
        self.cursor.execute(sql, values)

        self.cursor.execute("UPDATE livros SET disponivel = TRUE WHERE id = %s", (livro_id,))
        self.conn.commit()
        return "Livro devolvido com sucesso"

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    db = BibliotecaDB("localhost", "seu_usuario", "sua_senha", "biblioteca")

    livro_id = db.adicionar_livro("1984", "George Orwell", 1949, "Ficção Científica")
    print(f"Livro adicionado com ID: {livro_id}")

    usuario_id = db.adicionar_usuario("Maria")
    print(f"Usuário adicionado com ID: {usuario_id}")

    sucesso, mensagem = db.emprestar_livro(livro_id, usuario_id)
    print(mensagem)

    mensagem = db.devolver_livro(livro_id, usuario_id)
    print(mensagem)

    db.fechar_conexao()
