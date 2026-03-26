# src/config.py

from datetime import datetime

RUTA_GUARDADO = "./output"

TRANSACCION = "TRANSACCION_LOGISTICA"
LISTADO_CEDIS = [1001, 1002, 1003]

HOY = datetime.now().strftime('%d.%m.%Y')

EMAIL_CONFIG = {
    "to": ["usuario@empresa.com"],
    "cc": ["analista@empresa.com"]
}
