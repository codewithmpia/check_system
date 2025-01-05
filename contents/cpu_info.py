import platform
import psutil
from .colors import BColors as bcolors


def get_cpu_info():
    return (
        f"{bcolors.WHITE}Processeur: {bcolors.CYAN}{platform.processor()}\n"
        f"{bcolors.WHITE}Nombre de Cœurs CPU: {bcolors.CYAN}{psutil.cpu_count(logical=False)}\n"
        f"{bcolors.WHITE}Nombre de Coeurs Logiques CPU: {bcolors.CYAN}{psutil.cpu_count(logical=True)}{bcolors.ENDC}"
    )
