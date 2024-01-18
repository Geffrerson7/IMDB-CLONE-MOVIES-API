# IMDB-CLONE-MOVIES-API

## Descripción
API para registrar peliculas.

## Instalación local

Clonar el repositorio

```bash
 $ git clone https://github.com/Geffrerson7/IMDB-CLONE-MOVIES-API.git
```

Ir al directorio al proyecto

```bash
 $ cd IMDB-CLONE-MOVIES-API
```

Crear un entorno virtual

```sh
$ virtualenv venv
```

Activar el entorno virtual
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego, realizamos las migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```
Y navegar a
```sh
http://127.0.0.1:8000/
```

## Instalación en Docker del proyecto

Clonar el repositorio

```bash
$ git clone https://github.com/Geffrerson7/IMDB-CLONE-MOVIES-API.git
```

Ir al directorio al proyecto

```bash
$ cd IMDB-CLONE-MOVIES-API
```

Ejecutar el comando
```sh
$ docker-compose up
```

Y navegar a
```sh
http://127.0.0.1:8000/
```

## Tecnologías y lenguajes utilizados

* **Python** (v. 3.11.2) [Source](https://www.python.org/)
* **Django** (v. 4.2.1)  [Source](https://www.djangoproject.com/)
* **Django Rest Framework** (v. 3.14.0) [Source](https://www.django-rest-framework.org/)
* **django-cors-headers** (v. 4.0.0) [Source](https://pypi.org/project/django-cors-headers/)
* **Simple JWT** (v. 5.2.2) [Source](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* **drf-yasg** (v. 1.21.5) [Source](https://drf-yasg.readthedocs.io/en/stable/)
* **psycopg2** (v. 2.9.6) [Source](https://pypi.org/project/psycopg2/)
* **Docker** (v. 3.8) [Source](https://docs.docker.com/)


## Author
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)