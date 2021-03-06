
<h3 align="center">Lista de Tareas</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/daecazu/lista_de_tareas.svg)](https://github.com/daecazu/lista_de_tareas/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/daecazu/lista_de_tareas.svg)](https://github.com/daecazu/lista_de_tareas/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Este proyecto consiste en una API rest que permite tener una lista de tareas para cada usuario del sistema
    <br> 
</p>

## 馃摑 Tabla de contenidos

- [Descripci贸n](#about)
- [Comenzar](#getting_started)
- [Uso](#usage)
- [Construido usando](#built_using)
- [Listado de tareas](#todo)
- [Autor](#authors)

## 馃 Descripci贸n <a name = "about"></a>

Prueba T茅cnica que consiste en realizar una lista de tareas

## 馃弫 Comenzar <a name = "getting_started"></a>
Esta lista de instrucciones permitaran realizar una lista del proyecto en la maquina local para propositos de desarrollo y evaluaci贸n

### requisitios previos

- tener instalado docker
- tener instalado docker-compose en una versi贸n igual a superior a 1.25

### Instalaci贸n

- copiar/renombrar el archivo de variables de entorno `.env.example` a un archivo de nombre `.env` o por medio del siguiente comando `cp .env.example .env`
- construir las imagenes por medio del comando `docker-compose build`
- levantar las imagenes por medio del comando `docker-compose up -d`

el servicio levantar谩 las imagenes del servicio de django y de postgres


## 馃敡 Correr Tests <a name = "tests"></a>

Para lanzar los test necesitas usar el siguiente comando

- `docker-compose run --rm django sh -c 'python manage.py test'` 


### Test de estilo de c贸digo

Este proyecto fue desarrollado siguiendo el estilo de c贸digo sugerido por pep8,
para la cu谩l se utiliza la libreria flake8.

Para lanzar los test de estilo de c贸digo se utiliza el siguiente comando

- `docker-compose run --rm django sh -c 'flake8'`

## 馃巿 Uso <a name="usage"></a>

- Se pueden crear super usuarios usando el comando `docker-compose run --rm django sh -c 'python manage.py createsuperuser'`
- La schema de documentaci贸n del c贸digo fue creado usando OpenAPI/swagger y se encuenta disponibles en dos versiones en la siguientes urls *localhost:8000/documentation/* i/o *localhost:8000/redoc/* 

la API consta de 3 endpoints adicionales
* un endpoint para la creaci贸n de usuarios
* un endpoint para la creaci贸n de Token
* un endopoint que permite operaciones CRUD sobre la creaci贸n de tareas

la busqueda de tareas se debe realizar por medio `http://localhost:8000/api/tasks/?search=descripcion`

## 鉀忥笍 Construido usando <a name = "built_using"></a>

- [Postgresql](https://www.postgresql.org/) - Database
- [Python](https://www.python.org/) - Languaje
- [Django](https://www.djangoproject.com/) - Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework


## 馃殌 Listado de Tareas <a name = "todo"></a>

Se requiere hacer una app para registrar tareas como se muestra a continuaci贸n
Escribe un REST API en Django para suplir los siguientes requerimientos
* Los usuarios se deben autenticar
* Las tareas son privadas. Solo las puede administrar su due帽o
* Los usuarios pueden agregar, editar, eliminar y marcar como completa/incompleta las tareas
* El listado de tareas debe ser paginado
* Agregar validaciones, como no aceptar tareas sin descripci贸n, etc
* Buscar por descripci贸n
* Escribir test unitarios en el primer commit

## 鉁嶏笍 Autor <a name = "authors"></a>

- [@daecazu](https://github.com/daecazu) - desarrollador



