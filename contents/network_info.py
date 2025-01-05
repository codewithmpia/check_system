import os
import psutil
import socket
from .colors import BColors as bcolors

def get_network_info():
    try:
        ssid = os.popen("iwgetid -r").read().strip()
        connection_type = "Wi-Fi" if ssid else "Câblé"
        network_name = f"Nom du Réseau: {ssid}" if ssid else "Nom du Réseau: Non applicable"
    except Exception as e:
        network_name = f"Erreur lors de la récupération du nom du réseau: {e}"
        connection_type = "Type de Connexion: Non applicable"

    net_io = psutil.net_io_counters()
    ipv4_addresses = []
    ipv6_addresses = []
    mac_addresses = []

    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                ipv4_addresses.append(f"Adresse IP IPv4 ({interface}): {addr.address}")
            elif addr.family == socket.AF_INET6:
                ipv6_addresses.append(f"Adresse IP IPv6 ({interface}): {addr.address}")
            elif addr.family == psutil.AF_LINK:
                mac_addresses.append(f"Adresse MAC ({interface}): {addr.address}")

    return (
        f"{bcolors.WHITE}{network_name}\n"
        f"{bcolors.WHITE}Type de Connexion: {bcolors.CYAN}{connection_type}\n"
        f"{bcolors.WHITE}Adresses IP IPv4:\n" + "\n".join([f"{bcolors.CYAN}{addr}{bcolors.WHITE}" for addr in ipv4_addresses]) + "\n"
        f"{bcolors.WHITE}Adresses IP IPv6:\n" + "\n".join([f"{bcolors.CYAN}{addr}{bcolors.WHITE}" for addr in ipv6_addresses]) + "\n"
        f"{bcolors.WHITE}Adresses MAC:\n" + "\n".join([f"{bcolors.CYAN}{addr}{bcolors.WHITE}" for addr in mac_addresses]) + "\n"
        f"{bcolors.WHITE}Total Octets Envoyés: {bcolors.CYAN}{net_io.bytes_sent / (1024 ** 2):.2f} MB\n"
        f"{bcolors.WHITE}Total Octets Reçus: {bcolors.CYAN}{net_io.bytes_recv / (1024 ** 2):.2f} MB{bcolors.ENDC}"
    )
