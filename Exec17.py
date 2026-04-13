import psutil
import time
from datetime import datetime

# Nome do arquivo de log
NOME_ARQUIVO = "cpu_log.txt"

print(f"--- Iniciando Logger de CPU ---")
print(f"Salvando dados em {NOME_ARQUIVO} a cada 5 segundos...")
print("Pressione Ctrl+C para interromper.")

try:
    while True:
        # 1. Captura o uso da CPU (interval=1 para uma medição precisa)
        uso_cpu = psutil.cpu_percent(interval=1)
        
        # 2. Captura a data e hora atual formatada
        # Requisito: Ex.: 2026-02-19 19:30:12
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 3. Formata a linha que será salva
        linha_log = f"{agora} - CPU: {uso_cpu}%\n"
        
        # 4. Salva no arquivo (Requisito: usar modo "a" para anexar)
        with open(NOME_ARQUIVO, "a", encoding="utf-8") as arquivo:
            arquivo.write(linha_log)
        
        # Exibe no terminal apenas para acompanhamento
        print(f"Registro salvo: {linha_log.strip()}")
        
        # 5. Aguarda o intervalo de 5 segundos (Requisito)
        # Como o cpu_percent já usou 1 segundo de intervalo, aguardamos mais 4
        time.sleep(4)

except KeyboardInterrupt:
    print("\nLogger encerrado pelo usuário.")