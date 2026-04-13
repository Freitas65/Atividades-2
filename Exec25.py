def calcular_soma_notas_turma():
    print("Cálculo da soma das notas de uma turma qualquer\n")
    
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
    
    # Variáveis para processamento
    soma_notas = 0.0
    
    # Leitura das notas com validação
    print(f"\nDigite a nota de cada um dos {n} alunos (use ponto para decimais):")
    for i in range(1, n + 1):
        while True:
            try:
                nota = float(input(f"Aluno {i:3d}: "))
                if 0.0 <= nota <= 10.0:
                    soma_notas += nota
                    break
                else:
                    print("A nota deve estar entre 0.0 e 10.0. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número decimal válido.")
    
    # Exibição dos resultados
    print("\n" + "=" * 60)
    print(f"Total de alunos na turma:           {n:4d}")
    print(f"Soma total das notas da turma:     {soma_notas:8.2f}")
    
    # Cálculo e exibição da média
    if n > 0:
        media = soma_notas / n
        print(f"Média geral da turma:              {media:8.2f}")
    
    print("=" * 60)

# Execução do programa
if __name__ == "__main__":
    calcular_soma_notas_turma()