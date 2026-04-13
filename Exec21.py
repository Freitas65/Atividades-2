def calcular_soma_idades():
    print("Cálculo da soma das idades de 30 alunos\n")
    
    # Lista para armazenar as idades
    idades = []
    
    # Leitura das idades
    print("Digite a idade de cada aluno:")
    for i in range(1, 31):
        while True:
            try:
                idade = int(input(f"Aluno {i:2d}: "))
                if idade > 0:
                    idades.append(idade)
                    break
                else:
                    print("A idade deve ser um número positivo. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Cálculo da soma
    soma_idades = sum(idades)
    
    # Exibição do resultado
    print("\n" + "="*40)
    print(f"Soma das idades dos 30 alunos: {soma_idades} anos")
    print("="*40)

# Execução do programa
if __name__ == "__main__":
    calcular_soma_idades()