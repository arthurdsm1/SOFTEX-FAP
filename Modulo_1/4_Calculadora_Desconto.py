def calcular_valor(tipo_combustivel, litros):
    # Preços por litro
    preco_alcool = 1.90
    preco_gasolina = 2.50

    # Descontos por litro
    if tipo_combustivel == 'álcool':
        if litros <= 20:
            desconto = 0.03  # 3%
        else:
            desconto = 0.05  # 5%
        preco_por_litro = preco_alcool
    elif tipo_combustivel == 'gasolina':
        if litros <= 20:
            desconto = 0.04  # 4%
        else:
            desconto = 0.06  # 6%
        preco_por_litro = preco_gasolina
    else:
        return None  # Tipo inválido

    # Cálculo do valor total com desconto
    valor_bruto = preco_por_litro * litros
    valor_desconto = valor_bruto * desconto
    valor_final = valor_bruto - valor_desconto

    return valor_final, valor_desconto

def main():
    print("Bem-vindo ao Posto de Gasolina!\n")
    print("Tipos de combustível disponíveis: álcool, gasolina\n")
    
    tipo_combustivel = input("Digite o tipo de combustível: ").strip().lower()
    if tipo_combustivel not in ['álcool', 'gasolina']:
        print("Tipo de combustível inválido. Tente novamente.")
        return

    try:
        litros = float(input("Digite a quantidade de litros: "))
        if litros <= 0:
            print("Quantidade de litros inválida. Tente novamente.")
            return

        valor_final, valor_desconto = calcular_valor(tipo_combustivel, litros)

        if valor_final is not None:
            print(f"\nResumo da compra:")
            print(f"Tipo de combustível: {tipo_combustivel.capitalize()}")
            print(f"Quantidade de litros: {litros:.2f}L")
            print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
            print(f"Valor total a pagar: R$ {valor_final:.2f}")
        else:
            print("Erro no cálculo. Tente novamente.")

    except ValueError:
        print("Entrada inválida. Por favor, insira valores numéricos para a quantidade de litros.")

if __name__ == "__main__":
    main()
