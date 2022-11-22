import sqlite3


def conectar():
    """
    Função para conectar ao servidor
    """
    print('Conectando ao servidor...')
    conn = sqlite3.connect('psqlite3.<user>')
    
    conn.execute("""CREATE TABLE IF NOT EXISTS produtos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL);"""
    )
    return conn


def desconectar(conn):
    """ 
    Função para desconectar do servidor.
    """
    print('Desconectando do servidor...')
    conn.close()


def listar():
    """
    Função para listar os produtos
    """
    print('Listando produtos...')
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    
    produtos = cursor.fetchall()
    
    if len(produtos) > 0:
        print("Listando produtos")
        print("--------")
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Produto: {produto[1]}")
            print(f"Preço: {produto[2]}")
            print(f"Estoque: {produto[3]}")
            print("--------")
    else:
        print("Não existem produtos cadastrados.")
    desconectar(conn)


def inserir():
    """
    Função para inserir um produto
    """  
    print('Inserindo produto...')
    conn = conectar()
    cursor = conn.cursor()
    
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    estoque = int(input("Informe a quantidade em estoque: "))
    
    cursor.execute(f"""INSERT INTO produtos (nome, preco, estoque)
                    VALUES ('{nome}', {preco}, {estoque})"""
    )
    conn.commit()
    
    if cursor.rowcount == 1:
        print(f"O produto {nome} foi inserido com sucesso!")
    else:
        print("Não foi possivel cadastrar o produto.")
    desconectar(conn)


def atualizar():
    """
    Função para atualizar um produto
    """
    print('Atualizando produto...')
    conn = conectar()
    cursor = conn.cursor()
    
    codigo = int(input("Informe o código do produto: "))
    nome = input("Informe o nome do produto: ")
    preco = float(input("Informe o preço do produto: "))
    estoque = int(input("Informe a quantidade em estoque: "))
    
    cursor.execute(f"""UPDATE produtos 
                   SET nome='{nome}', preco={preco}, estoque={estoque}
                   WHERE id={codigo}"""
    )
    conn.commit()
    
    if cursor.rowcount == 1:
        print(f"O produto {nome} foi atualizado com sucesso!")
    else:
        print("Não foi possivel atualizar o produto.")
    desconectar(conn)


def deletar():
    """
    Função para deletar um produto
    """  
    print('Deletando produto...')
    conn = conectar()
    cursor = conn.cursor()
    
    codigo = int(input("Informe o código do produto: "))
    
    cursor.execute(f"""DELETE FROM produtos WHERE id={codigo}""")
    conn.commit()
    
    if cursor.rowcount == 1:
        print(f"O produto excluido com sucesso!")
    else:
        print("Erro ao excluir o produto.")
    desconectar(conn)


def menu():
    while True:
        """
        Função para gerar o menu inicial
        """
        print('=========Gerenciamento de Produtos==============')
        print('Selecione uma opção: ')
        print('1 - Listar produtos.')
        print('2 - Inserir produtos.')
        print('3 - Atualizar produto.')
        print('4 - Deletar produto.')
        print("0 - Sair")
        opcao = int(input())
        if opcao in [1, 2, 3, 4, 0]:
            if opcao == 1:
                listar()
            elif opcao == 2:
                inserir()
            elif opcao == 3:
                atualizar()
            elif opcao == 4:
                deletar()
            elif opcao == 0:
                print("Saindo do menu...")
                exit()
            else:
                print('Opção inválida')
        else:
            print('Opção inválida')
            
    
    menu()
