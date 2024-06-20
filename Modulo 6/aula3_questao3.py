import random

lista = []
for i in range(20):
    valor = random.randint(-10, 10)
    lista.append(valor)

print(f"Lista: {lista}")

del lista[lista.index(min(lista))]
print(f"lista com o menor número deletado: {lista}")