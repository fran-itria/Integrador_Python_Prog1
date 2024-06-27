import datetime

def crear_transaccion(transacciones, id_cliente, id_vehiculo, tipo_transaccion):
    if len(transacciones) == 0:
        id_transaccion = 1
    else:
        id_transaccion = transacciones[-1]['id_transaccion'] + 1
    print('\n Registro de transacción')
    fecha = input('Fecha de la transacción (AAAA-MM-DD): ')
    monto = int(input('Monto de la transacción: '))
    observaciones = input('Observaciones de la transacción: ')
    transaccion = {
        'id_transaccion': id_transaccion,
        'id_cliente': id_cliente,
        'id_vehiculo': id_vehiculo,
        'tipo_transaccion': tipo_transaccion,
        'fecha': fecha,
        'monto': monto,
        'observaciones': observaciones
    }
    transacciones.append(transaccion)
    return transacciones