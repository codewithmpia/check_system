import psutil
from .colors import BColors as bcolors


def get_memory_info():
    memory = psutil.virtual_memory()
    return (
        f"{bcolors.WHITE}Mémoire Totale: {bcolors.CYAN}{memory.total / (1024 ** 3):.2f} GB\n"
        f"{bcolors.WHITE}Mémoire Disponible: {bcolors.CYAN}{memory.available / (1024 ** 3):.2f} GB\n"
        f"{bcolors.WHITE}Mémoire Utilisée: {bcolors.CYAN}{memory.used / (1024 ** 3):.2f} GB\n"
        f"{bcolors.WHITE}Utilisation de la Mémoire: {bcolors.CYAN}{memory.percent}%{bcolors.ENDC}"
    )
