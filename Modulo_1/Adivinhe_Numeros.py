import random

def jogo_adivinhacao():
    print("Bem vindo ao jogo de adivinhação!\n")
    print("O sistema sorteou um número entre 0 e 100.")
    print("Tente adivinhar o número\n")

    numero_sorteado = random.randint(0, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 0 or palpite > 100:
                print("Por favor, insira um número entre 0 e 100.\n")
                continue

            if palpite < numero_sorteado:
                print("O número sorteado é maior. Tente novamente\n")
            elif palpite > numero_sorteado:
                print("O número sorteado é menor. Tente novamente\n")
            else:
                print(f"Você acertou o número {numero_sorteado}!")
                print(f"Número total de tentativas: {tentativas}")
                acertou = True
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.\n")

if __name__ == "__main__":
    jogo_adivinhacao()
