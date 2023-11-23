#!/bin/bash

# Obtener el directorio donde se encuentra el script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"


if [[ ":$PATH:" != *":$SCRIPT_DIR:"* ]]; then
    # Agregar el directorio del script a PATH en .bash_profile o .zshrc
    echo "export PATH=\$PATH:$SCRIPT_DIR" >> ~/.zshrc
    echo "Directorio del script agregado al PATH. Por favor, reinicia tu terminal."
    exit 0
fi


# Cambiar al directorio del script
cd "$SCRIPT_DIR"

# Ejecutar tu aplicación Flask
python run.py