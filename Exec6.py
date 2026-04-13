frase = input("Digite uma palavra ou frase: ").lower()
contador = 0
vogais = "aeiou"
for letra in frase:
    if letra in vogais:
        contador = contador + 1

print (f"A Frase/Palavra tem {contador} vogais.")