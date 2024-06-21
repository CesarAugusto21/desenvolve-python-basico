meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
data_nascimento = input("Digite uma data de nascimento, dessa forma:(dd/mm/aaaa):  ")

# split separador 
dia, mes, ano = data_nascimento.split('/')
mes = int(mes) - 1   #indice de mes
mes_extenso = meses[mes]
print(f"Você nasceu em {dia} de {mes_extenso} de {ano}.")


