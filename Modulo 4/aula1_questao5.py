n = int(input("Qual a quantidade de respondentes? "))
cont = 1 
soma = 0

while cont <= n:
    idade = int(input("Qual a idade: "))
    soma += idade
    cont += 1
soma = soma/n
print(" A média das idades é : ")
print(soma)
