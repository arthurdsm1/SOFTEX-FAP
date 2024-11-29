def decompor_valor(valor):
    cedulas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_cedulas = {}
    
    for cedula in cedulas:
        quantidade_cedulas[cedula] = valor // cedula
        valor %= cedula

    return quantidade_cedulas

def main():
    try:
        entrada = input("Digite o valor em reais (R$): ")
        valor = int(str(entrada))
        if valor < 0:
            print("Por favor, insira um valor positivo.")
            return
        
        resultado = decompor_valor(valor)
        print("Decomposição em cédulas:")
        for cedula, quantidade in resultado.items():
            if quantidade > 0:
                print(f"R$ {cedula}: {quantidade} cédula(s)")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

if __name__ == "__main__":
    main()