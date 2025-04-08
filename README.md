# Docker First Steps

Este proyecto es una introducción al uso de Docker, proporcionando una configuración básica para una aplicación Python. Incluye ejemplos de cómo estructurar un proyecto con Docker y cómo utilizar `pre-commit` para mantener la calidad del código.

## Estructura del Proyecto

- `app/`: Directorio que contiene el código fuente de la aplicación Python.
  - `__init__.py`: Archivo de inicialización del paquete.
  - `main.py`: Script principal de la aplicación.
- `.gitignore`: Especifica los archivos y directorios que Git debe ignorar.
- `.pre-commit-config.yaml`: Configuración para los hooks de `pre-commit`.
- `docker-compose.yml`: Archivo de configuración para Docker Compose.

## Prerrequisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [pre-commit](https://pre-commit.com/)

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/jcav67/docker_first_steps.git
   cd docker_first_steps

2. **Instalar pre-commit**:
    ```bash
    pre-commit install

## Uso
Construir y ejecutar la aplicación con Docker Compose
Para construir y ejecutar la aplicación en contenedores Docker:


        docker-compose up --build


Esto levantará los servicios definidos en docker-compose.yml.

Detener la aplicación
Para detener los servicios en ejecución:


        docker-compose down

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue los pasos a continuación para contribuir:

Haz un fork del proyecto.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y confirma tus commits (git commit -m 'Añadir nueva funcionalidad').

Empuja tus cambios al repositorio remoto (git push origin feature/nueva-funcionalidad).

Abre una solicitud de extracción.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
