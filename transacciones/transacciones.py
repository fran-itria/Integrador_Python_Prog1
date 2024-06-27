from transacciones.funciones.registrar_compra import registrar_compra
from transacciones.funciones.registrar_venta import registrar_venta
from transacciones.funciones.listar_transacciones import listar_transacciones

ruta_transacciones = 'json/transacciones.json'
texto = '''Desea realizar otra acción con las transacciones? 
1: Registrar Compra
2: Registrar Venta
3: Listar transacciones por compras
4: Listar transacciones por ventas
5: Listar transacciones en un rango de fechas
0: Salir
'''

def transacciones(leer_archivo, escribir_archivo, listar_archivo, json, tarea):
    transacciones = leer_archivo(ruta_transacciones, json)
    print('Desea registrar una compra o venta? Coloque el numero de la opción que desea realizar')
    transaccion = int(input('1: Compra \n 2: Venta \n 3: Listar compras \n 4: Listar ventas \n 5: Listar por rango de fecha \n 0: Salir \n'))
    while transaccion != 0:
        match transaccion:
            case 1:
                print('Registrar compra')
                transacciones = registrar_compra(transacciones, json, leer_archivo, escribir_archivo)
                transaccion = escribir_archivo(ruta_transacciones, transacciones, json, texto)
            case 2:
                print('Registrar venta')
                transacciones = registrar_venta(transacciones, json, leer_archivo, escribir_archivo)
                transaccion = escribir_archivo(ruta_transacciones, transacciones, json, texto)
            case 3:
                print('Listar compras')
                listar_transacciones(transacciones, 'Compra', listar_archivo, leer_archivo, json, False, False)
                transaccion = int(input(texto))
            case 4:
                print('Listar ventas')
                listar_transacciones(transacciones, 'Venta', listar_archivo, leer_archivo, json, False, False)
                transaccion = int(input(texto))
            case 5:
                print('Listar por rango de fecha')
                fecha_desde = input('Ingrese la fecha desde la cual desea listar (formato AAAA-MM-DD): ')
                fecha_hasta = input('Ingrese la fecha hasta la cual desea listar (formato AAAA-MM-DD): ')
                listar_transacciones(transacciones, False, listar_archivo, leer_archivo, json, fecha_desde, fecha_hasta)
                transaccion = int(input(texto))
    return int(input(tarea))