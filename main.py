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
            