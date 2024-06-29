import json
from funciones_archivos.escribir_archivo import escribir_archivo
from funciones_archivos.leer_archivo import leer_archivo
from funciones_archivos.listar import listar_archivo
from autos.autos import autos
from clientes.clientes import clientes
from transacciones.transacciones import transacciones
from crear_pdf import crear_pdf

tarea = int(input('Con que elementos desea operar? \n 1: Vehiculos \n 2: Clientes \n 3: Transacciones \n 0: Salir \n'))
texto = 'Desea operar con otro elemento? \n 1: Vehiculos \n 2: Clientes \n 3: Transacciones \n 0: Salir \n'

while tarea != 0:
    match tarea:
        case 1:
            tarea = autos(leer_archivo, escribir_archivo, listar_archivo, json, texto, crear_pdf)
        case 2:
            tarea = clientes(leer_archivo, escribir_archivo, listar_archivo, json, texto, crear_pdf)
        case 3:
            tarea = transacciones(leer_archivo, escribir_archivo, listar_archivo, json, texto, crear_pdf)
print('Gracias por usar nuestro sistema.')