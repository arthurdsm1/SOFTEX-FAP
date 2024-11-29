import ttkbootstrap as tb
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tableview import Tableview
from datetime import datetime
import json


class Tarefa:
    def __init__(self, descricao, data_inicio, data_fim, status, observacao, prioridade):
        self.__descricao = descricao
        self.__data_inicio = data_inicio
        self.__data_fim = data_fim
        self.__status = status
        self.__observacao = observacao
        self.__prioridade = prioridade
   
    def lista(self):
        return [self.__descricao, self.__data_inicio, self.__data_fim, self.__status, self.__observacao, self.__prioridade]


class Gerenciamento_Tarefas:
    def __init__(self):
        self.__tarefas = []
    
    def is_valid_date(self, date_string, date_format="%d/%m/%Y"):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False
        
   
    def cadastrar_tarefa(self, descricao, data_inicio, data_fim, status, observacao, prioridade):
        tarefa = Tarefa(descricao, data_inicio, data_fim, status, observacao, prioridade)
        self.__tarefas.append(tarefa)
   
    def buscar_tarefa(self, descricao):
        for tarefa in self.__tarefas:
            if tarefa.lista()[0] == descricao:
                return tarefa
        return None
   
    def editar_tarefa(self, descricao, nova_descricao=None, nova_data_inicio=None, nova_data_fim=None, novo_status=None, nova_observacao=None, nova_prioridade=None):
        tarefa = self.buscar_tarefa(descricao)
        if tarefa:
            if nova_descricao:
                tarefa._Tarefa__descricao = nova_descricao
            if nova_data_inicio:
                tarefa._Tarefa__data_inicio = nova_data_inicio
            if nova_data_fim:
                tarefa._Tarefa__data_fim = nova_data_fim
            if novo_status is not None:
                tarefa._Tarefa__status = novo_status
            if nova_observacao:
                tarefa._Tarefa__observacao = nova_observacao
            if nova_prioridade:
                tarefa._Tarefa__prioridade = nova_prioridade
            return True
        return False
   
    def excluir_tarefa(self, descricao):
        tarefa = self.buscar_tarefa(descricao)
        if tarefa:
            self.__tarefas.remove(tarefa)
            return True
        return False
   
    def get_tarefas(self):
        return self.__tarefas


class Tarefas(tb.Frame):
    def __init__(self, app):
        super().__init__(app, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)
        self.descricao_tarefa = tb.StringVar(value="")
        self.data_inicio_tarefa = tb.StringVar(value="")
        self.data_fim_tarefa = tb.StringVar(value="")
        self.status_tarefa = tb.BooleanVar(value=False)
        self.observacao_tarefa = tb.StringVar(value="")
        self.prioridade_tarefa = tb.StringVar(value="")
        self.gerenciador = Gerenciamento_Tarefas()
        self.colors = app.style.colors

        title = tb.Label(self, text="Gerenciamento de Tarefas", font=("Helvetica", 25))
        title.pack(pady=(10))

        self.entrada("Descrição:", self.descricao_tarefa)
        self.entrada("Data de Início:", self.data_inicio_tarefa)
        self.entrada("Data de Fim:", self.data_fim_tarefa)
        self.entrada("Status (0 ou 1):", self.status_tarefa)
        self.entrada("Observação:", self.observacao_tarefa)
        self.entrada("Prioridade:", self.prioridade_tarefa)

        self.app_bt()
        self.tabela = self.criar_tabela()

        self.carregar_dados()

    def entrada(self, rotulo, var):
        entrada_campos = tb.Frame(self)
        entrada_campos.pack(fill=X, expand=YES, padx=5, pady=5)

        entrada_rotulo = tb.Label(master=entrada_campos, text=rotulo, width=25)
        entrada_rotulo.pack(side=LEFT, padx=12)

        entrada_usuario = tb.Entry(master=entrada_campos, textvar=var)
        entrada_usuario.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return entrada_usuario

    def app_bt(self):
        caixa_bt = tb.Frame(self)
        caixa_bt.pack(fill=X, expand=YES, pady=(15,10))

        cadastrar_bt = tb.Button(master=caixa_bt, text="Cadastrar", command=self.cadastrar_tarefa, bootstyle=SUCCESS, width=10)
        cadastrar_bt.pack(side=LEFT, padx=5)

        editar_bt = tb.Button(master=caixa_bt, text="Editar", command=self.editar, bootstyle=INFO, width=10)
        editar_bt.pack(side=LEFT, padx=5)

        deletar_bt = tb.Button(master=caixa_bt, text="Excluir", command=self.deletar, bootstyle=DANGER, width=10)
        deletar_bt.pack(side=LEFT, padx=5)

        limpar_bt = tb.Button(master=caixa_bt, text="Limpar", command=self.limpar, bootstyle=WARNING, width=10)
        limpar_bt.pack(side=LEFT, padx=5)

    def cadastrar_tarefa(self):
        descricao = self.descricao_tarefa.get()
        data_inicio = self.data_inicio_tarefa.get()
        data_fim = self.data_fim_tarefa.get()
        status = bool(int(self.status_tarefa.get()))
        observacao = self.observacao_tarefa.get()
        prioridade = self.prioridade_tarefa.get()

        if descricao and data_inicio and data_fim and observacao and prioridade:
            if not self.gerenciador.is_valid_date(data_inicio):
                ToastNotification(title="Erro", message="Data invalida.", duration=3000).show_toast()
                return
            if not self.gerenciador.is_valid_date(data_fim):
                ToastNotification(title="Erro", message="Data invalida.", duration=3000).show_toast()
                return

            if any(tarefa.lista()[0] == descricao for tarefa in self.gerenciador.get_tarefas()):
                ToastNotification(title="Erro", message="A tarefa já está cadastrada.", duration=3000).show_toast()
                return

            self.gerenciador.cadastrar_tarefa(descricao, data_inicio, data_fim, status, observacao, prioridade)
            self.salvar_dados()
            ToastNotification(title="Tarefa Salva", message="Tarefa cadastrada com sucesso.", duration=3000).show_toast()
            self.atualizar_tabela()
        else:
            ToastNotification(title="Erro", message="Preencha todos os campos.", duration=3000).show_toast()

    def limpar(self):
        self.descricao_tarefa.set("")
        self.data_inicio_tarefa.set("")
        self.data_fim_tarefa.set("")
        self.status_tarefa.set(0)
        self.observacao_tarefa.set("")
        self.prioridade_tarefa.set("")

    def deletar(self):
        deletar_m = DeletarTarefa(self, self.gerenciador)
        deletar_m.grab_set()

    def editar(self):
        editar_m = EditarTarefa(self, self.gerenciador)
        editar_m.grab_set()

    def criar_tabela(self):
        coldata = [
            {"text": "Descrição"},
            {"text": "Data de Início"},
            {"text": "Data do Fim"},
            {"text": "Status"},
            {"text": "Observação"},
            {"text": "Prioridade"},
        ]
        rowdata = [tarefa.lista() for tarefa in self.gerenciador.get_tarefas()]
        tabela = Tableview(
            master=self,
            coldata=coldata,
            rowdata=rowdata,
            autoalign=TRUE,
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
        with open('tarefas.json', 'w') as f:
            json.dump([tarefa.lista() for tarefa in self.gerenciador.get_tarefas()], f, indent=4)

    def carregar_dados(self):
        try:
            with open('tarefas.json', 'r') as f:
                dados = json.load(f)
                for tarefa in dados:
                    self.gerenciador.cadastrar_tarefa(tarefa[0], tarefa[1], tarefa[2], tarefa[3], tarefa[4], tarefa[5])
                self.atualizar_tabela()
        except FileNotFoundError:
            pass


class EditarTarefa(tb.Toplevel):
    def __init__(self, mestre, gerenciador):
        super().__init__(mestre)
        self.title("Editar Tarefa")
        self.geometry("800x600")
        self.mestre = mestre
        self.gerenciador = gerenciador

        self.descricao_v = tb.StringVar()

        tb.Label(self, text="Digite a descrição da tarefa:").pack(pady=10)

        descricao_entry = tb.Entry(self, textvar=self.descricao_v)
        descricao_entry.pack(pady=5, padx=10, fill=X)

        self.data_inicio_var = tb.StringVar()
        self.data_fim_var = tb.StringVar()
        self.status_var = tb.BooleanVar()
        self.observacao_var = tb.StringVar()
        self.prioridade_var = tb.StringVar()

        tb.Button(self, text="Buscar", command=self.pesquisa).pack(pady=10)

    def pesquisa(self):
        descricao = self.descricao_v.get()
        tarefa = self.gerenciador.buscar_tarefa(descricao)
        if tarefa:
            self.data_inicio_var.set(tarefa._Tarefa__data_inicio)
            self.data_fim_var.set(tarefa._Tarefa__data_fim)
            self.status_var.set(tarefa._Tarefa__status)
            self.observacao_var.set(tarefa._Tarefa__observacao)
            self.prioridade_var.set(tarefa._Tarefa__prioridade)

            self.mostrar_campos_edicao()
        else:
            ToastNotification(title="Erro", message="Tarefa não encontrada.", duration=3000).show_toast()

    def mostrar_campos_edicao(self):
        tb.Label(self, text="Data de Início:").pack(pady=5)
        tb.Entry(self, textvar=self.data_inicio_var).pack(pady=5, padx=10, fill=X)

        tb.Label(self, text="Data de Fim:").pack(pady=5)
        tb.Entry(self, textvar=self.data_fim_var).pack(pady=5, padx=10, fill=X)

        tb.Label(self, text="Status (0 ou 1):").pack(pady=5)
        tb.Entry(self, textvar=self.status_var).pack(pady=5, padx=10, fill=X)

        tb.Label(self, text="Observação:").pack(pady=5)
        tb.Entry(self, textvar=self.observacao_var).pack(pady=5, padx=10, fill=X)

        tb.Label(self, text="Prioridade:").pack(pady=5)
        tb.Entry(self, textvar=self.prioridade_var).pack(pady=5, padx=10, fill=X)

        tb.Button(self, text="Salvar", command=self.salvar_edicao).pack(pady=20)

    def salvar_edicao(self):
        descricao = self.descricao_v.get()
        nova_data_inicio = self.data_inicio_var.get()
        nova_data_fim = self.data_fim_var.get()
        novo_status = bool(int(self.status_var.get()))
        nova_observacao = self.observacao_var.get()
        nova_prioridade = self.prioridade_var.get()

        sucesso = self.gerenciador.editar_tarefa(descricao, nova_data_inicio=nova_data_inicio, nova_data_fim=nova_data_fim, novo_status=novo_status, nova_observacao=nova_observacao, nova_prioridade=nova_prioridade)
        if sucesso:
            self.mestre.salvar_dados()
            self.mestre.atualizar_tabela()
            ToastNotification(title="Sucesso", message="Tarefa editada com sucesso.", duration=3000).show_toast()
            self.destroy()
        else:
            ToastNotification(title="Erro", message="Erro ao editar a tarefa.", duration=3000).show_toast()


class DeletarTarefa(tb.Toplevel):
    def __init__(self, mestre, gerenciador):
        super().__init__(mestre)
        self.title("Deletar Tarefa")
        self.geometry("800x600")
        self.mestre = mestre
        self.gerenciador = gerenciador

        self.descricao_v = tb.StringVar()

        tb.Label(self, text="Digite a descrição da tarefa que deseja excluir:").pack(pady=10)

        descricao_entry = tb.Entry(self, textvar=self.descricao_v)
        descricao_entry.pack(pady=5, padx=10, fill=X)

        tb.Button(self, text="Excluir", command=self.deletar_tarefa).pack(pady=10)

    def deletar_tarefa(self):
        descricao = self.descricao_v.get()
        sucesso = self.gerenciador.excluir_tarefa(descricao)
        if sucesso:
            self.mestre.salvar_dados()
            self.mestre.atualizar_tabela()
            ToastNotification(title="Sucesso", message="Tarefa excluída com sucesso.", duration=3000).show_toast()
            self.destroy()
        else:
            ToastNotification(title="Erro", message="Erro ao excluir a tarefa.", duration=3000).show_toast()


class App(tb.Window):
    def __init__(self):
        super().__init__(title="Gerenciamento de Tarefas", themename="superhero", size=(900, 800))
        Tarefas(self)
        self.mainloop()


if __name__ == "__main__":
    App()

