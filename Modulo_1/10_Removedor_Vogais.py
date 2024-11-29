def remover_vogais(texto):
    """Remove todas as vogais de uma string."""
    vogais = "aeiouAEIOU"
    return "".join(char for char in texto if char not in vogais)

print(remover_vogais(input('')))
