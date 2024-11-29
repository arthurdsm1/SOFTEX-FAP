import mysql.connector
from mysql.connector import Error

def inserir_dados():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            database='biblioteca',
            user='root',
            password='1234'
        )
        
        if conexao.is_connected():
            cursor = conexao.cursor()

            titulo = input("Digite o título do livro: ")
            id_editora = int(input("Digite o ID da editora: "))
            data_aquisicao = input("Digite a data de aquisição (AAAA-MM-DD): ")
            estado_livro = input("Digite o estado do livro (Novo/Usado): ")
            lido = input("O livro foi lido? (Sim/Não): ").lower() == 'sim'
            observacao = input("Digite alguma observação: ")

            livro_sql = """INSERT INTO Livro (Título, ID_Editora, Data_Aquisição, Estado_Livro, Lido, Observação)
                           VALUES (%s, %s, %s, %s, %s, %s)"""
            livro_dados = (titulo, id_editora, data_aquisicao, estado_livro, lido, observacao)
            cursor.execute(livro_sql, livro_dados)
            conexao.commit()
            id_livro = cursor.lastrowid

            while True:
                id_autor = int(input("Digite o ID do autor (ou 0 para terminar): "))
                if id_autor == 0:
                    break
                autor_livro_sql = """INSERT INTO Autor_Livro (ID_Autor, ID_Livro)
                                     VALUES (%s, %s)"""
                autor_livro_dados = (id_autor, id_livro)
                cursor.execute(autor_livro_sql, autor_livro_dados)
                conexao.commit()

            print("Livro inserido com sucesso!")
    
    except Error as e:
        print("Erro ao conectar ao MySQL", e)
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão ao MySQL encerrada")

if __name__ == "__main__":
    inserir_dados()
