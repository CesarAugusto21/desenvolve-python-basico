#1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), 
#bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e 
#imprima o resultado com a formatação apresentada a seguir.
#O terreno possui 250m2 e custa R$512,490.50
#Comente na linha acima de cada instrução uma breve descrição da instrução.
#Fórmulas: area_m2 = comprimento * largura       preco_total = preco_m2 * area_m2 

comprimento= int(input("Qual o comprimento do terreno?")) #entrada de dados do comprimento do terreno
largura= int(input("Qual a largura do terreno")) #entrada de dados da largura do terreno
preco_m2= float(input("Qual o preço do terreno por metro quadrado?")) #entrada de dados do preço por metro quadrado

area_m2= comprimento * largura   #processamento de dados para achar a area por metro quadrado
preco_total = preco_m2 * area_m2  #processamento de dados para achar o preço total

print(f"A area total do terreno é : {area_m2}m² e o preço total é : R${preco_total: ,.3f}")  #saida de dados formatado de acordo com o pedido
