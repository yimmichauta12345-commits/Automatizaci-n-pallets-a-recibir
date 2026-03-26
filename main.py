# src/main.py

from config import *
from sap_client import *
from excel_utils import *
from email_sender import *
from utils import *

def main():

    print("🚀 Iniciando automatización ERP")

    limpiar_carpeta(RUTA_GUARDADO)

    session = conectar_sap()
    abrir_transaccion(session, TRANSACCION)

    dataframes = []

    for cedi in LISTADO_CEDIS:
        print(f"Procesando CEDI: {cedi}")

        ejecutar_consulta(session)

        # 🔽 Aquí iría la lógica real de captura (mock para demo)
        import pandas as pd
        df = pd.DataFrame({
            "CEDI": [cedi],
            "valor": [100]
        })

        dataframes.append(df)

    df_final = consolidar_dataframes(dataframes)

    if df_final is not None:
        archivo = generar_reporte(df_final, RUTA_GUARDADO)

        enviar_correo(
            EMAIL_CONFIG,
            "Reporte automático",
            "Adjunto reporte generado automáticamente",
            archivo
        )

        print("✅ Proceso completado")

if __name__ == "__main__":
    main()
