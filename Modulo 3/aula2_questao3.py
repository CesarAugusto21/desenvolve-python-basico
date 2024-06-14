idade = int (input ("Digite sua idade: "))
jogos = int(input ("Digite a quantidade de jogos de tabuleiro que você jogou: "))
venceu = int(input("Já venceu quantos jogos: "))

print("Apto para ingressar no clube de jogos de tabuleiro:")
print((idade <=18 and idade >=16) and (jogos >= 3) and (venceu >= 1))
