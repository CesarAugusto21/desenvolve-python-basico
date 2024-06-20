# Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
import random

aleatorios = []
for i in range (20):
    valor = random.randint(-100, 100)
    aleatorios.append(valor)
print(sorted(aleatorios))
print(aleatorios)
print(max(aleatorios))
print(min(aleatorios))
print("O maior valor está no índice:", aleatorios.index(max(aleatorios)))
print("O menor valor está no índice:", aleatorios.index(min(aleatorios)))