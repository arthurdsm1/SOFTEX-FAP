def criptografar(frase):
    """Criptografa uma frase deslocando cada letra 3 posições no alfabeto."""
    resultado = []
    for char in frase:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            novo_char = chr(base + (ord(char) - base + 3) % 26)
            resultado.append(novo_char)
        else:
            resultado.append(char)
    return "".join(resultado)

print(criptografar(input('')))