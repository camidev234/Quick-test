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
### 4. Configuración de la base de datos

Edite el archivo `settings.py` para configurar su base de datos. Por ejemplo, si está utilizando PostgreSQL, puede modificar los campos en la sección `DATABASES` como sigue:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_la_bd',
        'USER': 'usuario_de_la_bd',
        'PASSWORD': 'contraseña_de_la_bd',
        'HOST': 'localhost',
        'PORT': '5432',       
    }
}
```

### 5. Aplicación de migraciones y seeding inicial

#### Migraciones
Después de configurar la base de datos, aplique las migraciones necesarias para crear las tablas requeridas en la base de datos. Ejecute el siguiente comando:

```bash
python manage.py makemigrations
python manage.py migrate
```
**Seed inicial de datos**
1. Creación de una tipología inicial y usuario administrador
Ejecute el siguiente comando para crear:

- Una tipología llamada Admin.
- Un usuario inicial asociado a esta tipología.
- Permisos asignados a este usuario para que pueda crear nuevas tipologías y gestionar permisos.

```bash
python manage.py users_seed
```

2. Creación de tipologías y permisos preconfigurados (opcional)
Si desea evitar la configuración manual de nuevas tipologías y permisos, puede ejecutar el siguiente comando. Esto generará:

- Todas las tipologías necesarias.
- Permisos predefinidos para un contexto de negocio relacionado con restaurantes.

```bash
python manage.py permissions_seed
```
## 6. Ejecutar servidor

Finalmente, levante el servidor local para probar el proyecto:

```bash
python manage.py runserver
```
Abra su navegador y acceda a http://127.0.0.1:8000.
