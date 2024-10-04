
tasks = []

def addTask():
    task = input('Por favor coloque a tarefa: ')
    tasks.append(task)
    print(f"Tarefa '{task}' adicionada à lista.")

def deleteTask():
    task = input('Por favor, selecione uma tarefa para deletar: ')
    if task in tasks:
        tasks.remove(task)
        print(f"Tarefa '{task}' deletada da lista.")
    else:
        print(f"Tarefa '{task}' não encontrada na lista.")

def listTasks():
    if tasks:
        print("Tarefas na lista:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("A lista de tarefas está vazia.")

if __name__ == '__main__':
    print('Bem-vindo ao aplicativo de lista de tarefas :)')
    while True:
        print('\n')
        print('Por favor, selecione uma das opções abaixo:')
        print('-----------------------------------------')
        print('1. Adicionar uma nova tarefa')
        print('2. Deletar uma tarefa')
        print('3. Listar tarefas')
        print('4. Sair')

        escolha = input('Digite sua escolha: ')

        if escolha == '1':
            addTask()
        elif escolha == '2':
            deleteTask()
        elif escolha == '3':
            listTasks()
        elif escolha == '4':
            print('Adeus (:')
            break
        else:
            print('Entrada inválida, por favor tente novamente.')
