def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Bem Vindo ao Conversor de Temperaturas\n")
    
    while True:
        print("Escolha o sistema de entrada:")
        print("1 - Celsius para Fahrenheit")
        print("2 - Fahrenheit para Celsius")
        print("0 - Sair")
        
        try:
            opcao = int(input("Digite a opção desejada: "))
            
            if opcao == 1:
                # Celsius para Fahrenheit
                celsius = float(input("Informe a temperatura em Celsius: "))
                fahrenheit = celsius_para_fahrenheit(celsius)
                print(f"\n{celsius:.2f}°C equivalem a {fahrenheit:.2f}°F.\n")
            elif opcao == 2:
                # Fahrenheit para Celsius
                fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
                celsius = fahrenheit_para_celsius(fahrenheit)
                print(f"\n{fahrenheit:.2f}°F equivalem a {celsius:.2f}°C.\n")
            elif opcao == 0:
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 0.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.\n")

if __name__ == "__main__":
    main()
