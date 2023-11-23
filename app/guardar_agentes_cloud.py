import requests
import json
from .config import AUTH_TOKEN, EMAIL

def guardar_agentes_cloud():
    url = "https://api.thousandeyes.com/v6/agents.json?agentTypes=CLOUD"
    headers = {"Content-Type": "application/json"}
    auth = (EMAIL,AUTH_TOKEN)

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        agentes_cloud = response.json()['agents']
        with open("agentes_cloud.json", "w") as archivo:
            json.dump(agentes_cloud, archivo)
        print("Agentes CLOUD guardados en 'agentes_cloud.json'")
    else:
        print("Error al obtener los agentes CLOUD:", response.status_code)

def main():
    parser = argparse.ArgumentParser(description='Gestión de Agentes Cloud en ThousandEyes')
    parser.add_argument('--actualizar-agentes', action='store_true', help='Actualiza la lista de agentes CLOUD y guarda en archivo JSON')

    args = parser.parse_args()


    if args.actualizar_agentes:
        guardar_agentes_cloud()
    else:
        # Si no se utiliza el comando, igualmente actualiza la lista al iniciar
        guardar_agentes_cloud()
        app.run(debug=True)  # O cualquier otra configuración con la que inicies Flask

if __name__ == '__main__':
    main()