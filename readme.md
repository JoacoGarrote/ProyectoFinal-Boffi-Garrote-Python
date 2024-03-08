# Eventismos

Bienvenido a Eventismos, tu plataforma completa para gestionar y promocionar eventos de manera eficiente.

## Descripción

¡Hola! Somos **Joaquín Garrote y Lautaro Boffi**, y este es nuestro proyecto final para el curso de Python en Coderhouse. Todo lo utilizado en este proyecto es ficticio.

Se trata de Eventismos, un simulador donde se pueden cargar eventos en base a diferentes categorias, con un sistema de comentarios y registro de usuarios.

Para este proyecto hemos utilizado principalmente:
**Python, Django, Bootstrap, HTML y CSS**. 
La mayoría de las vistas fue creada con plantillas predefindas de Bootstrap pero luego retocadas con el fin de mejorar el estilo.

### Reparto de tareas

**Lautaro Boffi:** Programación general de todo el proyecto con Python y Django, se enfocó en la personalización de eventos y en el correcto funcionamiento en la sección de comentarios.

**Joaquín Garrote:** Programación general de todo el proyecto con Python y Django, se enfocó en el enrutado, en mejorar el aspecto visual y testear el funcionamiento de usuarios.


## Funcionalidades clave

- Gestión de eventos por categoría.
- Detalles del evento con descripciones, fechas, ubicaciones y más.
- Registro de usuarios y perfiles customizables.
- Sistema de autenticación y autorización.
- Interfaz de administración para gestionar eventos y usuarios.
- Comentarios y opiniones de los usuarios.


## Instalación

1. <u>Clona este repositorio</u>:

   bash
   git clone https://github.com/JoacoGarrote/ProyectoFinal-Boffi-Garrote-Python

2. <u>Instalar las dependencias, ES POSIBLE que pida la libreria *pytz*</u>:

   pip install -r requirements.txt

3. <u>Realizar las migraciones correspondientes</u>:

   python manage.py makemigrations
   python manage.py migrate

4. <u>Si se desea, puede crear un **superusuario**, aunque hay uno ya creado</u>:

   python manage.py createsuperuser   
o  
   *Usuario*: Superusuario  
   *Contraseña*: 1234
   
4. <u>Por último, iniciar el servidor</u>:

   python manage.py runserver
