#Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista chamada interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:

import random

lista1 = []
lista2 = []

for i in range(20):
    valor = random.randint(0, 50)
    lista1.append(valor)

print(f"lista 1:  {lista1}")

for a in range(20):
    valor2 = random.randint(0, 50)
    lista2.append(valor2)

print(f"lista 2:  {lista2}")

interseção = []   #lista vazia
for elemento in lista1:      # vai pegar cada elemento da lista 1 e verificar se tem na lista 2
    if elemento in lista2 and elemento not in interseção:
        interseção.append(elemento)  # se tiverem em amabas as listas vai adiicionar na lsita de interseção

print(f"A lista de interseção ordenada: {sorted(interseção)}")

print("A quantidade de vezes que cada elemento aparece em cada lista: ")
for i in interseção:
    print(f"{i}: ({lista1.count(i)}, {lista2.count(i)})")