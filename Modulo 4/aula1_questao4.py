n = int(input("Digite um número: "))
maior = 0
while n > 0:
    x = int(input("Digite outro número: "))
    while x > maior:
        maior = x
    n -= 1
print(maior)