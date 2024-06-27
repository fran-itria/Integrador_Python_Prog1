from autos.funciones.crear_auto import crear_auto 
from autos.funciones.editar_auto import editar_auto
from funciones_archivos.eliminar import eliminar

ruta_vehiculos = 'json/vehiculos.json'
texto = '''¿Desea realizar otra accion con los vehiculos? 
1: Crear 
2: Editar 
3: Eliminar 
4: Listar por patente 
5: Listar por marca 
6: Listar por modelo 
7: Listar por precio de compra 
8: Listar por precio de venta 
0: Salir
'''
autos_o_clientes = 'autos'

def autos(leer_archivo, escribir_archivo, listar_archvo, json, tarea):
    vehiculos = leer_archivo(ruta_vehiculos, json)
    print('Que desea hacer con los vehiculos? \n 1: Crear \n 2: Editar \n 3: Eliminar \n 4: Listar por patente \n 5: Listar por marca \n 6: Listar por modelo \n 7: Listar por precio de compra \n 8: Listar por precio de venta \n 0: Salir')
    accion_vehiculo = int(input())
    while accion_vehiculo != 0:
        match accion_vehiculo:
            case 1:
                print('Crear vehiculo')
                vehiculos = crear_auto(vehiculos)
                accion_vehiculo = escribir_archivo(ruta_vehiculos, vehiculos, json, texto)
            case 2:
                print('Editar vehiculo')
                vehiculos = editar_auto(vehiculos)
                accion_vehiculo = escribir_archivo(ruta_vehiculos, vehiculos, json, texto)
            case 3:
                print('Eliminar vehiculo')
                vehiculos = eliminar(vehiculos, 'id_vehiculo', 'vehiculo')
                accion_vehiculo = escribir_archivo(ruta_vehiculos, vehiculos, json, texto)
            case 4:
                print('Listar por patente')
                listar_archvo(vehiculos, 'numero_patente', autos_o_clientes, False, False)
                accion_vehiculo = int(input(texto))
            case 5:
                print('Listar por marca')
                listar_archvo(vehiculos, 'marca', autos_o_clientes, False, False)
                accion_vehiculo = int(input(texto))
            case 6:
                print('Listar por modelo')
                listar_archvo(vehiculos, 'modelo', autos_o_clientes, False, False)
                accion_vehiculo = int(input(texto))
            case 7:
                print('Listar por precio de compra')
                listar_archvo(vehiculos, 'precio_compra', autos_o_clientes, False, False)
                accion_vehiculo = int(input(texto))
            case 8:
                print('Listar por precio de venta')
                listar_archvo(vehiculos, 'precio_venta', autos_o_clientes, False, False)    
                accion_vehiculo = int(input(texto))
    return int(input(tarea))