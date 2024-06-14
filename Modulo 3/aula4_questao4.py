distancia = int(input("Digite a distância da entrega em quilômetros: "))
peso = float(input("Digite o peso do pacote: "))

if  (distancia <= 100) and (peso <= 10):
    frete = 1 * distancia
if  (distancia <= 100) and (peso > 10):
    frete = 1 * distancia + 10

if  ((distancia > 100) and (distancia <= 300)) and (peso <= 10):
    frete = 1.5 * distancia
if  ((distancia > 100) and (distancia <= 300)) and (peso > 10):
    frete = 1.5 * distancia + 10

if  (distancia > 300) and (peso <= 10):
    frete = 2 * distancia
if  (distancia > 300) and (peso > 10):
    frete = 2 * distancia + 10

print("o valor do frete é: ")
print(frete)