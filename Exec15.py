import psutil
import time
import os

def formatar_velocidade(bytes_segundo):
    """Converte bytes para uma unidade legível (kB ou MB)."""
    kb = bytes_segundo / 1024
    if kb > 1024:
        return f"{kb / 1024:.2f} MB/s"
    return f"{kb:.2f} kB/s"

print("--- Monitor de Rede em Tempo Real ---")
print("Pressione Ctrl+C para parar.")

try:
    # Primeira leitura antes do loop
    io_antigo = psutil.net_io_counters()

    while True:
        # Requisito: Esperar um intervalo (1 segundo)
        time.sleep(1)
        
        # Segunda leitura para comparar
        io_novo = psutil.net_io_counters()

        # Requisito: Calcular a diferença entre as duas leituras
        download_velocidade = io_novo.bytes_recv - io_antigo.bytes_recv
        upload_velocidade = io_novo.bytes_sent - io_antigo.bytes_sent

        # Limpeza de tela
        os.system('cls' if os.name == 'nt' else 'clear')

        # Requisito: Exibir no terminal formatado
        print("-" * 40)
        print(f"TRÁFEGO DE REDE (Estimado)")
        print("-" * 40)
        print(f"Download: {formatar_velocidade(download_velocidade)}")
        print(f"Upload:   {formatar_velocidade(upload_velocidade)}")
        print("-" * 40)
        print("Atualizando a cada 1s...")

        # Atualiza a variável antiga para a próxima comparação
        io_antigo = io_novo

except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")