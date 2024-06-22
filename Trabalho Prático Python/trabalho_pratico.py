import os

# Definições de arquivo
USUARIOS_FILE = 'usuarios.txt'  # Nome do arquivo onde os dados dos usuários serão armazenados.
PRODUTOS_FILE = 'produtos.txt'  # Nome do arquivo onde os dados dos produtos serão armazenados.

# Funções para gerenciamento de usuários
def carregar_usuarios():
    """Carrega os usuários do arquivo de texto para uma lista de dicionários."""
    usuarios = []
    if os.path.exists(USUARIOS_FILE):  # Verifica se o arquivo de usuários existe.
        with open(USUARIOS_FILE, 'r') as file:  # Abre o arquivo de usuários em modo leitura.
            for line in file:  # Lê cada linha do arquivo.
                username, senha, nivel = line.strip().split(',')  # Divide a linha em username, senha e nível.
                usuarios.append({'username': username, 'senha': senha, 'nivel': nivel})  # Adiciona o usuário à lista.
    return usuarios  # Retorna a lista de usuários.

def salvar_usuarios(usuarios):
    """Salva a lista de usuários no arquivo de texto."""
    with open(USUARIOS_FILE, 'w') as file:  # Abre o arquivo de usuários em modo escrita.
        for usuario in usuarios:  # Itera sobre a lista de usuários.
            file.write(f"{usuario['username']},{usuario['senha']},{usuario['nivel']}\n")  # Escreve cada usuário no arquivo.

def criar_usuario(username, senha, nivel):
    """Adiciona um novo usuário ao sistema (Create)."""
    usuarios = carregar_usuarios()  # Carrega a lista de usuários existente.
    usuarios.append({'username': username, 'senha': senha, 'nivel': nivel})  # Adiciona o novo usuário à lista.
    salvar_usuarios(usuarios)  # Salva a lista atualizada de usuários.

def listar_usuarios():
    """Lista todos os usuários do sistema (Read)."""
    usuarios = carregar_usuarios()  # Carrega a lista de usuários.
    for usuario in usuarios:  # Itera sobre a lista de usuários.
        print(f"Username: {usuario['username']}, Nível: {usuario['nivel']}")  # Imprime os detalhes de cada usuário.

def atualizar_usuario(username, nova_senha=None, novo_nivel=None):
    """Atualiza os detalhes de um usuário existente (Update)."""
    usuarios = carregar_usuarios()  # Carrega a lista de usuários.
    for usuario in usuarios:  # Itera sobre a lista de usuários.
        if usuario['username'] == username:  # Verifica se o username corresponde.
            if nova_senha:  # Atualiza a senha, se fornecida.
                usuario['senha'] = nova_senha
            if novo_nivel:  # Atualiza o nível, se fornecido.
                usuario['nivel'] = novo_nivel
    salvar_usuarios(usuarios)  # Salva a lista atualizada de usuários.

def deletar_usuario(username):
    """Remove um usuário do sistema (Delete)."""
    usuarios = carregar_usuarios()  # Carrega a lista de usuários.
    usuarios = [usuario for usuario in usuarios if usuario['username'] != username]  # Remove o usuário da lista.
    salvar_usuarios(usuarios)  # Salva a lista atualizada de usuários.

# Função para autenticação
def autenticar(username, senha):
    """Autentica um usuário verificando seu username e senha."""
    usuarios = carregar_usuarios()  # Carrega a lista de usuários.
    for usuario in usuarios:  # Itera sobre a lista de usuários.
        if usuario['username'] == username and usuario['senha'] == senha:  # Verifica se o username e senha correspondem.
            return usuario  # Retorna o usuário autenticado.
    return None  # Retorna None se a autenticação falhar.


#produtos
# Funções para gerenciamento de produtos
def carregar_produtos():
    """Carrega os produtos do arquivo de texto para uma lista de dicionários."""
    produtos = []
    if os.path.exists(PRODUTOS_FILE):  # Verifica se o arquivo de produtos existe.
        with open(PRODUTOS_FILE, 'r') as file:  # Abre o arquivo de produtos em modo leitura.
            for line in file:  # Lê cada linha do arquivo.
                nome, preco, quantidade = line.strip().split(',')  # Divide a linha em nome, preço e quantidade.
                produtos.append({'nome': nome, 'preco': float(preco), 'quantidade': int(quantidade)})  # Adiciona o produto à lista.
    return produtos  # Retorna a lista de produtos.

def salvar_produtos(produtos):
    """Salva a lista de produtos no arquivo de texto."""
    with open(PRODUTOS_FILE, 'w') as file:  # Abre o arquivo de produtos em modo escrita.
        for produto in produtos:  # Itera sobre a lista de produtos.
            file.write(f"{produto['nome']},{produto['preco']},{produto['quantidade']}\n")  # Escreve cada produto no arquivo.

def criar_produto(nome, preco, quantidade):
    """Adiciona um novo produto ao sistema (Create)."""
    produtos = carregar_produtos()  # Carrega a lista de produtos existente.
    produtos.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})  # Adiciona o novo produto à lista.
    salvar_produtos(produtos)  # Salva a lista atualizada de produtos.

def listar_produtos():
    """Lista todos os produtos do sistema (Read)."""
    produtos = carregar_produtos()  # Carrega a lista de produtos.
    for produto in produtos:  # Itera sobre a lista de produtos.
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")  # Imprime os detalhes de cada produto.

def atualizar_produto(nome, novo_preco=None, nova_quantidade=None):
    """Atualiza os detalhes de um produto existente (Update)."""
    produtos = carregar_produtos()  # Carrega a lista de produtos.
    for produto in produtos:  # Itera sobre a lista de produtos.
        if produto['nome'] == nome:  # Verifica se o nome corresponde.
            if novo_preco:  # Atualiza o preço, se fornecido.
                produto['preco'] = novo_preco
            if nova_quantidade:  # Atualiza a quantidade, se fornecida.
                produto['quantidade'] = nova_quantidade
    salvar_produtos(produtos)  # Salva a lista atualizada de produtos.

def deletar_produto(nome):
    """Remove um produto do sistema (Delete)."""
    produtos = carregar_produtos()  # Carrega a lista de produtos.
    produtos = [produto for produto in produtos if produto['nome'] != nome]  # Remove o produto da lista.
    salvar_produtos(produtos)  # Salva a lista atualizada de produtos.

def buscar_produto(nome):
    """Busca um produto pelo nome."""
    produtos = carregar_produtos()  # Carrega a lista de produtos.
    for produto in produtos:  # Itera sobre a lista de produtos.
        if produto['nome'] == nome:  # Verifica se o nome corresponde.
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")  # Imprime os detalhes do produto.
            return produto  # Retorna o produto encontrado.
    print("Produto não encontrado.")  # Imprime mensagem de erro se o produto não for encontrado.
    return None  # Retorna None se o produto não for encontrado.

def listar_produtos_ordenados_por_nome():
    """Lista os produtos ordenados por nome."""
    produtos = carregar_produtos()  # Carrega a lista de produtos.
    produtos_ordenados = sorted(produtos, key=lambda x: x['nome'])  # Ordena os produtos pelo nome.
    for produto in produtos_ordenados:  # Itera sobre a lista de produtos ordenados.
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")  # Imprime os detalhes de cada produto.

def listar_produtos_ordenados_por_preco():
    """Lista os produtos ordenados por preço."""
    produtos = carregar_produtos()  # Carrega a lista de produtos.
    produtos_ordenados = sorted(produtos, key=lambda x: x['preco'])  # Ordena os produtos pelo preço.
    for produto in produtos_ordenados:  # Itera sobre a lista de produtos ordenados.
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")  # Imprime os detalhes de cada produto.


# Exemplo de uso para gerenciamento de usuários
criar_usuario('admin', 'admin123', 'gerente')
criar_usuario('funcionario', 'func123', 'funcionario')
listar_usuarios()
atualizar_usuario('funcionario', nova_senha='func456')
deletar_usuario('admin')
listar_usuarios()

# Exemplo de uso para gerenciamento de produtos
criar_produto('Telescópio', 1500.00, 10)
criar_produto('Luneta', 300.00, 15)
listar_produtos()
atualizar_produto('Telescópio', novo_preco=1400.00)
deletar_produto('Luneta')
listar_produtos()
buscar_produto('Telescópio')
listar_produtos_ordenados_por_nome()
listar_produtos_ordenados_por_preco()