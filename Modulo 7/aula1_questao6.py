from collections import Counter

def anagramas(palavra1, palavra2):
    return Counter(palavra1.lower()) == Counter(palavra2.lower())

frase = input("Digite uma frase: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

palavras = frase.split()
anagramas = []
for palavra in palavras:
    if anagramas(palavra, palavra_objetivo):
        anagramas.append(palavra)
print("Anagramas:", anagramas)