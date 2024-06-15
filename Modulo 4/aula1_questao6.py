n = int(input("Qual a quantidade de experimentos registrados? "))
cont = 0
soma_sapo, soma_rato, soma_coelho = 0, 0, 0

while cont < n:
    quantia = int(input("Qual a quantia de cobaias? "))
    tipo = input("Qual foi a cobaia usada? ")

    if tipo == 'S':
        soma_sapo += quantia
    elif tipo == 'R':
        soma_rato += quantia
    elif tipo == 'C':
        soma_coelho += quantia
    else:
        print("Valor inválido")
    cont += 1

print("Total de cobaias:", soma_sapo + soma_rato + soma_coelho)
print("Total de sapos:", soma_sapo)
print("Total de ratos:", soma_rato)
print("Total de coelhos:", soma_coelho)

print("Percental de sapos:", (soma_sapo * 100)/(soma_sapo + soma_rato + soma_coelho))
print("Percentual de ratos:", (soma_rato * 100)/(soma_sapo + soma_rato + soma_coelho))
print("Percentual de coelhos:", (soma_coelho * 100)/(soma_sapo + soma_rato + soma_coelho))