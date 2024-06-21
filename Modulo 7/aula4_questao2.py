import os

nome_arquivo_original = "frase.txt"
nome_arquivo_palavras = "palavras.txt"

with open(nome_arquivo_original, "r") as arquivo:
    conteudo = arquivo.read()

palavras = ''.join(char if char.isalpha() or char.isspace() else ' ' for char in conteudo).split()

with open(nome_arquivo_palavras, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + '\n')

with open(nome_arquivo_palavras, "r") as arquivo:
    conteudo_palavras = arquivo.read()

print(conteudo_palavras)