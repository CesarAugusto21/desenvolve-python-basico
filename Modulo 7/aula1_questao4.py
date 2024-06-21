numero = input("Digite seu número de telefone: ")

if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != 9:
    numero = "9" + numero

completo = numero[:5] + "-" + numero[5:]
print("Seu número completo é: ", completo)