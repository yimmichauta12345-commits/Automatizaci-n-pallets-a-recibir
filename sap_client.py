# src/sap_client.py

import time
import win32com.client

def conectar_sap():
    SapGuiAuto = win32com.client.GetObject("SAPGUI")
    application = SapGuiAuto.GetScriptingEngine
    connection = application.Children(0)
    session = connection.Children(0)
    return session

def abrir_transaccion(session, transaccion):
    session.findById("wnd[0]/tbar[0]/okcd").text = transaccion
    session.findById("wnd[0]").sendVKey(0)
    time.sleep(2)

def ejecutar_consulta(session):
    session.findById("wnd[0]/tbar[1]/btn[8]").press()
    time.sleep(3)
