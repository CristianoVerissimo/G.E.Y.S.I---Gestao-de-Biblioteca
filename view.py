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
    
#Função Exibir Usuarios
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Função Exibir livros
def get_books():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM livros")
    livros = c.fetchall()
    conn.close()
    return livros

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