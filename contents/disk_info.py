import psutil
from .colors import BColors as bcolors

def get_disk_info():
    disk = psutil.disk_usage('/')
    return (
        f"{bcolors.WHITE}Espace Disque Total: {bcolors.CYAN}{disk.total / (1024 ** 3):.2f} GB\n"
        f"{bcolors.WHITE}Espace Disque Utilisé: {bcolors.CYAN}{disk.used / (1024 ** 3):.2f} GB\n"
        f"{bcolors.WHITE}Espace Disque Libre: {bcolors.CYAN}{disk.free / (1024 ** 3):.2f} GB\n"
        f"{bcolors.WHITE}Utilisation du Disque: {bcolors.CYAN}{disk.percent}%{bcolors.ENDC}"
    )
