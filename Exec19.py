import psutil

# ==============================================================================
# CONCEITOS DE DISPOSITIVOS DE E/S (I/O)
#
# Em computação, dispositivos de E/S são a ponte entre o usuário e o processador.
# 
# 1. Dispositivos de ENTRADA: Levam dados para dentro do computador.
#    Exemplos: Teclado, Mouse, Scanner, Microfone, Sensores.
#
# 2. Dispositivos de SAÍDA: Traduzem os dados do computador para o usuário.
#    Exemplos: Monitor, Impressora, Caixas de Som.
#
# 3. Dispositivos HÍBRIDOS (Entrada e Saída): Permitem ler e gravar dados.
#    Exemplos: HDs, SSDs, Pendrives, Telas Touchscreen, Placas de Rede.
# ==============================================================================

def listar_dispositivos():
    # Requisito: Listar as partições/dispositivos de armazenamento
    particoes = psutil.disk_partitions()
    
    print("--- DISPOSITIVOS DE ARMAZENAMENTO DETECTADOS ---")
    for i, p in enumerate(particoes):
        # fstype nos diz o sistema de arquivos (NTFS, FAT32, ext4)
        print(f"[{i}] Dispositivo: {p.device} | Ponto de Montagem: {p.mountpoint}")
    return particoes

def mostrar_detalhes(particao):
    try:
        uso = psutil.disk_usage(particao.mountpoint)
        print(f"\n--- DETALHES DE: {particao.mountpoint} ---")
        print(f"Tipo de Arquivo: {particao.fstype}")
        print(f"Espaço Total:   {uso.total / (1024**3):.2f} GB")
        print(f"Espaço Usado:   {uso.used / (1024**3):.2f} GB")
        print(f"Espaço Livre:   {uso.free / (1024**3):.2f} GB")
        print(f"Status:         {'Pronto' if uso.total > 0 else 'Indisponível'}")
    except PermissionError:
        print("\nErro: Permissão negada para acessar este dispositivo.")
    except Exception as e:
        print(f"\nErro ao ler dispositivo: {e}")

# --- Execução Principal ---
lista = listar_dispositivos()

if lista:
    try:
        escolha = int(input("\nEscolha o número do dispositivo para ver detalhes: "))
        if 0 <= escolha < len(lista):
            mostrar_detalhes(lista[escolha])
        else:
            print("Opção inválida.")
    except ValueError:
        print("Por favor, digite um número inteiro.")
else:
    print("Nenhum dispositivo de armazenamento encontrado.")