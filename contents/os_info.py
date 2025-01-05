import platform
import subprocess
import os
from datetime import datetime, timedelta
from .colors import BColors as bcolors

def get_os_info():
    os_name = platform.system()
    os_version = platform.release()
    try:
        if os_name == "Linux":
            distro = subprocess.run(['lsb_release', '-d'], stdout=subprocess.PIPE, text=True).stdout.split(":")[1].strip()
            package_manager = "apt" if os.path.exists("/usr/bin/apt") else "yum" if os.path.exists("/usr/bin/yum") else "unknown"
            if package_manager == "apt":
                num_packages = subprocess.run(['dpkg-query', '-f', '${binary:Package}\n', '-W'], stdout=subprocess.PIPE, text=True).stdout.count('\n')
            elif package_manager == "yum":
                num_packages = subprocess.run(['yum', 'list', 'installed'], stdout=subprocess.PIPE, text=True).stdout.count('\n') - 1
            elif package_manager == "pacman":
                num_packages = subprocess.run(['pacman', '-Q'], stdout=subprocess.PIPE, text=True).stdout.count('\n')
            elif package_manager == "zypper":
                num_packages = subprocess.run(['zypper', 'se', '-si'], stdout=subprocess.PIPE, text=True).stdout.count('\n')
            elif package_manager == "dnf":
                num_packages = subprocess.run(['dnf', 'list', 'installed'], stdout=subprocess.PIPE, text=True).stdout.count('\n') - 1
            elif package_manager == "apk":
                num_packages = subprocess.run(['apk', 'info'], stdout=subprocess.PIPE, text=True).stdout.count('\n')
            else:
                num_packages = "inconnu"
            
            # Get installation date
            install_date = subprocess.run(['stat', '-c', '%W', '/'], stdout=subprocess.PIPE, text=True).stdout.strip()
            if install_date == '-':
                install_date = "inconnu"
            else:
                install_date = datetime.fromtimestamp(int(install_date)).strftime('%d/%m/%Y à %H:%M:%S')
            
            # Get uptime
            uptime_seconds = float(subprocess.run(['cat', '/proc/uptime'], stdout=subprocess.PIPE, text=True).stdout.split()[0])
            uptime_duration = str(timedelta(seconds=uptime_seconds)).split('.')[0]  # Remove microseconds
            
            return (f"{bcolors.WHITE}Rapport du: {bcolors.CYAN}{datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}{bcolors.ENDC}\n"
                    f"{bcolors.WHITE}Système d'exploitation: {bcolors.CYAN}{distro} {os_version}\n"
                    f"{bcolors.WHITE}Gestionnaire de paquets: {bcolors.CYAN}{package_manager}\n"
                    f"{bcolors.WHITE}Nombre de paquets installés: {bcolors.CYAN}{num_packages}\n"
                    f"{bcolors.WHITE}Date d'installation du système: {bcolors.CYAN}{install_date}\n"
                    f"{bcolors.WHITE}Durée depuis le démarrage: {bcolors.CYAN}{uptime_duration}{bcolors.ENDC}")
        else:
            return f"{bcolors.WHITE}Système d'exploitation: {bcolors.CYAN}{os_name} {os_version}{bcolors.ENDC}"
    except Exception as e:
        return f"{bcolors.WHITE}Erreur lors de la récupération du nom de la distribution: {bcolors.CYAN}{e}{bcolors.ENDC}"
