"""
TPI - Virtualizacion

Script de diagnostico del entorno virtualizado.

"""

import socket
import platform
import getpass
import sys
from datetime import datetime

def main():

    """Muestra informacion basica del entorno virtualizado."""

    servidor = socket.gethostname()
    usuario = getpass.getuser()
    fecha_hora = datetime.now()

    print("=" * 40)
    print(" TPI - Virtualizacion")
    print("=" * 40)

    print(f"Servidor: {servidor}")
    print(f"Usuario: {usuario}")
    print(f"Fecha y hora: {fecha_hora.strftime('%d/%m/%Y %H:%M:%S')}")

    print(f"Sistema Operativo: {platform.system()} {platform.release()}")
    print(f"Version de Python: {sys.version}")

    ip = socket.gethostbyname(socket.gethostname())

    print(f"Direccion IP: {ip}")
    print("Estado de Red: OK")

    print()
    print("Entorno virtualizado operativo.")
    print("Proyecto academico - Arquitectura y Sistemas Operativos.")
    print("=" * 40)

if __name__ == "__main__":
    main()