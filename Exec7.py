while True:
    try:
        n = int(input("Quantos números você deseja digitar? "))
        if n > 0:
            break
        else:
            print("Por favor, digite um número maior que zero.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

numeros = []

for i in range(n):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print("-" * 30)
print(f"Lista completa: {numeros}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média dos valores: {media:.2f}")