# G.E.Y.S.I

# Descrição do Projeto
Este código implementa um sistema de gestão de biblioteca usando a biblioteca Tkinter para a interface gráfica, o Tkcalendar para seleção de datas, e o SQLite para o banco de dados. O sistema permite a criação de novos usuários, a inserção de novos livros, a#  visualização de todos os livros, a realização de empréstimos, a devolução de livros emprestados e a visualização de livros atualmente emprestados.

# Descrição Geral
Este código implementa um sistema de gestão de biblioteca usando a biblioteca Tkinter para a interface gráfica, o Tkcalendar para seleção de datas, e o SQLite para o banco de dados. O sistema permite a criação de novos usuários, a inserção de novos livros, a visualização de todos os livros, a realização de empréstimos, a devolução de livros emprestados e a visualização de livros atualmente emprestados.

# Modulos e Dependências
O código faz uso das seguintes bibliotecas e módulos:

tkinter: Biblioteca para criação de interfaces gráficas.
ttk: Módulo Tkinter que provê acesso a widgets temáticos.
PIL: Biblioteca Python Imaging Library para manipulação de imagens.
tkcalendar: Widget de calendário para Tkinter.
datetime: Módulo para manipulação de datas e horas.

# Configuração de Cores
As cores utilizadas no sistema estão definidas no início do código para facilitar a personalização. As variáveis como cor1, cor2, etc., representam códigos hexadecimais de cores.

# Estrutura da Interface
O sistema possui uma interface gráfica dividida em três frames:

Frame do Logo: Exibe o logo da biblioteca.
Frame do Menu: Contém botões para acessar diferentes funcionalidades do sistema.
Frame de Visualização dos Dados: Exibe as informações conforme a funcionalidade selecionada.

# Funcionalidades Principais
Novo Usuário (novo_usuario)
Permite a criação de um novo usuário. O usuário deve inserir informações como primeiro nome, sobrenome, sala, endereço e telefone.

Novo Livro (novo_livro)
Permite a inserção de informações sobre um novo livro, como título, autor, editora, ano e ISBN.

Ver Livros (ver_livros)
Apresenta uma tabela com todos os livros cadastrados na biblioteca, exibindo informações como ID, título, autor, editora, ano e ISBN.

Ver Usuários (ver_usuarios)
Exibe uma tabela com todos os usuários cadastrados na biblioteca, mostrando informações como ID, nome, sobrenome, sala, endereço e telefone.

Realizar Empréstimo (realizar_emprestimo)
Permite a realização de empréstimos de livros. O usuário deve fornecer o ID do usuário e o ID do livro.

Devolução de Empréstimo (devolucao_emprestimo)
Possibilita a atualização da data de devolução de um livro emprestado. O usuário deve fornecer o ID do empréstimo e a nova data de devolução.

Ver Livros Emprestados (ver_livros_emprestados)
Apresenta uma tabela com todos os livros atualmente emprestados, mostrando informações como ID, título, usuário, data de saída e data de devolução prevista.

# Menu de Navegação
O sistema conta com um menu à esquerda que permite a navegação entre as diferentes funcionalidades. Cada botão do menu chama a função correspondente.

# Estrutura do Banco de Dados
O sistema utiliza um banco de dados SQLite para armazenar informações sobre usuários, livros e empréstimos. As funções insert_user, insert_book, insert_loan, update_loan_return_date, get_books, get_users e get_books_on_loan interagem com o banco de dados.

# Observações
Imagens utilizadas no sistema (logo_livros.png, add_user.png, etc.) devem estar presentes no diretório do código para que a interface funcione corretamente.
As datas são manipuladas em formato de string no padrão "AAAA-MM-DD".

# Autor
Cristiano Verissimo - Ano: 2023

# GitHub
O código-fonte está disponível em https://github.com/CristianoVerissimo.

# Ambiente de Desenvolvimento
Python 3.x
Bibliotecas: tkinter, ttk, PIL, tkcalendar
