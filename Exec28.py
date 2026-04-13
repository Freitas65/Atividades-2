def calcular_soma_idades_acima_25():
    print("Cálculo da soma das idades dos alunos com mais de 25 anos\n")
    
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
    soma_idades = 0
    contador_acima_25 = 0
    
    # Leitura das idades com validação
    print(f"\nDigite a idade de cada um dos {n} alunos:")
    for i in range(1, n + 1):
        while True:
            try:
                idade = int(input(f"Aluno {i:3d}: "))
                if idade > 0:
                    if idade > 25:
                        soma_idades += idade
                        contador_acima_25 += 1
                    break
                else:
                    print("A idade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    # Exibição dos resultados
    print("\n" + "=" * 65)
    print(f"Total de alunos na turma:                    {n:4d}")
    print(f"Alunos com mais de 25 anos:                  {contador_acima_25:4d}")
    print(f"Soma das idades dos alunos > 25 anos:       {soma_idades:6d} anos")
    
    if contador_acima_25 > 0:
        media_idades = soma_idades / contador_acima_25
        print(f"Média das idades dos alunos > 25 anos:      {media_idades:6.2f} anos")
    else:
        print("Nenhum aluno possui mais de 25 anos.")
    
    print("=" * 65)

# Execução do programa
if __name__ == "__main__":
    calcular_soma_idades_acima_25()