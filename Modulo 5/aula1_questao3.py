import random

n = random.randint(1, 10)
x = 0
while x != n:
    x = int(input("Advinhe o número entre 1 e 10: "))

    if x > n :
        print("Muito alto, tente novamente!")
    elif x < n:
        print("Muito baixo, tente novamente!")

print("Correto o número é:", n)