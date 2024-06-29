
from transacciones.funciones.registro_cliente import registro_cliente
from transacciones.funciones.crear_transaccion import crear_transaccion 
from autos.funciones.crear_auto import crear_auto
ruta_vehiculos = 'json/vehiculos.json'

def registrar_compra(transacciones, json, leer_archivo, escribir_archivo):
    # REGISTRO DE CLIENTE
    id_cliente = registro_cliente(leer_archivo, escribir_archivo, json)
    #  REGISTRO DE VEHICULO
    print('\n Registre el vehículo que se va a comprar')
    vehiculos = leer_archivo(ruta_vehiculos, json)
    vehiculo = crear_auto(vehiculos)
    escribir_archivo(ruta_vehiculos, vehiculo, json, False)
    id_vehiculo = vehiculo[-1]['id_vehiculo']
    #  REGISTRO DE TRANSACCION
    transacciones = crear_transaccion(transacciones, id_cliente, id_vehiculo, 'Compra')
    return transacciones