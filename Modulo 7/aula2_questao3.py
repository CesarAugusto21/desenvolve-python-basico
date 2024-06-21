import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim": #colocar tudo para minusculo
        break
    
    fraseP = ''.join(char.lower() for char in frase if char.isalnum())
    
    if fraseP == fraseP[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')