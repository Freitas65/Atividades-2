import psutil

# Configuração do limite (Requisito: Limite em % como constante ou entrada)
LIMITE_CRITICO_PORCENTAGEM = 10.0

def converter_para_gb(bytes_valor):
    return bytes_valor / (1024 ** 3)

print(f"--- VERIFICANDO PARTIÇÕES COM MENOS DE {LIMITE_CRITICO_PORCENTAGEM}% LIVRE ---")
print("-" * 60)

particoes = psutil.disk_partitions()
encontrou_critica = False

for particao in particoes:
    try:
        uso = psutil.disk_usage(particao.mountpoint)
        
        # Cálculo do espaço livre em porcentagem
        # O psutil dá a porcentagem USADA, então calculamos a LIVRE
        porcentagem_livre = 100 - uso.percent
        
        # Requisito: Mostrar apenas as partições "críticas"
        if porcentagem_livre < LIMITE_CRITICO_PORCENTAGEM:
            encontrou_critica = True
            total_gb = converter_para_gb(uso.total)
            livre_gb = converter_para_gb(uso.free)
            
            print(f"ALERTA: Partição [{particao.mountpoint}] está ficando cheia!")
            print(f" -> Espaço Total: {total_gb:.2f} GB")
            print(f" -> Espaço Livre: {livre_gb:.2f} GB ({porcentagem_livre:.1f}%)")
            print("-" * 30)
            
    except (PermissionError, OSError):
        # Ignora unidades de CD vazias ou partições de sistema protegidas
        continue

if not encontrou_critica:
    print("Tudo certo! Todas as partições possuem espaço suficiente.")

print("\nVerificação concluída.")