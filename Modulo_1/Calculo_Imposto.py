def calcular_imposto(salario):

    if salario <= 2259.20:
        aliquota = 0
        deducao = 0
    elif salario <= 2826.65:
        aliquota = 0.075
        deducao = 169.44
    elif salario <= 3751.05:
        aliquota = 0.15
        deducao = 381.44
    elif salario <= 4664.68:
        aliquota = 0.225
        deducao = 662.77
    else:
        aliquota = 0.275
        deducao = 896.00

    imposto = (salario * aliquota) - deducao
    return max(imposto, 0)

while True:
    try:
        salario = float(input("Digite o seu salário bruto em R$: "))
        if salario < 0:
            print("O salário não pode ser negativo.")
            continue
        imposto = calcular_imposto(salario)
        print(f"\nSalário: R$ {salario:.2f}")
        print(f"Imposto a pagar: R$ {imposto:.2f}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, insira um valor válido.")