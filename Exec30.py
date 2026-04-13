def calcular_media_idades_25_a_39():
    print("Cálculo da média das idades dos alunos entre 26 e 39 anos\n")
    
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
    contador = 0
    
    # Leitura das idades com validação
    print(f"\nDigite a idade de cada um dos {n} alunos:")
    for i in range(1, n + 1):
        while True:
            try:
                idade = int(input(f"Aluno {i:3d}: "))
                if idade > 0:
                    if 25 < idade < 40:   # mais de 25 e menos de 40
                        soma_idades += idade
                        contador += 1
                    break
                else:
                    print("A idade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    # Exibição dos resultados
    print("\n" + "=" * 70)
    print(f"Total de alunos na turma:                          {n:4d}")
    print(f"Alunos com idade > 25 e < 40 anos:                 {contador:4d}")
    
    if contador > 0:
        media = soma_idades / contador
        print(f"Soma das idades desse grupo:                      {soma_idades:6d} anos")
        print(f"Média das idades (26 a 39 anos):                  {media:8.2f} anos")
    else:
        print("Nenhum aluno possui idade entre 26 e 39 anos.")
    
    print("=" * 70)

# Execução do programa
if __name__ == "__main__":
    calcular_media_idades_25_a_39()