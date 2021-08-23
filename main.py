from dados import Dados

agenda = []

print("*"*18)
print("Agenda telefonica")
print("*"*18)

while True:
    print("1 - Cadastrar contato;")
    print("2 - Listar contatos;")
    print("3 - Apagar contato;")
    print("4 - Adicionar tarefa;")
    print("5 - Listar tarefas;")
    print("6 - Apagar tarefa;")
    print("7 - Sair.")

    opcao = int(input("Escolha a opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o numero de telefone: ")
        agenda.append(Dados.inserir(nome, telefone))
    elif opcao == 2:
        Dados.listarTodos(agenda)
    elif opcao == 3:
        nome = input("Digite o nome do contato: ")
        print(Dados.deletarContato(agenda, nome))
    elif opcao == 4:
        nome = input("Qual tarefa deseja adicionar? ")
        conclusao = input("A tarefa já foi concluida? ")
        continue
        agenda.append(Dados.criarTarefa(conclusao))
    elif opcao == 5:
        print(Dados.listarTarefas(agenda))
    elif opcao == 6:
        nome = input("Qual tarefa deseja apagar? ")
        print(Dados.deletarTarefa(agenda, nome))
    elif opcao == 7:
        break
    else:
        print("Digite a opção correta")
