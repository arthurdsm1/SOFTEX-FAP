def obter_altura():
    while True:
        try:
            altura = float(input("Digite sua altura em metros (entre 0.6 e 2.5): "))
            if 0.6 <= altura <= 2.5:
                return altura
            else:
                print("Altura inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def obter_peso():
    while True:
        try:
            peso = float(input("Digite seu peso em kg (entre 15 e 250): "))
            if 15 <= peso <= 250:
                return peso
            else:
                print("Peso inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 25 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35 <= imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    print("Bem vindo a calculadora de IMC\n")
    
    altura = obter_altura()
    peso = obter_peso()
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print("\nResultados:")
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

if __name__ == "__main__":
    main()
