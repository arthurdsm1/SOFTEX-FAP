class Animal:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    def fazer_som(self):
        if self.tipo == "Cachorro":
            print(f"{self.nome} diz: Au Au!")
        elif self.tipo == "Gato":
            print(f"{self.nome} diz: Miau!")
        else:
            print(f"{self.nome} faz um som desconhecido.")


animal = Animal("Rex", "Cachorro")
animal.fazer_som()

animal2 = Animal("Felix", "Gato")
animal2.fazer_som()
