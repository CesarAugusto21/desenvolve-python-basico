import os

nome_arquivo = "estomago.txt"

def processar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
        for i in range(min(25, len(linhas))):
            print(linhas[i].strip())

        numero_de_linhas = len(linhas)
        print(f"\nNúmero total de linhas: {numero_de_linhas}")

        linha_mais_longa = max(linhas, key=len)
        print(f"\nLinha com maior número de caracteres ({len(linha_mais_longa)} caracteres):\n{linha_mais_longa.strip()}")

        mencoes_nonato = sum(1 for linha in linhas if "nonato" in linha.lower().split())
        mencoes_iria = sum(1 for linha in linhas if "íria" in linha.lower().split() or "iria" in linha.lower().split())
        print(f"\nNúmero de menções a 'Nonato': {mencoes_nonato}")
        print(f"Número de menções a 'Íria': {mencoes_iria}")

    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

processar_arquivo(nome_arquivo)