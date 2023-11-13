from tkinter import Tk, ttk
from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from view import *

#Cores
cor0 = "#2e2d2b" #Preto
cor1 = "#feffff" #Branco
cor2 = "#4fa882" #Verde
cor3 = "#38576b" #Valor
cor4 = "#403d3d" #Letra
c0r5 = "#e06636" #-Profit
cor6 = "#E9A178"
cor7 = "#3fbfb9" #Verde
cor8 = "#263238" #Verde
cor9 = "#e9edf5" #Verde
cor10 ="#6e8faf"
cor11 = "#f2f4f2"

#Janela
janela = Tk()
janela.title("Gestão de Biblioteca")
janela.geometry('800x372')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")


#Divisão da janela (FRAMES)
#FRAME LOGO
frameCima = Frame(janela, width=770, height=50, bg=cor6, relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

#FRAME MENU
frameEsquerda = Frame(janela, width=150, height=265, bg=cor4, relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

#FRAME VISUALIZAÇÃO DOS DADOS
frameDireita = Frame(janela, width=600, height=265, bg=cor1, relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)


#Logo
app_img = Image.open('logo_livros.png')
app_img = app_img.resize((50,50))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, anchor=NW, bg=cor2, fg=cor1)
app_logo.place(x=0, y=0)


#Nome APP
app_ = Label(frameCima, text="Gestão de Biblioteca", compound=LEFT, padx=5, anchor=NW, font=('Verdana 18 bold'), bg=cor2, fg=cor1)
app_.place(x=50, y=7)

app_linha = Label(frameCima, width=800, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1 bold'), bg=cor8, fg=cor1)
app_linha.place(x=0, y=47)


#Formulario Criar Usuario
def novo_usuario():
    global img_salvar
    
    def add():
        primeiro_nome = entry_primeiro_nome.get()
        sobrenome = entry_sobrenome.get()
        sala = entry_sala.get()
        endereco = entry_endereco.get()
        telefone = entry_telefone.get()
        
        #Verificando entradas
        lista = [primeiro_nome, sobrenome, sala, endereco, telefone]
        for i in lista:
            if i == '':
                messagebox.showerror('ERRO!', 'Preencha todos os campos.')
                return
        
        #Inserindo usuario no baco de dados
        insert_user(primeiro_nome, sobrenome, sala, endereco, telefone)
        messagebox.showinfo('Sucesso!', 'Usuario inserido com Sucesso!')
        
        #Limpando a tela
        entry_primeiro_nome.delete(0, END)
        entry_sobrenome.delete(0, END)
        entry_sala.delete(0, END)
        entry_endereco.delete(0, END)
        entry_telefone.delete(0, END)
        
        
    
    app_ = Label(frameDireita, text="Criar um novo usuario", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 bold'), bg=cor8, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    
    label_primeiro_nome = Label(frameDireita, text="Primeiro nome*", anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
    label_primeiro_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    entry_primeiro_nome = Entry(frameDireita, width=25, justify='left', relief=SOLID)
    entry_primeiro_nome.grid(row=2, column=1, padx=5, pady=10, sticky=NSEW)
    
    label_sobrenome = Label(frameDireita, text="Sobrenome*", anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
    label_sobrenome.grid(row=3, column=0, padx=5, pady=10, sticky=NSEW)
    entry_sobrenome = Entry(frameDireita, width=25, justify='left', relief=SOLID)
    entry_sobrenome.grid(row=3, column=1, padx=5, pady=10, sticky=NSEW)
    
    label_sala = Label(frameDireita, text="Sala*", anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
    label_sala.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)
    entry_sala = Entry(frameDireita, width=25, justify='left', relief=SOLID)
    entry_sala.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)
    
    label_endereco = Label(frameDireita, text="Endereço*", anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
    label_endereco.grid(row=5, column=0, padx=5, pady=10, sticky=NSEW)
    entry_endereco = Entry(frameDireita, width=25, justify='left', relief=SOLID)
    entry_endereco.grid(row=5, column=1, padx=5, pady=10, sticky=NSEW)
    
    label_telefone = Label(frameDireita, text="Telefone*", anchor=NW, font=('Verdana 10 bold'), bg=cor1, fg=cor4)
    label_telefone.grid(row=6, column=0, padx=5, pady=10, sticky=NSEW)
    entry_telefone = Entry(frameDireita, width=25, justify='left', relief=SOLID)
    entry_telefone.grid(row=6, column=1, padx=5, pady=10, sticky=NSEW)
    
    img_salvar = Image.open('salvar.png')
    img_salvar = img_salvar.resize((20,20))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    botao_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, anchor=NW, text='Salvar', bg=cor1, fg=cor4, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
    botao_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)


#Formulario Lista de Usuarios
def ver_usuarios():
     
    app_ = Label(frameDireita, text="Lista de usuarios", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 12 bold'), bg=cor1, fg=cor4)
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)    
    app_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1 bold'), bg=cor8, fg=cor1)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
    
    dados = get_users()
    
    #Tabela Usuarios
    list_header = ['ID', 'Nome', 'Sobrenome', 'Sala', 'Endereço', 'Telefone']
    
    global tree
    
    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)
    hd=["nw", "nw", "nw", "nw", "nw", "nw"]
    h=[30,120,120,50,130,80,120]
    n=0
    
    for col in list_header:
        tree.heading(col, text=col, anchor=NW)
        tree.column(col, width=h[n], anchor=hd[n])
        n+=1
    
    for item in dados:
        tree.insert('', 'end', values=item)


#Back-end Menu
def control(i):
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_usuario()
    
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_usuarios()


#MENU
#Novo Usuario
img_novo_usuario = Image.open('add_user.png')
img_novo_usuario = img_novo_usuario.resize((20,20))
img_novo_usuario = ImageTk.PhotoImage(img_novo_usuario)
botao_novo_usuario = Button(frameEsquerda, command=lambda:control('novo_usuario'), image=img_novo_usuario, compound=LEFT, anchor=NW, text='Criar Novo Usuario', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_novo_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

#Novo Livro
img_novo_livro = Image.open('add_book.png')
img_novo_livro = img_novo_livro.resize((20,20))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
botao_novo_livro = Button(frameEsquerda, image=img_novo_livro, compound=LEFT, anchor=NW, text='Criar Novo Livro', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

#Ver livros
img_ver_livros = Image.open('logo_livros.png')
img_ver_livros = img_ver_livros.resize((20,20))
img_ver_livros = ImageTk.PhotoImage(img_ver_livros)
botao_ver_livros = Button(frameEsquerda, image=img_ver_livros, compound=LEFT, anchor=NW, text='Exibir Todos Livros', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_ver_livros.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

#Ver lista de livros
img_ver_usuarios = Image.open('users.png')
img_ver_usuarios = img_ver_usuarios.resize((20,20))
img_ver_usuarios = ImageTk.PhotoImage(img_ver_usuarios)
botao_ver_usuarios = Button(frameEsquerda, command=lambda:control('ver_usuarios'), image=img_ver_usuarios, compound=LEFT, anchor=NW, text='Exibir Todos Usuarios', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_ver_usuarios.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

#Realizar emprestimo de livro
img_emprestimo_livro = Image.open('out_book.png')
img_emprestimo_livro = img_emprestimo_livro.resize((20,20))
img_emprestimo_livro = ImageTk.PhotoImage(img_emprestimo_livro)
botao_emprestimo_livro = Button(frameEsquerda, image=img_emprestimo_livro, compound=LEFT, anchor=NW, text='Emprestar Livro', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_emprestimo_livro.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

#Realizar devolucao de livro
img_devolucao_livro = Image.open('return.png')
img_devolucao_livro = img_devolucao_livro.resize((20,20))
img_devolucao_livro = ImageTk.PhotoImage(img_devolucao_livro)
botao_devolucao_livro = Button(frameEsquerda, image=img_devolucao_livro, compound=LEFT, anchor=NW, text='Devolução de Livro', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_devolucao_livro.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

#Livros emprestados
img_livros_emprestados = Image.open('emprestados.png')
img_livros_emprestados = img_livros_emprestados.resize((20,20))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
botao_livros_emprestados = Button(frameEsquerda, image=img_livros_emprestados, compound=LEFT, anchor=NW, text='Livros Emprestados', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
botao_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)





janela.mainloop()
