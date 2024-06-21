import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    palavras_embaralhadas = []
    
    for palavra in palavras:
        if len(palavra) > 2:
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])
            random.shuffle(letras_internas)
            palavra_embaralhada = primeira_letra + ''.join(letras_internas) + ultima_letra
            palavras_embaralhadas.append(palavra_embaralhada)
        else:
            palavras_embaralhadas.append(palavra)
    resultado = ' '.join(palavras_embaralhadas)
    
    return resultado
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)