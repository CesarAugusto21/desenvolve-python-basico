#Todos os números pares entre 20 e 50, ou seja, [20, 22, 24, …, 48, 50]
lista1 = []
for i in range(20, 51):
    lista1.append(i)

pares = [n for n in lista1 if n % 2 == 0]
print(f"Lista 1: {pares}")

#Os quadrados de todos os valores da lista [1,2,3,4,5,6,7,8,9]

lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista 2: {lista2}")
quadrado = [n**2 for n in lista2]
print(f"quadrado da lista 2: {quadrado}")

#Todos os números entre 1 e 100 que sejam divisíveis por 7

lista3 = []
for i in range(1, 101):
    lista3.append(i)
print(f"Lista 3: {lista3}")
divisivel_7 = [n for n in lista3 if n % 7 ==0]
print(f"Lista 3 com números divisiveis por 7: {divisivel_7}")

#Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento (ex: ['par', 'impar',… , 'impar']) 
lista4 = []
for i in range(0, 30, 3):
    lista4.append(i)
if lista4[i] % 2 == 0:
    print("par")
else:
    print("impar")
