import psutil
import time
import os

# 1. Configuração inicial e leitura do limite
print("=== CONFIGURAÇÃO DO MONITOR COM ALERTA ===")
try:
    limite_usuario = float(input("Defina o limite de uso de RAM para alerta (ex: 80): "))
except ValueError:
    print("Entrada inválida. Usando 80% como padrão.")
    limite_usuario = 80.0

print(f"\nMonitorando... Alerta configurado para {limite_usuario}%")
print("Pressione Ctrl+C para encerrar.")
time.sleep(2)

try:
    while True:
        # Coleta dos dados de memória
        memoria = psutil.virtual_memory()
        percentual_uso = memoria.percent
        
        # Limpeza de tela (ajustado para Windows/Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Exibição dos dados
        print("-" * 40)
        print(f"STATUS DA MEMÓRIA RAM")
        print(f"Uso Atual: {percentual_uso}%")
        print(f"Limite Definido: {limite_usuario}%")
        print("-" * 40)

        # 2. Lógica de Alerta (Requisito)
        if percentual_uso > limite_usuario:
            print("\n[!!!] ALERTA: O USO DE MEMÓRIA ULTRAPASSOU O LIMITE! [!!!]")
            # No Windows, você pode adicionar um 'beep' sonoro com:
            # import winsound; winsound.Beep(1000, 500)
        else:
            print("\nUso dentro dos parâmetros normais.")

        # Requisito: Loop contínuo a cada 2 segundos
        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoramento encerrado pelo usuário.")