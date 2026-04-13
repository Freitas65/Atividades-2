
ARQUIVO_TAREFAS = "tarefas.txt"

print("=== GERENCIADOR DE TAREFAS ===")

# Requisito: Menu em while
while True:
    print("\n1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        tarefa = input("Digite a nova tarefa: ")
        
        with open(ARQUIVO_TAREFAS, "a", encoding="utf-8") as arquivo:
            arquivo.write(tarefa + "\n")
        print("Tarefa salva com sucesso!")

    elif opcao == '2':
        print("\n--- SUAS TAREFAS ---")
        try:
            
            with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                
                if not linhas:
                    print("A lista está vazia.")
                else:
                    
                    for i, linha in enumerate(linhas, start=1):
                        print(f"{i}. {linha.strip()}")
        except FileNotFoundError:
            print("Nenhuma tarefa encontrada (o arquivo ainda não existe).")

    elif opcao == '3':
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida!")