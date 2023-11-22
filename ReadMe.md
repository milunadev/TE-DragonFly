Para iniciar la aplicación Flask normalmente (lo cual incluye una actualización automática de los agentes CLOUD):
python run.py
Este comando iniciará la aplicación Flask y realizará automáticamente una actualización de la lista de agentes CLOUD, guardando los datos en un archivo JSON.



Actualización Manual de Agentes CLOUD
Si deseas actualizar la lista de agentes CLOUD sin iniciar la aplicación web, puedes utilizar el siguiente comando:
python run.py --actualizar-agentes
Este comando ejecutará solamente la función de actualización de los agentes CLOUD, almacenando la información actualizada en el archivo JSON correspondiente, sin iniciar el servidor web de Flask.