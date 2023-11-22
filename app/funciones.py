import json

def obtener_datos_agentes(ruta_archivo='agentes_cloud.json'):
    try:
        with open(ruta_archivo, 'r') as archivo:
            agentes = json.load(archivo)
        
        lista_agentes = []
        for agente in agentes:
            agent_id = agente.get('agentId')
            agent_name = agente.get('agentName')
            location = agente.get('location')

            lista_agentes.append({
                'agentId': agent_id,
                'agentName': agent_name,
                'location': location
            })
       
        return lista_agentes

    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_archivo}")
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON")
        return []

def obtener_agentes_SouthAmerica(ruta_archivo='agentes_cloud.json'):
    try:
        with open(ruta_archivo, 'r') as archivo:
            agentes_cloud_SA = json.load(archivo)
        lista_agentes_SA = []

        paises_deseados = ["Colombia", "Peru", "Chile", "Argentina", "Costa Rica"]

        for agente in agentes_cloud_SA:
            agent_id = agente.get('agentId')
            agent_name = agente.get('agentName')
            location = agente.get('location')

            # Comprobar si la ubicación del agente está en la lista de países deseados
            if any(pais in location for pais in paises_deseados):
                lista_agentes_SA.append({
                    'agentId': agent_id,
                    'agentName': agent_name,
                    'location': location
                })

        return lista_agentes_SA
    except FileNotFoundError:
        print(f"No se encontró el archivo {ruta_archivo}")
        return []
    except json.JSONDecodeError:
        print("Error al leer el archivo JSON")
        return []
# Ejemplo de uso
# agentes = obtener_datos_agentes()
# print(agentes)
