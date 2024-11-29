def comprimir_string(texto):
    """Comprime uma string substituindo sequências de caracteres repetidos."""
    if not texto:
        return ""
    
    comprimido = []
    contador = 1
    
    for i in range(1, len(texto)):
        if texto[i] == texto[i - 1]:
            contador += 1
        else:
            comprimido.append(f"{contador}{texto[i - 1]}")
            contador = 1
    
    comprimido.append(f"{contador}{texto[-1]}")  # Adiciona o último grupo
    return "".join(comprimido)

print(comprimir_string(input('')))
