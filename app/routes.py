from app import app
from flask import render_template, request, redirect, url_for
from app.api_handler import listar_etiquetas, existe_etiqueta_dragonfly, obtener_agentes, crear_prueba_http
from app.funciones import obtener_datos_agentes, obtener_agentes_SouthAmerica


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listar_etiquetas', methods=['GET', 'POST'])
def listar_etiquetas_ruta():

    if request.method == 'POST':
        accion = request.form.get('accion')
        print(accion)
        if accion == 'listar_etiquetas':
            etiquetas = listar_etiquetas()
            return render_template('labels.html', etiquetas=etiquetas)

        elif accion == 'validar_dragonfly':
            dragon_etiqueta = existe_etiqueta_dragonfly()
            return render_template('index.html', etiqueta_mensaje=dragon_etiqueta)

    # Esta línea se ejecutará si no es una solicitud POST o si 'accion' no es ninguno de los valores esperados
    return render_template('index.html')


@app.route('/listar_agentes', methods=['POST'])
def listar_agentes_ruta():

    if request.method == 'POST':
        agentes_enterprise = obtener_agentes()
        agentes_cloud = obtener_agentes_SouthAmerica()
        return render_template('enterprise_table.html', agentes_enterprise=agentes_enterprise, agentes_cloud=agentes_cloud)
    # Lógica para listar agentes
    return render_template('index.html')


@app.route('/agentes_cloud_tabla', methods=['GET','POST'])
def agentes_cloud_ruta():
    cloud_agents = obtener_datos_agentes()
    # Lógica para crear prueba HTTP
    return render_template('cloud_table.html', cloud_agents=cloud_agents)

@app.route('/crear_prueba_http', methods=['POST'])
def crear_prueba_http_ruta():
     # Recoger los datos del formulario
    agent_ids = request.form.get('agent_ids')
    urls = request.form.get('urls')
    dragonfly = 'dragonfly' in request.form

    # Separar los IDs de los agentes y las URLs
    lista_agent_ids = [int(id.strip()) for id in agent_ids.split(',')]
    lista_urls = [url.strip() for url in urls.split(',')]

    mensajes_pruebas = []
    for i, url in enumerate(lista_urls, start=1):
        resultado_prueba = crear_prueba_http(lista_agent_ids, f"Test_{url}", url, dragonfly)
        if resultado_prueba:
            # Si la función devuelve un mensaje, asumimos que es el mensaje de éxito
            mensaje_prueba = f"\n- Prueba {i}: {resultado_prueba}\n"
            mensajes_pruebas.append(mensaje_prueba)

    mensaje_resultado = "Se ha creado lo siguiente:\n" +"\n"+ "\n".join(mensajes_pruebas)
    return render_template('test_created.html', mensaje_resultado=mensaje_resultado)