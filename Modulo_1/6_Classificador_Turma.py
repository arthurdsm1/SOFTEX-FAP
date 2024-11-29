def classificar_turma(media_idade):
    if 0 <= media_idade <= 25:
        return "Jovem"
    elif 26 <= media_idade <= 60:
        return "Adulta"
    elif media_idade > 60:
        return "Idosa"
    else:
        return "Idade inválida"

def main():
    print("Classificador de Turma por Idade\n")
    print("Digite as idades. Digite 0 para encerrar.\n")
    
    idades = []
    
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade == 0:
                break
            if idade < 0:
                print("Idade inválida. Tente novamente.")
                continue
            idades.append(idade)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    
    if idades:
        media_idade = sum(idades) / len(idades)
        classificacao = classificar_turma(media_idade)
        print(f"\nMédia de idade: {media_idade:.2f} anos")
        print(f"Classificação da turma: {classificacao}")
    else:
        print("\nNenhuma idade foi informada.")

if __name__ == "__main__":
    main()
