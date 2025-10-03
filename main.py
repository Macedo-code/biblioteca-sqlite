import sqlite3

conexao = sqlite3.connect("biblioteca.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_livro TEXT NOT NULL,
    autor_livro TEXT NOT NULL,
    ano INTEGER,
    disponibilidade CHAR(1) CHECK(disponibilidade IN('S','N'))
    )
""")

def add_livro(nome_livro,autor_livro,ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO livros(nome_livro, autor_livro, ano, disponibilidade) VALUES (?,?,?,?)""", (nome_livro, autor_livro, ano, "S"))

        conexao.commit()

        if cursor.rowcount > 0:
            print(f"Livro {nome_livro} foi cadastrado com sucesso!")

        else:
            print("Erro ao cadastrar o Livro!")

    except sqlite3.Error as error:
        print("Erro ao cadastrar o livro {error}")

    finally:
        if conexao:
            conexao.close()

def lista_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for line in cursor.fetchall():
            print(f"ID: {line[0]} | Título: {line[1]} | Autor: {line[2]} | Ano: {line[3]} | Disponibilidade: {line[4]}")

    except sqlite3.Error as error:
        print(f"Erro ao listar o livro {error}")
    finally:
        if conexao:
            conexao.close

def atualizar_disp(id_livro, new_disp):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        UPDATE livros SET disponibilidade = ? WHERE id = ?""", 
        (new_disp, id_livro))

        conexao.commit()

        if cursor.rowcount > 0:
            print(f"ID:{id_livro} foi alterada!")

        else:
            print(f"Nenhum livro cadastrado com esse ID: {id_livro}")
    
    except sqlite3.error as error:
        print(f"erro ao tentar alterar disponibilidade", {error})

    finally:
        if conexao:
            conexao.close()

def remover_livro(id_livro):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE id =?", (id_livro,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Livro deletado com sucesso!")

        else:
            print("Nenhum Livro cadastrado com ID fornecido!")
    
    except sqlite3.Error as error:
        print(f"Erro ao tentar deletar o Livro",{error})

    finally:
        if conexao:
            conexao.close()