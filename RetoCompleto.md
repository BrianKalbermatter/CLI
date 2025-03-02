/*
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 
 
 *API
 * - Algunas herramientas clave para tu aprendizaje:

    FastAPI → Para crear APIs REST rápidas y eficientes.

    Typer → Basado en Click, ideal para crear interfaces CLI en Python.
    
    Requests → Para consumir APIs desde CLI.
    
    SQLite o PostgreSQL → Para almacenamiento de datos.
 
 */


UTN
129 alumnado interno
Luis Seniquel
1.3 comision



Documentación para aprender Ubuntu y Python CLI

Aquí tienes los mejores recursos para aprender:
📌 Ubuntu

🔗 Documentación oficial de Ubuntu:
👉 https://ubuntu.com/tutorials

🔗 Comandos básicos de Linux/Ubuntu:
👉 https://ss64.com/bash/

🔗 Guía de línea de comandos en Linux:
👉 https://linuxcommand.org/
📌 Python CLI y desarrollo en Ubuntu

🔗 Documentación oficial de Python:
👉 https://docs.python.org/es/

🔗 Aprender a usar argparse (para crear CLIs avanzadas en Python):
👉 https://docs.python.org/3/library/argparse.html

🔗 Crear herramientas CLI con Click (más fácil que argparse):
👉 https://click.palletsprojects.com/en/8.1.x/

🔗 Guía de programación en Python en Linux:
👉 https://realpython.com/python-command-line-interfaces-cli/
🔹 ¿Cómo empezar con Python CLI en Ubuntu?

1️⃣ Instalar Python (ya viene en Ubuntu, pero puedes actualizarlo):

sudo apt update && sudo apt install python3 python3-pip

2️⃣ Ejecutar scripts desde la terminal:

python3 mi_script.py

3️⃣ Crear un CLI con argparse:

import argparse

parser = argparse.ArgumentParser(description="Programa de ejemplo en CLI")
parser.add_argument("nombre", help="Tu nombre")
args = parser.parse_args()

print(f"Hola, {args.nombre}!")

Ejecutar:

python3 script.py Brian

4️⃣ Aprender bash y comandos de Linux para automatizar tareas.
🔹 Conclusión

Si quieres aprender Ubuntu + Python CLI, sigue esta ruta:
✅ Aprender comandos básicos de Ubuntu.
✅ Crear scripts Python simples en CLI con sys.argv o argparse.
✅ Explorar herramientas CLI más avanzadas (Click, Typer).
✅ Automatizar tareas en Ubuntu con Python + Bash.

Si necesitas ayuda con un tema específico, dime. 🚀🔥


