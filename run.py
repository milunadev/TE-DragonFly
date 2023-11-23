import argparse
from app.guardar_agentes_cloud import guardar_agentes_cloud
from app.config import AUTH_TOKEN, EMAIL
from app import app
from dotenv import load_dotenv
import os
import webbrowser
from threading import Timer

#Cargando variables de entorno
load_dotenv()
guardar_agentes_cloud()

def abrir_navegador():
    webbrowser.open_new('http://localhost:5000/')

if __name__ == '__main__':
    Timer(1.5, abrir_navegador).start()  # Espera 1.5 segundos para abrir el navegador
    app.run(debug=True)