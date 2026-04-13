import psutil
import os
import time

try:
    while True:
        # Chamamos a função apenas UMA VEZ por ciclo
        # Usamos interval=1 para ter uma leitura precisa de 1 segundo
        cores = psutil.cpu_percent(interval=1, percpu=True)
        
        # Em vez de chamar a função de novo, calculamos a média da lista
        # Isso garante que o Total seja fiel à soma dos núcleos exibidos
        cpu_total = sum(cores) / len(cores)

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"CPU Total: {cpu_total:.1f}%")
        print("-" * 30)
        
        # Exibição elegante em pares
        for i in range(0, len(cores), 2):
            c1 = f"Núcleo {i}: {cores[i]:>5}%"
            # Verifica se existe o próximo núcleo (para CPUs com número ímpar, embora raro)
            c2 = f" | Núcleo {i+1}: {cores[i+1]:>5}%" if (i+1) < len(cores) else ""
            print(c1 + c2)
            
except KeyboardInterrupt:
    print("\nMonitor encerrado.")