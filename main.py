import requests

def crear_etiqueta(email, auth_token, etiqueta_nombre, test_ids):
    # Define los datos necesarios
    url = "https://api.thousandeyes.com/v6/groups/tests/new"
    data = {
        "name": etiqueta_nombre,
        "tests": [{"testId": test_id} for test_id in test_ids]
    }
    headers = {"Content-Type": "application/json"}
    auth = (email, auth_token)

    # Realiza la solicitud POST
    response = requests.post(url, json=data, headers=headers, auth=auth)

    # Verifica si el código de estado es 200 o 201 (éxito)
    if response.status_code in (200, 201):
        print("Etiqueta creada exitosamente.")
    else:
        print(f"Error al crear la etiqueta. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)


def crear_prueba_http(email, auth_token, agent_id, test_name, url):
    url = "https://api.thousandeyes.com/v6/tests/http-server/new.json"
    data = {
        "interval": 300,  #5 minutos por defecto
        "agents": [{"agentId": agent_id}],
        "testName": test_name,
        "url": url,
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = (email, auth_token)

    # Realiza la solicitud POST
    response = requests.post(url, json=data, headers=headers, auth=auth)

    # Verifica si el código de estado es 200 o 201 (éxito)
    if response.status_code in (200, 201):
        print("Prueba HTTP creada exitosamente.")
        print(response)
    else:
        print(f"Error al crear la prueba. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)

def obtener_agentes(email, auth_token, agent_types=None):
    # Define la URL base para obtener la lista de agentes
    base_url = "https://api.thousandeyes.com/v6/agents.json"

    # Define los parámetros de consulta (querystring) si se proporcionan agent_types
    params = {}
    if agent_types:
        params["agentTypes"] = agent_types

    # Define las cabeceras de autenticación
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    auth = (email, auth_token)

    # Realiza la solicitud GET con los parámetros de consulta
    response = requests.get(base_url, params=params, headers=headers, auth=auth)

    # Verifica si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        data = response.json()
        return data  # Devuelve la lista de agentes en formato JSON
    else:
        print(f"Error al obtener la lista de agentes. Código de estado: {response.status_code}")
        print("Mensaje de error:", response.text)
        return None

# Solicitar al usuario que ingrese sus datos
#email = input("Ingresa tu dirección de correo electrónico: ")
#auth_token = input("Ingresa tu credencial (AuthToken): ")

etiqueta_nombre = input("Ingresa el nombre de la etiqueta: ")
test_ids = input("Ingresa los IDs de los tests (separados por comas): ").split(',')

agent_types= "CLOUD"
# Llama a la función para crear la etiqueta
#crear_etiqueta(email, auth_token, etiqueta_nombre, test_ids)
print(obtener_agentes(email,auth_token,agent_types))