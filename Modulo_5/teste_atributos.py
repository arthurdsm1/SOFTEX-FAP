class Carro:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f"O carro acelerou, Velocidade: {self.velocidade} km/h")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O carro freou, Velocidade: {self.velocidade} km/h")
        else:
            print("ja esta parado")


carro = Carro("Toyota", "Corolla", "Prata")
carro.acelerar()
carro.acelerar()
carro.frear()
