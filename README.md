# Quick-test
Technical test - Quick

# Proyecto de Prueba Técnica

Este proyecto está construido con **Django** y **Django REST Framework**, utilizando **PostgreSQL** como base de datos. A continuación, encontrará las instrucciones para configurarlo y ejecutarlo en su máquina local.

## Requisitos Previos

Antes de comenzar, asegúrese de tener instalado lo siguiente:

- **Python 3.8 o superior**
- **PostgreSQL**
- **Git** (opcional, pero recomendado para clonar el repositorio)

## Configuración Inicial

Siga los pasos a continuación para preparar el entorno del proyecto:

### 1. Clonar el repositorio

Primero, descargue el proyecto desde el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crear un entorno virtual

Se recomienda usar un entorno virtual para manejar las dependencias de forma aislada. Para crear uno, ejecute:

```bash
python -m venv venv
```

Luego, active el entorno virtual:

- En windows

```bash
venv\Scripts\activate
```

- En linux

```bash
source venv/bin/activate
```   

### 3. Instalar dependencias

Con el entorno virtual activado, instale las dependencias del proyecto ejecutando:

```bash
pip install -r requirements.txt
```
Si desea instalar las dependencias manualmente, puede ejecutar:

```bash
pip install djangorestframework==3.15.2
pip install djangorestframework_simplejwt==5.4.0
pip install psycopg2-binary==2.9.10
```


