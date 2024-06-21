import random

def carrega_palavras(arquivo):
    with open(arquivo, "r") as f:
        palavras = f.read().splitlines()
    return palavras

def carrega_enforcado(arquivo):
    with open(arquivo, "r") as f:
        estagios = f.read().splitlines()
    estagios_formatados = [estagios[i:i + 7] for i in range(0, len(estagios), 7)]
    return estagios_formatados

def escolhe_palavra(palavras):
    return random.choice(palavras)

def imprime_enforcado(estagios, erros):
    for linha in estagios[erros]:
        print(linha)

def jogo_da_forca():
    palavras = carrega_palavras("gabarito_forca.txt")
    estagios = carrega_enforcado("gabarito_enforcado.txt")

    palavra = escolhe_palavra(palavras)
    palavra_oculta = ["_"] * len(palavra)
    letras_tentadas = []
    erros = 0
    max_erros = 6
    
    print("Bem-vindo ao jogo da forca!")
    print("A palavra tem {} letras: {}".format(len(palavra), " ".join(palavra_oculta)))
    
    while erros < max_erros and "_" in palavra_oculta:
        tentativa = input("Digite uma letra: ").lower()
        
        if tentativa in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        letras_tentadas.append(tentativa)
        
        if tentativa in palavra:
            for i, letra in enumerate(palavra):
                if letra == tentativa:
                    palavra_oculta[i] = tentativa
            print("Acertou! A palavra até agora: {}".format(" ".join(palavra_oculta)))
        else:
            erros += 1
            imprime_enforcado(estagios, erros)
            print("Errou! Você tem mais {} tentativas.".format(max_erros - erros))
        
        print("Letras tentadas: {}".format(", ".join(letras_tentadas)))
    
    if "_" not in palavra_oculta:
        print("Parabéns! Você adivinhou a palavra: {}".format(palavra))
    else:
        print("Você foi enforcado! A palavra era: {}".format(palavra))


jogo_da_forca()