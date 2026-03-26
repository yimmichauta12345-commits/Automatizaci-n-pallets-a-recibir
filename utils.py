# src/utils.py

import os

def limpiar_carpeta(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)
        return

    for archivo in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)
