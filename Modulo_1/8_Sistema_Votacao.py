def calcular_percentual(valor, total):
    """Calcula o percentual de um valor em relação ao total."""
    if total == 0:
        return 0.0
    return (valor / total) * 100

def main():
    print("Sistema de Votação\n")
    print("Candidatos:")
    print("1 - Candidato 1")
    print("2 - Candidato 2")
    print("3 - Candidato 3")
    print("4 - Candidato 4")
    print("5 - Voto Nulo")
    print("6 - Voto em Branco")
    print("Digite 0 para encerrar a votação.\n")

    # Inicialização dos contadores de votos
    votos_candidato = {1: 0, 2: 0, 3: 0, 4: 0}
    votos_nulos = 0
    votos_brancos = 0
    total_votos = 0

    while True:
        try:
            voto = int(input("Digite o número do seu voto: "))
            if voto == 0:
                break  # Encerra a votação
            elif voto in votos_candidato:
                votos_candidato[voto] += 1
            elif voto == 5:
                votos_nulos += 1
            elif voto == 6:
                votos_brancos += 1
            else:
                print("Voto inválido. Tente novamente.")
                continue
            total_votos += 1
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    # Exibição dos resultados
    print("\nResultado da Votação:")
    for candidato, votos in votos_candidato.items():
        percentual = calcular_percentual(votos, total_votos)
        print(f"Candidato {candidato}: {votos} votos ({percentual:.2f}%)")
    
    percentual_nulos = calcular_percentual(votos_nulos, total_votos)
    percentual_brancos = calcular_percentual(votos_brancos, total_votos)
    
    print(f"Votos Nulos: {votos_nulos} ({percentual_nulos:.2f}%)")
    print(f"Votos em Branco: {votos_brancos} ({percentual_brancos:.2f}%)")
    print(f"Total de votos: {total_votos}")

if __name__ == "__main__":
    main()
