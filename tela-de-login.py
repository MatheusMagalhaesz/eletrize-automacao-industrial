import csv
from tkinter import *
from tkinter import messagebox

colors = {'c0': "#000000", 'c1': "#feffff"}

# Criando tela de login
tela = Tk()
tela.title('Gestão de Manutenção')
tela.geometry("310x300")
tela.configure(background=colors['c0'])
tela.resizable(width=FALSE, height=FALSE)

# Separação das telas
frame_cima = Frame(tela, width=310, height=50, bg=colors['c0'], relief='flat')
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(tela, width=310, height=250, bg=colors['c0'], relief='flat')
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configuração do frame_cima

label_nome = Label(frame_cima, text='LOGIN DO COLABORADOR', anchor=NE, font='Ivy 16', bg=colors['c0'],
                   fg=colors['c1'])
label_nome.place(x=5, y=5)

label_separate = Label(frame_cima, text='', width=275, anchor=NW, font='Ivy 1', bg=colors['c1'], fg=colors['c1'])
label_separate.place(x=10, y=45)


def verifica_senha():
    try:
        with open("./arquivos-uteis/lista-de-usuarios.csv") as arquivo:
            leitor_csv = csv.reader(arquivo)
            for linha in leitor_csv:
                id_usuario, senha = linha
                if entry_nome.get() == id_usuario and entry_senha.get() == senha:
                    messagebox.showinfo('Login', 'Seja Bem-Vindo!')
                    return
    except FileNotFoundError:
        messagebox.showerror('Erro', 'Arquivo não encontrado.')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro na leitura do arquivo: {e}')

    messagebox.showwarning('Acesso Negado', 'Verifique seu acesso!')


# Configuração do frame_baixo

label_nome = Label(frame_baixo, text='ID COLABORADOR *', anchor=NE, font='Ivy 10', bg=colors['c0'], fg=colors['c1'])
label_nome.place(x=10, y=20)
entry_nome = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
entry_nome.place(x=14, y=50)

label_senha = Label(frame_baixo, text='SENHA DE AUTENTICAÇÃO *', anchor=NE, font='Ivy 10', bg=colors['c0'],
                    fg=colors['c1'])
label_senha.place(x=10, y=95)
entry_senha = Entry(frame_baixo, width=25, justify='left', show='*', font=("", 15), highlightthickness=1, relief='solid')
entry_senha.place(x=14, y=130)

button_confirmar = Button(frame_baixo, command=verifica_senha, text='ENTRAR', width=39, height=2, bg=colors['c1'],
                          font='Ivy 8 bold', fg=colors['c0'], relief=RAISED, overrelief=RIDGE)
button_confirmar.place(x=15, y=180)

# Run da tela
tela.mainloop()
