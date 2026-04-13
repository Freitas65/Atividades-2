def contar_alunos_com_30_anos():
    print("Contagem de alunos com exatamente 30 anos em uma turma qualquer\n")
    
    # Solicita a quantidade de alunos
    while True:
        try:
            n = int(input("Digite o número de alunos na turma: "))
            if n > 0:
                break
            else:
                print("O número de alunos deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    # Variável para contagem
    contador_30 = 0
    
    # Leitura das idades com validação
    print(f"\nDigite a idade de cada um dos {n} alunos:")
    for i in range(1, n + 1):
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
    
    # Exibição dos resultados
    print("\n" + "=" * 60)
    print(f"Total de alunos na turma:               {n:4d}")
    print(f"Quantidade de alunos com 30 anos:       {contador_30:4d}")
    
    if contador_30 == 0:
        print("Nenhum aluno possui exatamente 30 anos.")
    elif contador_30 == 1:
        print("Apenas 1 aluno possui exatamente 30 anos.")
    else:
        print(f"{contador_30} alunos possuem exatamente 30 anos.")
    
    print("=" * 60)

# Execução do programa
if __name__ == "__main__":
    contar_alunos_com_30_anos()