import re
from .colors import BColors as bcolors
from .os_info import get_os_info
from .cpu_info import get_cpu_info
from .memory_info import get_memory_info
from .disk_info import get_disk_info
from .network_info import get_network_info
from .battery_info import get_battery_info
from .temperature_info import get_temperature_info
from .fan_info import get_fan_info
from .gpu_info import get_gpu_info
from .devices_info import get_connected_devices

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)


def system_checkup():
    print(f"{bcolors.BOLD}RAPPORT DE VERIFICATION DU SYSTEME{bcolors.ENDC}")
    print(f"{bcolors.BOLD}=================================={bcolors.ENDC}")
    print(get_os_info())
    print()
    print(f"{bcolors.BOLD}I. Informations du processeur (CPU):{bcolors.ENDC}")
    print(f"{bcolors.BOLD}-------------------------------------{bcolors.ENDC}")
    print(get_cpu_info())
    print()
    print(f"{bcolors.BOLD}II. Informations de la mémoire:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}-------------------------------{bcolors.ENDC}")
    print(get_memory_info())
    print()
    print(f"{bcolors.BOLD}III. Informations du Disque de stockage:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}---------------------------------------{bcolors.ENDC}")
    print(get_disk_info())
    print()
    print(f"{bcolors.BOLD}IV. Informations du Réseau:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}---------------------------{bcolors.ENDC}")
    print(get_network_info())
    print()
    print(f"{bcolors.BOLD}V. Informations de la Batterie:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}------------------------------{bcolors.ENDC}")
    print(get_battery_info())
    print()
    print(f"{bcolors.BOLD}VI. Informations de la Température:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}----------------------------------{bcolors.ENDC}")
    print(get_temperature_info())
    print()
    print(f"{bcolors.BOLD}VII. Informations des Ventilateurs:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}----------------------------------{bcolors.ENDC}")
    print(get_fan_info())
    print()
    print(f"{bcolors.BOLD}VIII. Informations du GPU:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}--------------------------{bcolors.ENDC}")
    print(get_gpu_info())
    print()
    print(f"{bcolors.BOLD}IX. Liste de périphériques connectés:{bcolors.ENDC}")
    print(f"{bcolors.BOLD}------------------------------------{bcolors.ENDC}")
    print(get_connected_devices())
    print()

    # Write the report to a file
    with open("system_checkup_report.txt", "w") as file:
        file.write(strip_ansi_codes(f"{bcolors.BOLD}RAPPORT DE VERIFICATION DU SYSTEME{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}=================================={bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_os_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}I. Informations du processeur (CPU):{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}-------------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_cpu_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}II. Informations de la mémoire:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}-------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_memory_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}III. Informations du Disque de stockage:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}---------------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_disk_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}IV. Informations du Réseau:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}---------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_network_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}V. Informations de la Batterie:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_battery_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}VI. Informations de la Température:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}----------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_temperature_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}VII. Informations des Ventilateurs:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}----------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_fan_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}VIII. Informations du GPU:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}--------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_gpu_info() + "\n\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}IX. Liste de périphériques connectés:{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(f"{bcolors.BOLD}------------------------------------{bcolors.ENDC}\n"))
        file.write(strip_ansi_codes(get_connected_devices() + "\n\n"))