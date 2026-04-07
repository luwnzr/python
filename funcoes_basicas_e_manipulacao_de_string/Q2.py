# Média de dois números reais com arrendondamento

n1 = float(input("Digite o 1° numero: "))
n2 = float(input("Digite o 2° numero: "))
media = (float(n1) + float(n2)) / 2
media = round(media,2)
print(f"A média é {media}")