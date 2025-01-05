import psutil
from .colors import BColors as bcolors


def get_temperature_info():
    temp = psutil.sensors_temperatures()
    if temp:
        temps = []
        for name, entries in temp.items():
            for entry in entries:
                temps.append(f"{name}: {entry.current:.1f}°C")
        return f"{bcolors.WHITE}" + '\n'.join([f"{bcolors.CYAN}{temp}{bcolors.WHITE}" for temp in temps]) + f"{bcolors.ENDC}"
    else:
        return f"{bcolors.WHITE}Aucune température détectée.{bcolors.ENDC}"
