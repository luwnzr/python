# Compriento de um texto

texto = input("Digite uma frase: ")
t = len(texto)
qe = texto.count(" ")
print(f"O tamanho da frase é: {t}")
print(f"O tamanho da frase sem espaço é: {t-qe}")