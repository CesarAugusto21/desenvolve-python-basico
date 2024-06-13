#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade 
#possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída 
#deve estar formatada exatamente como indicado. 
#Entrada: 576
#Saída:  5 nota(s) de R$100,00    1 nota(s) de R$50,00  1 nota(s) de R$20,00   0 nota(s) de R$10,00
#1 nota(s) de R$5,00   0 nota(s) de R$2,00   1 nota(s) de R$1,00

quantia = int(input("Qual o valor em reais?"))
resto100 = quantia % 100
div1 = int (quantia / 100)

resto50 = resto100 % 50
div2 = int (resto100 / 50)

resto20 = resto50 % 20
div3 = int (resto50 / 20)

resto10 = resto20 % 10
div4 = int (resto20 / 10)

resto5 = resto10 % 5
div5 = int (resto10 / 5)

resto2 = resto5 % 2
div6 = int (resto5 / 2)

resto1 = resto2 % 1
div7 = int (resto2 / 1)

print(f"{div1} notas de R$ 100,00 , {div2} notas de R$ 50,00 , {div3} notas de R$ 20,00 , {div4} notas de R$10,00 , {div5} notas de R$5,00 , {div6} notas de R$2,00 e {div7} notas de R$1,00")
