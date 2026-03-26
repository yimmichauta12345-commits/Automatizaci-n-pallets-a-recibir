# src/excel_utils.py

import pandas as pd

def consolidar_dataframes(lista_dfs):
    if not lista_dfs:
        return None
    return pd.concat(lista_dfs, ignore_index=True)

def generar_reporte(df, ruta):
    archivo = f"{ruta}/reporte_consolidado.xlsx"
    df.to_excel(archivo, index=False)
    return archivo
