frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"

vogaisFrase = [char for char in frase if char in vogais]
consoantesFrase = [char for char in frase if char not in vogais]
vogaisOrdenadas = sorted(vogaisFrase)

print("Vogais:", vogaisOrdenadas)
print("Consoantes:", consoantesFrase)