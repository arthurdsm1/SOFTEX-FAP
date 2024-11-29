import math

def obter_dimensoes_deposito():
    while True:
        try:
            comprimento = float(input("Digite o comprimento do depósito (cm): "))
            largura = float(input("Digite a largura do depósito (cm): "))
            altura = float(input("Digite a altura do depósito (cm): "))
            if comprimento > 0 and largura > 0 and altura > 0:
                return comprimento, largura, altura
            else:
                print("As dimensões devem ser números positivos.")
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

def selecionar_tamanho_bola():
    bolas_predefinidas = {
        1: ("Bola de Basquete Adulto", 24),
        2: ("Bola de Basquete Infantil", 22),
        3: ("Bola de Futebol Oficial", 22),
        4: ("Bola de Vôlei", 21),
        5: ("Bola de Handball", 19),
        6: ("Bola de Futebol de Salão", 20)
    }
    
    print("\nSelecione o tipo de bola:")
    for chave, (nome, diametro) in bolas_predefinidas.items():
        print(f"{chave} - {nome} ({diametro} cm)")
    print("7 - Outro tamanho de bola")
    
    while True:
        try:
            opcao = int(input("Digite o número correspondente à sua escolha: "))
            if opcao in bolas_predefinidas:
                return bolas_predefinidas[opcao][1]
            elif opcao == 7:
                while True:
                    try:
                        diametro = float(input("Digite o diâmetro da bola (cm): "))
                        if diametro > 0:
                            return diametro
                        else:
                            print("O diâmetro deve ser um número positivo.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número válido.")
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def calcular_volume_deposito(comprimento, largura, altura):
    return comprimento * largura * altura

def calcular_volume_bola(diametro):
    raio = diametro / 2
    return (4/3) * math.pi * (raio ** 3)

def estimar_quantidade_bolas(volume_deposito, volume_bola):
    eficiencia_empacotamento = 0.7
    return int((volume_deposito * eficiencia_empacotamento) // volume_bola)

def exibir_resultados(qtd_bolas, volume_deposito, volume_bola):
    print("\nResultados:")
    print(f"Volume do depósito: {volume_deposito:.2f} cm³")
    print(f"Volume da bola: {volume_bola:.2f} cm³")
    print(f"Número aproximado de bolas que cabem no depósito: {qtd_bolas}")

def main():
    print("Programa de cálculo de bolas em um depósito\n")
    
    comprimento, largura, altura = obter_dimensoes_deposito()
    diametro_bola = selecionar_tamanho_bola()
    
    volume_deposito = calcular_volume_deposito(comprimento, largura, altura)
    volume_bola = calcular_volume_bola(diametro_bola)
    qtd_bolas = estimar_quantidade_bolas(volume_deposito, volume_bola)
    
    exibir_resultados(qtd_bolas, volume_deposito, volume_bola)

if __name__ == "__main__":
    main()
