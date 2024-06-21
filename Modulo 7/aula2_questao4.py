def validador_senha(senha):
    if len(senha) == 8:
        return True
    
    maiuscula = any(char.isupper() for char in senha)
    minuscula = any(char.islower() for char in senha)
    if  (maiuscula and minuscula):
        return True
    
    numero = any(char.isdigit() for char in senha)
    if  numero:
        return True

    caracteres_especiais = string.punctuation  
    especial = any(char in caracteres_especiais for char in senha)
    if  especial:
        return True
    return False

senha = input("Digite uma senha: ")
resultado = validador_senha(senha)
print(f"A senha {senha} é :{resultado}")