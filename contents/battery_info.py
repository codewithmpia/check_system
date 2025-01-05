import psutil
from .colors import BColors as bcolors


def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        return (
            f"{bcolors.WHITE}Niveau de Batterie: {bcolors.CYAN}{battery.percent:.2f}%\n"
            f"{bcolors.WHITE}Branché sur Secteur: {bcolors.CYAN}{battery.power_plugged}\n"
            f"{bcolors.WHITE}Temps d'Utilisation Restant: {bcolors.CYAN}{battery.secsleft / 3600:.2f} heures{bcolors.ENDC}"
        )
    else:
        return f"{bcolors.WHITE}Aucune batterie détectée.{bcolors.ENDC}"
