import sqlite3

def connect():
    conn = sqlite3.connect('dados.db')
    return conn

# Função Inserindo Livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)", (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função Inserindo Usuários
def insert_user(nome, sobrenome, sala, endereco, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, sala, endereco, telefone) VALUES (?, ?, ?, ?, ?)", (nome, sobrenome, sala, endereco, telefone))
    conn.commit()
    conn.close()

# Função Exibir livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    
    if not livros:
        print("Não há livros")
        return
    print("Livros da Biblioteca: ")
    for livro in livros:
        print(f"ID: {livro[0]}")
        print(f"Título: {livro[1]}")
        print(f"Autor: {livro[2]}")
        print(f"Editora: {livro[3]}")
        print(f"Ano de publicação: {livro[4]}")
        print(f"ISBN: {livro[5]}")
        print("\n")

# Função Empréstimos de livros
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)", (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função exibir emprestimos
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.id, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                            FROM livros \
                            INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                            INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                            WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

#Função devolução
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()
    



# Exemplo de uso:
#livros_emprestados = get_books_on_loan()
# insert_book("Dom Quixote", "Miguel Carlos", "Editora Aurora", 1958, "999999999")
# insert_user("Cristiano", "Veríssimo", "12", "Ribeirão das Neves - MG", "(31)99473-0351")
# insert_loan(1, 1, "03/11/2023", None)
# exibir_livros()
#print(livros_emprestados)
#update_loan_return_date(1, "04/11/2023")