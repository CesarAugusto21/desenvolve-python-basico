genero = str(input("Qual o seu gênero: M para masculino ou F para feminino ? "))  
idade = int(input("Digite sua idade: "))
servico = int(input("Digite seu tempo de serviço em anos: "))

print((genero == 'F') and ((idade > 60) or (servico >= 30) or((idade==60)and(servico>=25))) or (genero == 'M') and ((idade > 65) or (servico >= 30) or((idade==60)and(servico>=25))))