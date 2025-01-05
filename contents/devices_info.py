import os
from .colors import BColors as bcolors


def get_connected_devices():
    return f"{bcolors.WHITE}" + os.popen("lsusb").read().strip() + f"{bcolors.ENDC}"
