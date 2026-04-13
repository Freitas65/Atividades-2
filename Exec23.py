def contar_alunos_30_anos():
    print("Contagem de alunos com 30 anos em uma turma de 100 alunos\n")
    
    # Contador para alunos com 30 anos
    contador_30 = 0
    
    # Leitura das idades com validação
    print("Digite a idade de cada aluno:")
    for i in range(1, 101):
        while True:
            try:
                idade = int(input(f"Aluno {i:3d}: "))
                if idade > 0:
                    if idade == 30:
                        contador_30 += 1
                    break
                else:
                    print("A idade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    # Exibição do resultado
    print("\n" + "=" * 60)
    print(f"Total de alunos na turma:          100")
    print(f"Quantidade de alunos com 30 anos:   {contador_30}")
    
    if contador_30 == 0:
        print("Nenhum aluno possui 30 anos.")
    elif contador_30 == 1:
        print("Apenas um aluno possui 30 anos.")
    else:
        print(f"{contador_30} alunos possuem 30 anos.")
    
    print("=" * 60)

# Execução do programa
if __name__ == "__main__":
    contar_alunos_30_anos()