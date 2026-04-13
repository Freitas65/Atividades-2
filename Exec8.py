import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("--- Jogo de Adivinhação ---")
print("Tente adivinhar o número que estou pensando entre 1 e 100.")

while not acertou:
    try:
        palpite = int(input("Qual o seu palpite? "))
        tentativas += 1  

        if palpite == numero_secreto:
            print(f" Parabéns! Você acertou em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("Dica: O número é MAIOR.") 
        else:
            print("Dica: O número é MENOR.") 
            
    except ValueError:
        print("Por favor, digite apenas números inteiros.")

print("Fim de jogo!")