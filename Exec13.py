import psutil

def converter_para_gb(bytes_valor):
    return bytes_valor / (1024 ** 3)

print(f"{'PARTIÇÃO':<15} | {'TOTAL':>10} | {'USADO':>10} | {'LIVRE':>10} | {'USO %'}")
print("-" * 65)

# 1. Requisito: usar psutil.disk_partitions() para listar as partições
particoes = psutil.disk_partitions()

for particao in particoes:
    try:
        # 2. Requisito: usar psutil.disk_usage() para cada ponto de montagem
        uso = psutil.disk_usage(particao.mountpoint)
        
        # Extração dos dados
        ponto_montagem = particao.mountpoint
        total = converter_para_gb(uso.total)
        usado = converter_para_gb(uso.used)
        livre = converter_para_gb(uso.free)
        percentual = uso.percent

        # 3. Requisito: Exibir em forma de tabela organizada
        print(f"{ponto_montagem:<15} | {total:>7.1f} GB | {usado:>7.1f} GB | {livre:>7.1f} GB | {percentual:>5}%")
    
    except PermissionError:
        # Alguns drivers (como o de CD-ROM ou partições de sistema) podem negar acesso
        continue
    except OSError:
        # Ignora partições que não estão prontas (ex: leitor de cartão vazio)
        continue

print("-" * 65)