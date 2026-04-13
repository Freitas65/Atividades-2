import psutil
import time
import os

def converter_para_mb(bytes_valor):
    # Converte bytes para MegaBytes (MB)
    return bytes_valor / (1024 * 1024)

print("--- Monitor de Memória RAM (Pressione Ctrl+C para parar) ---")

try:
    while True:
        # Requisito: usar psutil.virtual_memory()
        memoria = psutil.virtual_memory()
        
        total = converter_para_mb(memoria.total)
        usada = converter_para_mb(memoria.used)
        livre = converter_para_mb(memoria.available)
        porcentagem_livre = 100 - memoria.percent

        # Limpa a tela para parecer um monitor em tempo real
        # 'cls' para Windows, 'clear' para Linux/Mac
        os.system('cls' if os.name == 'nt' else 'clear')

        # Requisito: Exibir de forma organizada
        print(f"{' COMPONENTE ': ^30}")
        print("-" * 30)
        print(f"Total:         {total:>10.2f} MB")
        print(f"Em uso:        {usada:>10.2f} MB ({memoria.percent}%)")
        print(f"Livre:         {livre:>10.2f} MB ({porcentagem_livre:.1f}%)")
        print("-" * 30)
        print("Atualizando a cada 2 segundos...")

        # Requisito: Atualizar a cada 2 segundos
        time.sleep(2)

except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")