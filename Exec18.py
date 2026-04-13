import psutil
import platform
import subprocess
import os

def obter_numero_serie_cpu():
    """
    Tenta obter o número de série da CPU de forma específica por SO.
    Em muitos sistemas modernos, isso é bloqueado por questões de privacidade.
    """
    try:
        if platform.system() == "Windows":
            # Comando via WMI para Windows
            cmd = "wmic cpu get processorid"
            resultado = subprocess.check_output(cmd, shell=True).decode().split()
            return resultado[1] if len(resultado) > 1 else "Não encontrado"
        
        elif platform.system() == "Linux":
            # Comando via dmidecode (requer privilégios de root)
            cmd = "cat /proc/cpuinfo | grep 'Serial' | cut -d ':' -f 2"
            resultado = os.popen(cmd).read().strip()
            return resultado if resultado else "Não disponível (requer permissão root)"
        
        return "Método não suportado para este SO"
    except Exception:
        return "Acesso negado ou ID não disponível"

# 1. Coleta de informações básicas (Requisitos)
nome_cpu = platform.processor()
arquitetura = platform.machine()
nucleos_fisicos = psutil.cpu_count(logical=False)
nucleos_logicos = psutil.cpu_count(logical=True)
frequencia = psutil.cpu_freq()
id_cpu = obter_numero_serie_cpu()

# 2. Exibição organizada
print("="*50)
print(f"{'INFORMAÇÕES DO PROCESSADOR':^50}")
print("="*50)

print(f"Modelo/ID:       {nome_cpu}")
print(f"Arquitetura:     {arquitetura}")
print(f"Núcleos Físicos: {nucleos_fisicos}")
print(f"Núcleos Lógicos: {nucleos_logicos}")

if frequencia:
    print(f"Frequência Máx:  {frequencia.max:.2f} MHz")
    print(f"Frequência Atual: {frequencia.current:.2f} MHz")

print("-" * 50)
# Requisito: Exibir número de série ou mensagem explicativa
print(f"Número de Série: {id_cpu}")

if "Não" in id_cpu or "Acesso" in id_cpu:
    print("\n[Nota Didática]: O número de série da CPU (Processor ID) é uma ")
    print("informação sensível. Muitos sistemas operacionais e BIOS bloqueiam ")
    print("o acesso a este dado por questões de privacidade e segurança.")
print("="*50)