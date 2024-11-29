import json
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview

class Aluno:
    def __init__(self, nome, matricula, email, curso):
        self.__nome = nome
        self.__matricula = matricula
        self.__email = email
        self.__curso = curso
        self.__notas = []
        
    def adicionar_notas(self, notas):
        notas_validas = True
        for nota in notas:
            if 0 <= nota <= 10:
                self.__notas.append(nota)
            else:
                notas_validas = False
                if not notas_validas:
                    print("Tente notas entre 0 e 10")

    def calcular_media(self):
        return sum(self.__notas) / len(self.__notas) if self.__notas else 0
    
    def __str__(self):
        return f"Nome: {self.__nome}, Matrícula: {self.__matricula}, Email: {self.__email}, Curso: {self.__curso}, Notas: {self.__notas}, Média: {self.calcular_media()}"
    
    def lista(self):
        return [self.__nome, self.__matricula, self.__email, self.__curso, ' '.join(map(str, self.__notas)), self.calcular_media()]

    @property
    def matricula(self):
        return self.__matricula

class Gerenciamento_Alunos:
    def __init__(self):
        self.__alunos = []
    
    def cadastrar_aluno(self, nome, matricula, email, curso, notas):
        aluno = Aluno(nome, matricula, email, curso)
        aluno.adicionar_notas(notas)
        self.__alunos.append(aluno)
    
    def buscar_aluno(self, matricula):
        for aluno in self.__alunos:
            if aluno.matricula == matricula:
                return aluno
        return None
    
    def editar_aluno(self, matricula, nome=None, email=None, curso=None, notas=None):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            if nome:
                aluno._Aluno__nome = nome
            if email:
                aluno._Aluno__email = email
            if curso:
                aluno._Aluno__curso = curso
            if notas is not None:
                aluno._Aluno__notas = []
                aluno.adicionar_notas(notas)
            return True
        return False
    
    def excluir_aluno(self, matricula):
        aluno = self.buscar_aluno(matricula)
        if aluno:
            self.__alunos.remove(aluno)
            return True
        return False
    
    def get_alunos(self):
        return self.__alunos

class Alunos(tb.Frame):
    def __init__(self, menu):
        super().__init__(menu, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)
        self.nome_aluno = tb.StringVar(value="")
        self.matricula_aluno = tb.StringVar(value="")
        self.email_aluno = tb.StringVar(value="")
        self.notas_aluno = tb.StringVar(value="")
        self.curso_aluno = tb.StringVar(value="")
        self.gerenciador = Gerenciamento_Alunos()
        self.colors = menu.style.colors

        title = tb.Label(self, text="Gerenciamento de Alunos", font=("Helvetica", 25))
        title.pack(pady=(10))

        self.entrada("Nome:", self.nome_aluno)
        self.entrada("Matricula:", self.matricula_aluno)
        self.entrada("Email:", self.email_aluno)
        self.entrada("Curso:", self.curso_aluno)
        self.entrada("Notas(separadas por espaço)", self.notas_aluno)

        self.menu_bt()
        self.tabela = self.criar_tabela()

        self.carregar_dados()

    def entrada(self, rotulo, variable):
        entrada_campos = tb.Frame(self)
        entrada_campos.pack(fill=X, expand=YES, padx=5, pady=5)

        entrada_rotulo = tb.Label(master=entrada_campos, text=rotulo, width=25)
        entrada_rotulo.pack(side=LEFT, padx=12)

        entrada_usuario = tb.Entry(master=entrada_campos, textvariable=variable)
        entrada_usuario.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return entrada_usuario

    def menu_bt(self):
        caixa_bt = tb.Frame(self)
        caixa_bt.pack(fill=X, expand=YES, pady=(15,10))

        cadastrar_bt = tb.Button(master=caixa_bt, text="Enviar", command=self.cadastrar_aluno, bootstyle=SUCCESS, width=6)
        cadastrar_bt.pack(side=LEFT, padx=5)

        editar_bt = tb.Button(master=caixa_bt, text="Editar", command=self.open_edit_window, bootstyle=INFO, width=6)
        editar_bt.pack(side=LEFT, padx=5)

        deletar_bt = tb.Button(master=caixa_bt, text="Excluir", command=self.deletar, bootstyle=DANGER, width=6)
        deletar_bt.pack(side=LEFT, padx=5)

        sair_bt = tb.Button(master=caixa_bt, text="Sair", command=self.sair, bootstyle=DANGER, width=6)
        sair_bt.pack(side=LEFT, padx=5)

    def cadastrar_aluno(self):
        nome = self.nome_aluno.get()
        matricula = self.matricula_aluno.get()
        email = self.email_aluno.get()
        notas_str = self.notas_aluno.get()
        curso = self.curso_aluno.get()

        try:
            notas = list(map(float, notas_str.split()))
        except ValueError as e:
            ToastNotification(title="Erro", message=f"Erro ao processar notas: {e}", duration=3000).show_toast()
            return

        if nome and matricula and email and curso:
            if any(aluno.lista()[1] == matricula for aluno in self.gerenciador.get_alunos()):
                ToastNotification(title="Erro", message="A matrícula já está sendo utilizada.", duration=3000).show_toast()
                return

            self.gerenciador.cadastrar_aluno(nome, matricula, email, curso, notas)
            self.salvar_dados()
            ToastNotification(title="Aluno Salvo", message="Seus Dados foram Salvos", duration=3000).show_toast()
            self.atualizar_tabela()
        else:
            ToastNotification(title="Erro", message="Tente novamente preenchendo todos os campos", duration=3000).show_toast()

    def sair(self):
        self.quit()

    def deletar(self):
        deletar_m = deletar_mn(self, self.gerenciador)
        deletar_m.grab_set()

    def open_edit_window(self):
        edit_window = editar_mn(self, self.gerenciador)
        edit_window.grab_set()

    def criar_tabela(self):
        coldata = [
            {"text": "Nome"},
            {"text": "Matricula"},
            {"text": "Email"},
            {"text": "Curso"},
            {"text": "Notas"},
            {"text": "Média"},
        ]
        rowdata = [aluno.lista() for aluno in self.gerenciador.get_alunos()]
        tabela = Tableview(
            master=self,
            coldata=coldata,
            rowdata=rowdata,
            paginated=TRUE,
            searchable=TRUE,
            bootstyle="light",
            stripecolor=(self.colors.light, None))
        
        tabela.pack(fill=BOTH, expand=YES, pady=10)
        return tabela

    def atualizar_tabela(self):
        self.tabela.destroy()
        self.tabela = self.criar_tabela()

    def salvar_dados(self):
        with open('alunos.json', 'w') as f:
            json.dump([aluno.lista() for aluno in self.gerenciador.get_alunos()], f, indent=4)

    def carregar_dados(self):
        try:
            with open('alunos.json', 'r') as f:
                dados = json.load(f)
                for aluno in dados:
                    self.gerenciador.cadastrar_aluno(aluno[0], aluno[1], aluno[2], aluno[3], list(map(float, aluno[4].split())))
                self.atualizar_tabela()
        except FileNotFoundError:
            pass

class editar_mn(tb.Toplevel):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)
        self.title("Editar Aluno")
        self.geometry("800x600")
        self.parent = parent
        self.gerenciador = gerenciador

        self.matricula_v = tb.StringVar()

        tb.Label(self, text="Digite a matrícula do aluno a ser editado:").pack(pady=10)

        matricula_entry = tb.Entry(self, textvariable=self.matricula_v)
        matricula_entry.pack(pady=5, padx=10, fill=X)

        self.nome_var = tb.StringVar()
        self.email_var = tb.StringVar()
        self.curso_var = tb.StringVar()
        self.notas_var = tb.StringVar()

        tb.Button(self, text="Buscar", command=self.pesquisa).pack(pady=10)

    def pesquisa(self):
        matricula = self.matricula_v.get()
        aluno = self.gerenciador.buscar_aluno(matricula)
        if aluno:
            self.nome_var.set(aluno._Aluno__nome)
            self.email_var.set(aluno._Aluno__email)
            self.curso_var.set(aluno._Aluno__curso)
            self.notas_var.set(' '.join(map(str, aluno._Aluno__notas)))
            self.campos_editar()
        else:
            ToastNotification(title="Erro", message="Matrícula não encontrada.", duration=3000).show_toast()

    def campos_editar(self):
        tb.Label(self, text="Nome:").pack(pady=5)
        tb.Entry(self, textvariable=self.nome_var).pack(pady=5, fill=X)

        tb.Label(self, text="Email:").pack(pady=5)
        tb.Entry(self, textvariable=self.email_var).pack(pady=5, fill=X)

        tb.Label(self, text="Curso:").pack(pady=5)
        tb.Entry(self, textvariable=self.curso_var).pack(pady=5, fill=X)

        tb.Label(self, text="Notas (separadas por espaços):").pack(pady=5)
        tb.Entry(self, textvariable=self.notas_var).pack(pady=5, fill=X)

        tb.Button(self, text="Salvar", command=self.salvar_editar).pack(pady=10)
        tb.Button(self, text="Fechar", command=self.destroy, bootstyle=DANGER).pack(pady=10)

    def salvar_editar(self):
        nome = self.nome_var.get()
        email = self.email_var.get()
        notas_str = self.notas_var.get()
        curso = self.curso_var.get()

        try:
            notas = list(map(float, notas_str.split()))
        except ValueError as e:
            ToastNotification(title="Erro", message=f"Erro ao processar notas: {e}", duration=3000).show_toast()
            return

        matricula = self.matricula_v.get()
        if self.gerenciador.editar_aluno(matricula, nome, email, curso, notas):
            self.parent.salvar_dados()
            self.parent.atualizar_tabela()
            ToastNotification(title="Aluno Editado", message="Os dados do aluno foram editados com sucesso.", duration=3000).show_toast()
            self.destroy()
        else:
            ToastNotification(title="Erro", message="Matrícula não encontrada.", duration=3000).show_toast()

class deletar_mn(tb.Toplevel):
    def __init__(self, parent, gerenciador):
        super().__init__(parent)
        self.title("Excluir Aluno")
        self.geometry("600x400")
        self.parent = parent
        self.gerenciador = gerenciador

        tb.Label(self, text="Insira a matrícula do aluno:").pack(pady=10)

        self.matricula_v = tb.StringVar()
        entry = tb.Entry(self, textvariable=self.matricula_v)
        entry.pack(pady=5, padx=10, fill=X)

        tb.Button(self, text="Excluir", command=self.on_delete).pack(pady=10)
        tb.Button(self, text="Fechar", command=self.destroy, bootstyle=DANGER).pack(pady=10)

    def on_delete(self):
        matricula = self.matricula_v.get()
        if self.gerenciador.excluir_aluno(matricula):
            self.parent.salvar_dados()
            self.parent.atualizar_tabela()
            ToastNotification(title="Aluno Excluído", message="O aluno foi excluído com sucesso.", duration=3000).show_toast()
            self.destroy()
        else:
            ToastNotification(title="Erro", message="Matrícula não encontrada.", duration=3000).show_toast()

if __name__ == "__main__":
    app = tb.Window("Gerenciamento de Alunos", "darkly", resizable=(False, False))
    Alunos(app)
    app.mainloop()
