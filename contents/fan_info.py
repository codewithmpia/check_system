import psutil
from .colors import BColors as bcolors


def get_fan_info():
    fans = psutil.sensors_fans()
    if fans:
        fan_info = []
        for name, entries in fans.items():
            for entry in entries:
                fan_info.append(f"{name}: {entry.current} RPM")
        return f"{bcolors.WHITE}" + '\n'.join([f"{bcolors.CYAN}{fan}{bcolors.WHITE}" for fan in fan_info]) + f"{bcolors.ENDC}"
    else:
        return f"{bcolors.WHITE}Aucun ventilateur détecté.{bcolors.ENDC}"
