def calcular_media_idades():
    print("Cálculo da média das idades de 50 alunos\n")
    
    # Lista para armazenar as idades
    idades = []
    
    # Leitura das idades com validação
    print("Digite a idade de cada aluno:")
    for i in range(1, 51):
        while True:
            try:
                idade = int(input(f"Aluno {i:2d}: "))
                if idade > 0:
                    idades.append(idade)
                    break
                else:
                    print("A idade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    # Cálculo da média
    soma_idades = sum(idades)
    media_idades = soma_idades / len(idades)
    
    # Exibição dos resultados
    print("\n" + "=" * 50)
    print(f"Soma das idades:          {soma_idades:6d} anos")
    print(f"Média das idades:         {media_idades:6.2f} anos")
    print("=" * 50)

# Execução do programa
if __name__ == "__main__":
    calcular_media_idades()