import requests
from .config import AUTH_TOKEN, EMAIL

#etiqueta_nombre = input("Ingresa el nombre de la etiqueta: ")


def crear_prueba_http(agent_ids, test_name, test_url, agregar_dragonfly):
    api_url = "https://api.thousandeyes.com/v6/tests/http-server/new.json"
    
    data = {
        "interval": 300,
        "agents": [{"agentId": agent_id} for agent_id in agent_ids],
        "testName": test_name,
        "url": test_url
    }

    if agregar_dragonfly:
        data["groups"] = [{"name": "Dragonfly", "groupId": 767156, "builtin": 0}]
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = (EMAIL, AUTH_TOKEN)

    response = requests.post(api_url, json=data, headers=headers, auth=auth)

    if response.status_code in (200, 201):
        response_data = response.json()  # Convierte la respuesta JSON en un diccionario
        test_info = response_data.get('test', [])[0]  # Asegúrate de que 'test' es la clave correcta
        nombre = test_info.get('testName')
        agentes = test_info.get('agents', [])
        nombres_agentes = '  |  '.join([agente.get('agentName') for agente in agentes])
        print(nombre, agentes, nombres_agentes)
        mensaje_exito = "Prueba {nombre} creada exitosamente desde los agentes\n: {agentes}".format(
            nombre=nombre, agentes=nombres_agentes)
        print(mensaje_exito)
        return mensaje_exito
    else:
        print(f"Error al crear la prueba. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)
        return f"Mensaje de error: {response.text}"

def listar_etiquetas():
    # Define los datos necesarios
    url = "https://api.thousandeyes.com/v6/groups.json"
    headers = {"Content-Type": "application/json"}
    auth = (EMAIL, AUTH_TOKEN)

    # Realiza la solicitud GET
    response = requests.get(url, headers=headers, auth=auth)

    # Inicializa una lista vacía para almacenar los nombres de las etiquetas
    etiquetas = []

    # Verifica si el código de estado es 200 (éxito)
    if response.status_code == 200:
        # Comprueba si la respuesta no está vacía y contiene 'groups'
        if response.json() and 'groups' in response.json():
            # Itera sobre cada grupo en la lista de 'groups'
            for grupo in response.json()['groups']:
                # Extrae el nombre de cada grupo y lo añade a la lista de etiquetas
                nombre_etiqueta = grupo.get('name', '')  # Usa un valor por defecto si 'name' no existe
                etiquetas.append(nombre_etiqueta)

        # Retorna la lista de nombres de etiquetas
        return sorted(etiquetas)

    else:
        print(f"Error al listar las etiquetas. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)
        return []

def existe_etiqueta_dragonfly():
    url = "https://api.thousandeyes.com/v6/groups.json"
    headers = {"Content-Type": "application/json"}
    auth = (EMAIL, AUTH_TOKEN)

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        if response.json() and 'groups' in response.json():
            etiqueta_existe = any(grupo.get('name', '') == 'Dragonfly' for grupo in response.json()['groups'])
            if etiqueta_existe:
                return "La etiqueta DRAGONFLY YA está creada 😀"
            else:
                creation_response = crear_etiqueta_dragonfly(email, auth_token)
                return creation_response
        return "No se encontraron grupos"
    else:
        print(f"Error al verificar la etiqueta. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)
        return "Error en consulta API"

def crear_etiqueta_dragonfly():
    url = "https://api.thousandeyes.com/v6/groups/tests/new"
    headers = {"Content-Type": "application/json"}
    auth = (EMAIL, AUTH_TOKEN)
    data = {
        "name" : "Dragonfly"
    }
    response = requests.post(url, json=data, headers=headers, auth=auth)

    if response.status_code in (200, 201):
        print("Etiqueta Dragonfly creada exitosamente.")
        return "Etiqueta Dragonfly creada exitosamente 😀"
    else:
        print(f"Error al crear la etiqueta: {response.status_code}")
        print("Mensaje de error:", response.text)
        return f"Mensaje de error: {response.text} 😨"


def obtener_agentes( agent_types='enterprise'):
    # Define la URL base para obtener la lista de agentes
    base_url = "https://api.thousandeyes.com/v6/agents.json"

    # Define los parámetros de consulta (querystring) si se proporcionan agent_types
    params = {}
    if agent_types:
        params["agentTypes"] = 'ENTERPRISE'

    # Define las cabeceras de autenticación
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = (EMAIL, AUTH_TOKEN)

    # Realiza la solicitud GET con los parámetros de consulta
    response = requests.get(base_url, params=params, headers=headers, auth=auth)
    enterprise_agents = []
    # Verifica si la solicitud fue exitosa (código de estado 200)
    print(response.json())
    if response.status_code == 200:
        if response.json() and 'agents' in response.json():
            for agent in response.json()['agents']:
                agent_id = agent.get('agentId')
                agent_name = agent.get('agentName')
                location = agent.get('location')

                enterprise_agents.append({
                'agentId': agent_id,
                'agentName': agent_name,
                'location': location
            })
        return enterprise_agents
    else:
        print(f"Error al obtener la lista de agentes. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)
        return []