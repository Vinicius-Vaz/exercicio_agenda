from telefone_tarefa import Telefone

class Dados():
    def inserir(contato, telefone):
        return Telefone(contato, telefone)

    def listarTodos(listaTelefone):
        for tel in listaTelefone:
            print("{} / {}".format(tel.getContato(), tel.getTelefone()))

    def deletarContato(listaTelefone, contato):
        if len(listaTelefone) != 0:
            cont = 0
            for tel in listaTelefone:
                if tel.getContato() == contato:
                    listaTelefone.pop(cont)
                    return "Contato {} excluido".format(contato)
                else:
                    return "Contato não encontrado!"
        else:
            return "Lista está vazia"

    def criarTarefa(tarefa):
        dever = input("Qual tarefa deseja adicionar? ")
        concluida = input("A tarefa foi concluida? ")
        return Telefone(tarefa)
        print("Tarefa adicionada")

    def listarTarefas(listaTarefa):
        for tar in listaTarefa:
            print("{}".format(tar.getTarefa()))

    def deletarTarefa(listaTarefa, tarefa):
        if len(listaTarefa) != 0:
            cont = 0
            for tar in listaTarefa:
                if tar.getTarefa() == tarefa:
                    listaTarefa.pop(cont)
                    return "Tarefa {} foi excluida".format(tarefa)
                else:
                    return "Tarefa não encontrada!"
        else:
            return "Lista de tarefas está vazia"
