from transacciones.funciones.registro_cliente import registro_cliente
from transacciones.funciones.crear_transaccion import crear_transaccion 

def registrar_venta(transacciones, json, leer_archivo, escribir_archivo):
    #  REGISTRO DE CLIENTE 
    id_cliente = registro_cliente(leer_archivo, escribir_archivo, json)
    # SELECCION DE VEHICULO
    print('\n Seleccione el vehículo que se va a vender')
    vehiculos = leer_archivo('json/vehiculos.json', json)
    for vehiculo in vehiculos:
        print(f"id del vehiculo {vehiculo['id_vehiculo']}: {vehiculo['marca']} {vehiculo['modelo']} {vehiculo['año']}")
    id_vehiculo = int(input('Seleccione el id del vehículo: '))
    # COMPROBACION DE EXISTENCIA DEL VEHICULO
    vehiculo_encontrado = False
    while not vehiculo_encontrado:
        for vehiculo in vehiculos:
            if vehiculo['id_vehiculo'] == id_vehiculo:
                vehiculo_encontrado = True
                vehiculo['estado'] = 'Vendido'
                escribir_archivo('json/vehiculos.json', vehiculos, json, False)
                break
        if not vehiculo_encontrado:
            print('Vehículo no encontrado')
            id_vehiculo = int(input('Seleccione el id del vehículo: '))
    # REGISTRO DE TRANSACCION
    transacciones = crear_transaccion(transacciones, id_cliente, id_vehiculo, 'Venta')
    return transacciones
    