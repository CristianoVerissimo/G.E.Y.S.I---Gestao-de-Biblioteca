from tkinter .ttk import *
from tkinter import *
from PIL import Image, ImageTk


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
janela.geometry('770x372')
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
app_ = Label(frameCima, text="Gestão de Livros", compound=LEFT, padx=5, anchor=NW, font=('Verdana 18 bold'), bg=cor2, fg=cor1)
app_.place(x=50, y=7)

app_linha = Label(frameCima, width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1 bold'), bg=cor8, fg=cor1)
app_linha.place(x=0, y=47)


#MENU
#Novo Usuario
img_novo_usuario = Image.open('add_user.png')
img_novo_usuario = img_novo_usuario.resize((20,20))
img_novo_usuario = ImageTk.PhotoImage(img_novo_usuario)
botao_novo_usuario = Button(frameEsquerda, image=img_novo_usuario, compound=LEFT, anchor=NW, text='Criar Novo Usuario', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
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
botao_ver_usuarios = Button(frameEsquerda, image=img_ver_usuarios, compound=LEFT, anchor=NW, text='Exibir Todos Usuarios', bg=cor4, fg=cor1, font='Ivy 11 bold', overrelief=RIDGE, relief=GROOVE)
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
