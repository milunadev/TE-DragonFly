@echo off
SET "SCRIPT_DIR=%~dp0"

REM Quitar la última barra invertida
SET "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"

REM Comprobar si el directorio del script está en PATH
echo %PATH% | findstr /C:"%SCRIPT_DIR%" > nul
IF %ERRORLEVEL% NEQ 0 (
    REM Agregar el directorio del script a PATH
    SETX PATH "%PATH%;%SCRIPT_DIR%"
    echo Se ha agregado el directorio del script al PATH.
)

cd /d %SCRIPT_DIR%
REM Ejecutar tu aplicación Flask
python run.py
