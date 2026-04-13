def eh_primo(numero):
    """Retorna True se o número for primo, False caso contrário."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    
    # Verifica divisores de 5 até a raiz quadrada do número
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    
    return True

def verificar_numero_primo():
    print("Verificação se um número é primo\n")
    
    # Solicita o número com validação
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))
            if num > 0:
                break
            else:
                print("O número deve ser maior que zero. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro positivo.")
    
    # Verificação e exibição do resultado
    print("\n" + "=" * 60)
    if eh_primo(num):
        print(f"O número {num} É primo.")
    else:
        print(f"O número {num} NÃO é primo.")
    print("=" * 60)

# Execução do programa
if __name__ == "__main__":
    verificar_numero_primo()