class Telefone():
    def __init__(self, contato, telefone):
        self.__contato = contato
        self.__telefone = telefone

    def getContato(self):
        return self.__contato

    def getTelefone(self):
        return self.__telefone

    def __init__(self, tarefa):
        self.__tarefa = tarefa

    def getTarefa(self):
        return self.__tarefa
