# src/email_sender.py

import win32com.client

def enviar_correo(config, asunto, cuerpo, adjunto=None):
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = ";".join(config["to"])
    mail.CC = ";".join(config["cc"])
    mail.Subject = asunto
    mail.Body = cuerpo

    if adjunto:
        mail.Attachments.Add(adjunto)

    mail.Send()
