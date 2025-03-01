import os

import platform


def close_firefox():

    if platform.system() == "Windows":

        os.system("taskkill /F /IM firefox.exe")

    elif platform.system() == "Linux":

        os.system("killall firefox")

    elif platform.system() == "Darwin":  # Для macOS

        os.system("pkill firefox")

    else:

        print("Unsupported OS")


close_firefox()