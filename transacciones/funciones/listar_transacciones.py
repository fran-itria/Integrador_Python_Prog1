import datetime

def listar_transacciones(transacciones, tipo_transaccion, listar_archivo, leer_archivo, json, fecha_desde, fecha_hasta):
    lista_filtrada = []
    # FILTRADO POR TIPO DE TRANSACCION
    for transaccion in transacciones:
        if transaccion['tipo_transaccion'] == tipo_transaccion:
            lista_filtrada.append(transaccion)
    # FILTRADO POR RANGO DE FECHA
    if fecha_desde and fecha_hasta:
        inicio = datetime.datetime.strptime(fecha_desde, '%Y-%m-%d')
        fin = datetime.datetime.strptime(fecha_hasta, '%Y-%m-%d')
        for transaccion in transacciones:
            fecha_transaccion = datetime.datetime.strptime(transaccion['fecha'], '%Y-%m-%d')
            if inicio <= fecha_transaccion <= fin:
                lista_filtrada.append(transaccion)
    for transaccion in lista_filtrada:
        id_cliente = transaccion['id_cliente']
        id_vehiculo = transaccion['id_vehiculo']
        clientes = leer_archivo('json/clientes.json', json)
        vehiculos = leer_archivo('json/vehiculos.json', json)
        cliente = listar_archivo(clientes, False, False, 'id_cliente', id_cliente)
        vehiculo = listar_archivo(vehiculos, False, False, 'id_vehiculo', id_vehiculo)
        print(f''' 
              Id de transaccion: {transaccion['id_transaccion']}
              Tipo de transacción: {transaccion['tipo_transaccion']}
              Cliente: {f'''
                        . Nombre y apellido: {cliente['nombre']} {cliente['apellido']}
                        . Documento: {cliente['documento']}
                        . Teléfono: {cliente['telefono']}
                        . Correo electrónico: {cliente['email']}
                        '''}
              Vehiculo: {f'''
                        . Marca: {vehiculo['marca']} 
                        . Modelo: {vehiculo['modelo']} 
                        . Año: {vehiculo['año']} 
                        . Patente: {vehiculo['numero_patente']}
                        '''}
              Fecha: {transaccion['fecha']}
              Monto: {transaccion['monto']}  
            ''')