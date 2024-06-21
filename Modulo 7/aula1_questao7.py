import random

def encrypt(nomes):
    n = random.randint(1, 10)
    
    def criptografar(nome, n):
        nome_criptografado = []
        for char in nome:
            novo_char = chr(((ord(char) - 33 + n) % 94) + 33)
            nome_criptografado.append(novo_char)
        return ''.join(nome_criptografado)
    
    nomes_criptografados = [criptografar(nome, n) for nome in nomes]
    
    return nomes_criptografados, n
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_criptografados, chave_aleatoria = encrypt(nomes)
print(f"Chave aleatória: {chave_aleatoria}")
print("Nomes criptografados: ", nomes_criptografados)