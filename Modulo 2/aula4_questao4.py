#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade 
#possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída 
#deve estar formatada exatamente como indicado. 
#Entrada: 576
#Saída:  5 nota(s) de R$100,00    1 nota(s) de R$50,00  1 nota(s) de R$20,00   0 nota(s) de R$10,00
#1 nota(s) de R$5,00   0 nota(s) de R$2,00   1 nota(s) de R$1,00

quantia = int(input("Qual o valor em reais?"))
resto100 = quantia / 100
resto100 = int(resto100)

resto50 = quantia / 50
resto50 = int(resto50)

resto20 = quantia / 20
resto20 = int(resto20)

resto10 = quantia / 10
resto10 = int(resto10)

resto5 = quantia / 5
resto5 = int(resto5)

resto2 = quantia / 2
resto2 = int(resto2)

resto1 = quantia / 1
resto1 = int(resto1)

print(f"{resto100} notas de R$ 100,00 , {resto50} notas de R$ 50,00 , {resto20} notas de R$ 20,00 , {resto10} notas de R$10,00 , {resto5} notas de R$5,00 , {resto2} notas de R$2,00 e {resto1} notas de R$1,00")
