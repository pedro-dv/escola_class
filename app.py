from escola import Escola
from aluno import Aluno
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App:
    def __init__(self, nome: str):
        self.escola = Escola(nome)

        self.janela = Tk()
        self.janela.title(f"Sistema - {self.escola.nome}")

        # Label
        self.label__matricula = Label(self.janela, text="Matricula", font="Tahoma 14 bold", fg="red")
        self.label__matricula.grid(row=0, column=0)
        # Entry
        self.txt__matricula = Entry(self.janela, font="Tahoma 14", width=27, bg="lightgray", state=DISABLED)
        self.txt__matricula.grid(row=0, column=1)

        # Label
        self.label__nome = Label(self.janela, text="nome", font="Tahoma 15 bold", fg="red")
        self.label__nome.grid(row=1, column=0)
        # Entry
        self.txt__nome = Entry(self.janela, font="Tahoma 14", width=27, bg="lightgray")
        self.txt__nome.grid(row=1, column=1)

        # Label
        self.label__idade = Label(self.janela, text="idade", font="Tahoma 15 bold", fg="red")
        self.label__idade.grid(row=2, column=0)
        # Entry
        self.txt__idade = Entry(self.janela, font="Tahoma 14", width=27, bg="lightgray")
        self.txt__idade.grid(row=2, column=1)

        self.cursos = ["python", "javascript", "Node", "C++"]
        self.label__curso = Label(self.janela, text="Curso: ", font="Tahoma 14 bold", fg="red")
        self.label__curso.grid(row=3, column=0)

        # Combobox - (caixa de seleção)
        self.combo_cursos = ttk.Combobox(self.janela, values=self.cursos, width=25, state='readonly')
        self.combo_cursos.grid(row=3, column=1)

        # Label
        self.label__nota = Label(self.janela, text="nota", font="Tahoma 15 bold", fg="red")
        self.label__nota.grid(row=4, column=0)
        # Entry
        self.txt__nota = Entry(self.janela, font="Tahoma 14", width=27, bg="lightgray")
        self.txt__nota.grid(row=4, column=1)

        # Botao ------------------------------------------
        self.button_adicionar = Button(self.janela, text="Adicionar", font="Tahoma 12 bold", width=7, bg="green",
                                       command=self.cadastrarAluno)
        self.button_adicionar.grid(row=5, column=0)

        self.button_editar = Button(self.janela, text="Editar", font="Tahoma 12 bold", width=7, bg="yellow")
        self.button_editar.grid(row=5, column=1)

        self.button_excluir = Button(self.janela, text="Excluir", font="Tahoma 12 bold", width=7, bg="red",
                                     command=self.deletarAluno)
        self.button_excluir.grid(row=5, column=2)

        # frame - (Espaço na tabela)
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3)

        self.colunas = ["matricula", "Nome", "Idade", "Curso", "Nota"]
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show="headings")
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110)

        self.tabela.bind("<ButtonRelease-1>", self.selecionarAluno)
        self.tabela.pack()

        self.atualizarTabela()
        self.janela.mainloop()

    def cadastrarAluno(self):
        nome = self.txt__nome.get()
        idade = int(self.txt__idade.get())
        curso = self.combo_cursos.get()
        nota = float(self.txt__nota.get())
        aluno = Aluno(nome, idade, curso, nota)

        self.escola.alunos.append(aluno)
        messagebox.showinfo("Sucesso!", "Aluno cadastrado com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def limparCampos(self):
        self.txt__matricula.config(state=NORMAL)
        self.txt__matricula.delete(0, END)
        self.txt__matricula.config(state=DISABLED)
        self.txt__nome.delete(0, END)
        self.txt__idade.delete(0, END)
        self.combo_cursos.set('')
        self.txt__nota.delete(0, END)

    def atualizarTabela(self):
        for linha in self.tabela.get_children():
            self.tabela.delete(linha)
        for aluno in self.escola.alunos:
            self.tabela.insert("", END, values=(aluno.matricula,
                                                aluno.nome,
                                                aluno.idade,
                                                aluno.curso,
                                                aluno.nota))

    def selecionarAluno(self, event):
        linha_selecionada = self.tabela.selection()[0]
        valores = self.tabela.item(linha_selecionada)["values"]
        self.limparCampos()
        self.txt__matricula.config(state=NORMAL)
        self.txt__matricula.insert(0, valores[0])
        self.txt__matricula.config(state=DISABLED)
        self.txt__nome.insert(0, valores[1])
        self.txt__idade.insert(0, valores[2])
        self.combo_cursos.set(valores[3])
        self.txt__nota.insert(0, valores[4])

    def deletarAluno(self):
        matricula = self.txt__matricula.get()
        opcao = messagebox.askyesno("Deseja remover o aluno?")
        if opcao:
            self.escola.removerAluno(matricula)
            messagebox.showinfo("Sucesso!", "Aluno removido com sucesso!")

        self.limparCampos()
        self.atualizarTabela()


App("Infinity")
