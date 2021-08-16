
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

## 📝 Tabla de contenidos

- [Descripción](#about)
- [Comenzar](#getting_started)
- [Uso](#usage)
- [Construido usando](#built_using)
- [Listado de tareas](#todo)
- [Autor](#authors)

## 🧐 Descripción <a name = "about"></a>

Prueba Técnica que consiste en realizar una lista de tareas

## 🏁 Comenzar <a name = "getting_started"></a>
Esta lista de instrucciones permitaran realizar una lista del proyecto en la maquina local para propositos de desarrollo y evaluación

### requisitios previos

- tener instalado docker
- tener instalado docker-compose en una versión igual a superior a 1.25

### Instalación

- copiar/renombrar el archivo de variables de entorno a un archivo de nombre ´.env´ o por medio del siguiente comando ´cp .env.example .env´

- construir las imagenes por medio del comando 'docker-compose build'
- levantar las imagenes por medio del comando 'docker-compose up -d'

el servicio levantará las imagenes del servicio de django y de postgres


## 🔧 Correr Tests <a name = "tests"></a>

Para lanzar los test necesitas usar el siguiente comando

- docker-compose run --rm django sh -c 'python manage.py test' 


### Test de estilo de código

Este proyecto fue desarrollado siguiendo el estilo de código sugerido por pep8,
para la cuál se utiliza la libreria flake8.

Para lanzar los test de estilo de código se utiliza el siguiente comando

- docker-compose run --rm django sh -c 'flake8'

## 🎈 Uso <a name="usage"></a>




## ⛏️ Construido usando <a name = "built_using"></a>

- [Postgresql](https://www.postgresql.org/) - Database
- [Python](https://www.python.org/) - Languaje
- [Django](https://www.djangoproject.com/) - Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Framework


## 🚀 Listado de Tareas <a name = "todo"></a>
Se requiere hacer una app para registrar tareas como se muestra a continuación
Escribe un REST API en Django para suplir los siguientes requerimientos
* Los usuarios se deben autenticar
* Las tareas son privadas. Solo las puede administrar su dueño
* Los usuarios pueden agregar, editar, eliminar y marcar como completa/incompleta las tareas
* El listado de tareas debe ser paginado
* Agregar validaciones, como no aceptar tareas sin descripción, etc
* Buscar por descripción
* Escribir test unitarios en el primer commit

## ✍️ Autor <a name = "authors"></a>

- [@daecazu](https://github.com/daecazu) - desarrollador



