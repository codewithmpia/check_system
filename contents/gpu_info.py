import subprocess
from .colors import BColors as bcolors


def get_gpu_info():
    gpu_info = []
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,utilization.gpu,memory.total,memory.used,memory.free,temperature.gpu', '--format=csv,noheader,nounits'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            gpus_info = result.stdout.strip().split('\n')
            for gpu in gpus_info:
                name, utilization, memory_total, memory_used, memory_free, temperature = gpu.split(', ')
                gpu_info.append(
                    f"{bcolors.WHITE}Nom du GPU: {bcolors.CYAN}{name}\n"
                    f"{bcolors.WHITE}Utilisation du GPU: {bcolors.CYAN}{utilization}%\n"
                    f"{bcolors.WHITE}Mémoire Totale du GPU: {bcolors.CYAN}{memory_total} MB\n"
                    f"{bcolors.WHITE}Mémoire Utilisée du GPU: {bcolors.CYAN}{memory_used} MB\n"
                    f"{bcolors.WHITE}Mémoire Libre du GPU: {bcolors.CYAN}{memory_free} MB\n"
                    f"{bcolors.WHITE}Température du GPU: {bcolors.CYAN}{temperature} °C{bcolors.ENDC}"
                )
        else:
            gpu_info.append(f"{bcolors.WHITE}Aucun GPU NVIDIA détecté ou erreur lors de l'exécution de nvidia-smi.{bcolors.ENDC}")
    except FileNotFoundError:
        gpu_info.append(f"{bcolors.WHITE}L'outil nvidia-smi n'est pas installé. Veuillez l'installer pour obtenir des informations sur le GPU NVIDIA.{bcolors.ENDC}")

    try:
        result = subprocess.run(['lspci', '-nnk'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            gpus_info = [line for line in result.stdout.strip().split('\n') if 'VGA compatible controller' in line or '3D controller' in line]
            for gpu in gpus_info:
                gpu_info.append(f"{bcolors.WHITE}Nom du GPU: {bcolors.CYAN}{gpu}\n{bcolors.WHITE}Informations détaillées sur le GPU non-NVIDIA non disponibles dans cette version.{bcolors.ENDC}")
        else:
            gpu_info.append(f"{bcolors.WHITE}Aucun autre GPU détecté ou erreur lors de l'exécution de lspci.{bcolors.ENDC}")
    except FileNotFoundError:
        gpu_info.append(f"{bcolors.WHITE}L'outil lspci n'est pas installé. Veuillez l'installer pour obtenir des informations sur les autres GPU.{bcolors.ENDC}")

    return '\n'.join(gpu_info)
