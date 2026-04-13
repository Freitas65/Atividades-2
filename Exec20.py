import psutil
import os
import time

def monitorar_processos():
    try:
        while True:
            # Lista para armazenar os dados dos processos
            processos = []

            # Itera sobre todos os processos rodando no sistema
            for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
                try:
                    # Obtemos os dados como um dicionário
                    info = proc.info
                    # Se o uso for None (comum na primeira leitura), tratamos como 0.0
                    if info['cpu_percent'] is None:
                        info['cpu_percent'] = 0.0
                    processos.append(info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            # Ordena a lista pelo consumo de CPU (do maior para o menor)
            # Requisito: Pegar os 5 primeiros
            top_5 = sorted(processos, key=lambda p: p['cpu_percent'], reverse=True)[:5]

            # Limpeza e exibição
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 45)
            print(f"{'PID':<8} | {'NOME DO PROCESSO':<25} | {'CPU %':>6}")
            print("-" * 45)

            for p in top_5:
                print(f"{p['pid']:<8} | {p['name'][:25]:<25} | {p['cpu_percent']:>6.1f}%")
            
            print("-" * 45)
            print("Atualizando a cada 2 segundos... (Ctrl+C para sair)")
            
            # Precisamos de um intervalo para o psutil calcular o uso de CPU entre ciclos
            time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitor de processos encerrado.")

if __name__ == "__main__":
    monitorar_processos()