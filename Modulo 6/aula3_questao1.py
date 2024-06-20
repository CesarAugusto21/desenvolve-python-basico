tamanho = int(input("Qual a quantidade de elementos da lista: "))
lista = []

for i in range(tamanho):
    valor = int(input("Digite um número para a lista: "))
    lista.append(valor)

print(f"Lista: {lista}")
print(f"Lista: {lista[0:3:]}")
print(f"Lista: {lista[:-3:-1]}")
print(f"Lista: {lista[::-1]}")
print(f"Lista: {lista[0::2]}")
print(f"Lista: {lista[1::2]}")