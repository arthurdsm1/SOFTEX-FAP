class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def verificar_maioridade(self, ano_atual):
        idade = ano_atual - self.ano_nascimento
        if idade >= 18:
            print(f"{self.nome} é maior de idade!")
        else:
            print(f"{self.nome} é menor de idade!")

pessoa = Pessoa("Maria", 2000)
pessoa.verificar_maioridade(2024)
