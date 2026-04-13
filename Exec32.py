def calcular_fatorial():
    print("Cálculo do Fatorial de um Número\n")
    
    # Solicita o número com validação
    while True:
        try:
            num = int(input("Digite um número inteiro não negativo: "))
            if num >= 0:
                break
            else:
                print("O número deve ser maior ou igual a zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    # Cálculo do fatorial
    if num == 0 or num == 1:
        fatorial = 1
    else:
        fatorial = 1
        for i in range(2, num + 1):
            fatorial *= i
    
    # Exibição do resultado
    print("\n" + "=" * 50)
    print(f"O fatorial de {num} é: {fatorial}")
    print("=" * 50)

# Execução do programa
if __name__ == "__main__":
    calcular_fatorial()