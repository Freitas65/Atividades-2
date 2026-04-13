
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    
    if b == 0:
        return "Erro! Não é possível dividir por zero."
    return a / b

# --- Menu Principal ---

print("=== CALCULADORA SIMPLES ===")
print("1. Somar")
print("2. Subtrair")
print("3. Multiplicar")
print("4. Dividir")

opcao = input("\nEscolha a operação (1-4): ")

if opcao in ['1', '2', '3', '4']:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))

    if opcao == '1':
        resultado = somar(n1, n2)
        print(f"Resultado: {n1} + {n2} = {resultado}")
    elif opcao == '2':
        resultado = subtrair(n1, n2)
        print(f"Resultado: {n1} - {n2} = {resultado}")
    elif opcao == '3':
        resultado = multiplicar(n1, n2)
        print(f"Resultado: {n1} * {n2} = {resultado}")
    elif opcao == '4':
        resultado = dividir(n1, n2)
        print(f"Resultado: {resultado}")
else:
    print("Opção inválida!")