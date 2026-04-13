def calcular_media_notas_entre_5_e_7():
    print("Cálculo da média das notas dos alunos com nota > 5,0 e < 7,0\n")
    
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
    contador = 0
    
    # Leitura das notas com validação
    print(f"\nDigite a nota de cada um dos {n} alunos (use ponto para decimais):")
    for i in range(1, n + 1):
        while True:
            try:
                nota = float(input(f"Aluno {i:3d}: "))
                if 0.0 <= nota <= 10.0:
                    if 5.0 < nota < 7.0:   # maior que 5,0 e menor que 7,0
                        soma_notas += nota
                        contador += 1
                    break
                else:
                    print("A nota deve estar entre 0.0 e 10.0. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número decimal válido.")
    
    # Exibição dos resultados
    print("\n" + "=" * 70)
    print(f"Total de alunos na turma:                          {n:4d}")
    print(f"Alunos com nota > 5,0 e < 7,0:                    {contador:4d}")
    
    if contador > 0:
        media = soma_notas / contador
        print(f"Soma das notas desse grupo:                       {soma_notas:8.2f}")
        print(f"Média das notas (maior que 5,0 e menor que 7,0):  {media:8.2f}")
    else:
        print("Nenhum aluno possui nota entre 5,0 e 7,0 (exclusivo).")
    
    print("=" * 70)

# Execução do programa
if __name__ == "__main__":
    calcular_media_notas_entre_5_e_7()