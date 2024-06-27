from clientes.funciones.crear_cliente import crear_cliente
from clientes.funciones.editar_cliente import editar_cliente
from funciones_archivos.eliminar import eliminar

ruta_clientes = 'json/clientes.json'
texto = '''Desea realizar otra acción con los clientes? 
1: Crear 
2: Editar 
3: Eliminar 
4: Listar por documento 
5: Listar por nombres 
6: Listar por apellido
7: Listar por nombre y apellido
0: Salir
'''
autos_o_clientes = 'clientes'

def clientes(leer_archivo, escribir_archivo, listar_archvo, json, tarea):
    clientes = leer_archivo(ruta_clientes, json)
    print('Que desea hacer con los clientes? \n 1: Crear \n 2: Editar \n 3: Eliminar \n 4: Listar por documento \n 5: Listar por nombres \n 6: Listar por apellido \n 7: Listar por nombre y apellido \n 0: Salir')
    accion_cliente = int(input())
    while accion_cliente != 0:
        match accion_cliente:
            case 1:
                print('Crear cliente')
                clientes = crear_cliente(clientes)
                accion_cliente = escribir_archivo(ruta_clientes, clientes, json, texto)
            case 2:
                print('Editar cliente')
                clientes = editar_cliente(clientes)
                accion_cliente = escribir_archivo(ruta_clientes, clientes, json, texto)
            case 3:
                print('Eliminar cliente')
                clientes = eliminar(clientes, 'id_cliente', 'cliente')
                accion_cliente = escribir_archivo(ruta_clientes, clientes, json, texto)
            case 4:
                print('Listar por documento')
                listar_archvo(clientes, 'documento', autos_o_clientes, False, False)
                accion_cliente = int(input(texto))
            case 5:
                print('Listar por nombres')
                listar_archvo(clientes, 'nombre', autos_o_clientes, False, False)
                accion_cliente = int(input(texto))
            case 6:
                print('Listar por apellido')
                listar_archvo(clientes, 'apellido', autos_o_clientes, False, False)
                accion_cliente = int(input(texto))
            case 7:
                print('Listar por nombre y apellido')
                listar_archvo(clientes, 'nombre y apellido', autos_o_clientes, False, False)
                accion_cliente = int(input(texto))
    return int(input(tarea))