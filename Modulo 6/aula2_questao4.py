

quantidade = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = []
for i in range(quantidade):
    valor = int(input("Digite um elemento da lista: "))
    lista1.append(valor)


quantidade2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = []
for i in range(quantidade2):
    valor2 = int(input("Digite um elemento da lista: "))
    lista2.append(valor2)

def listaIntercalada(lista1, lista2):
    intercalada = []
    tamanho = max(len(lista1), len(lista2))
    for i in range(tamanho):
        if i< len(lista1):
            intercalada.append(lista1[i])
        if i< len(lista2):
            intercalada.append(lista2[i])
    return intercalada
intercalada = listaIntercalada(lista1, lista2)

print(f"Lista 1: {lista1} ")
print(f"Lista2: {lista2} ")
print(f"Lista intercalada: {intercalada} ")
