import sqlite3
conexao = sqlite3.connect('dados.db')

# Tabela de Livros
conexao.execute('''CREATE TABLE livros(
                    id INTEGER PRIMARY KEY,
                    titulo TEXT,
                    autor TEXT,
                    editora TEXT,
                    ano_publicacao INTEGER,
                    isbn TEXT)''')

# Tabela de Usuários
conexao.execute('''CREATE TABLE usuarios(
                    id INTEGER PRIMARY KEY,
                    nome TEXT,
                    sobrenome TEXT,
                    sala TEXT,
                    endereco TEXT,
                    telefone TEXT)''')

# Tabela de Empréstimos
conexao.execute('''CREATE TABLE emprestimos(
                    id INTEGER PRIMARY KEY,
                    id_livro INTEGER,
                    id_usuario INTEGER,
                    data_emprestimo TEXT,
                    data_devolucao TEXT,
                    FOREIGN KEY(id_livro) REFERENCES livros(id),
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id))''')