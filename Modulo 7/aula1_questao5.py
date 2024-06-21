frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
contas = 0
indice = []
for i in range(len(frase)):
    if frase[i] in vogais:
        contas += 1
        indice.append(i)
print(f"A frase: {frase}")
print(f"O número de vogais é: {contas}")
print(f"Os índices que contém vogais são: {indice}")