import datetime


def obtener_cliente_vehivulo(leer_archivo, json, listar_archivo, id_cliente, id_vehiculo):
    clientes = leer_archivo('json/clientes.json', json)
    vehiculos = leer_archivo('json/vehiculos.json', json)
    cliente = listar_archivo(clientes, False, False, 'id_cliente', id_cliente)
    vehiculo = listar_archivo(vehiculos, False, False, 'id_vehiculo', id_vehiculo)
    return cliente, vehiculo

def listar_transacciones(transacciones, tipo_transaccion, listar_archivo, leer_archivo, json, fecha_desde, fecha_hasta, id):
    lista_filtrada = []
    # FILTRADO POR TIPO DE TRANSACCION
    if tipo_transaccion:
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
    # FILTRADO POR ID
    if id:
        transaccion_encontrada = False
        while not transaccion_encontrada:
            for transaccion in transacciones:
                if(transaccion['id_transaccion'] == id):
                    detalle = transaccion
                    transaccion_encontrada = True
                    break
            if not transaccion_encontrada:
                id = int(input('Transaccion no encontrada, coloque otro id: '))
        cliente, vehiculo = obtener_cliente_vehivulo(leer_archivo, json, listar_archivo, detalle['id_cliente'], detalle['id_vehiculo'])
        informacion = f'''
            Id de transaccion: {detalle['id_transaccion']}
            Tipo de transacción: {detalle['tipo_transaccion']}
            Fecha: {detalle['fecha']}
            Monto: {detalle['monto']}
            Cliente involucrado: {f'''
                    . Id de cliente: {detalle['id_cliente']}
                    . Nombre y apellido: {cliente['nombre']} {cliente['apellido']}
                    . Documento: {cliente['documento']}
                    . Dirección: {cliente['direccion']}
                    . Teléfono: {cliente['telefono']}
                    . Correo electrónico: {cliente['email']}
                    '''}
            Vehiculo involucrado: {f'''
                    . Id de vehiculo: {detalle['id_vehiculo']}
                    . Patente: {vehiculo['numero_patente']}
                    . Marca: {vehiculo['marca']} 
                    . Modelo: {vehiculo['modelo']}
                    . Tipo: {vehiculo['tipo']} 
                    . Año: {vehiculo['año']} 
                    . Kilometraje: {vehiculo['kilometraje']}
                    . Precio de compra: {vehiculo['precio_compra']}
                    . Precio de venta: {vehiculo['precio_venta']}
                    . Estado: {vehiculo['estado']}
                    '''}
              '''
        print(informacion)
        return [{
            'Id de transaccion': detalle['id_transaccion'],
            'Tipo de transacción': detalle['tipo_transaccion'],
            'Fecha': detalle['fecha'],
            'Monto': detalle['monto'],
            'Cliente involucrado': {
                'Id de cliente': detalle['id_cliente'],
                'Nombre y apellido': f"{cliente['nombre']} {cliente['apellido']}",
                'Documento': cliente['documento'],
                'Dirección': cliente['direccion'],
                'Teléfono': cliente['telefono'],
                'Correo electrónico': cliente['email']
            },
            'Vehiculo involucrado': {
                'Id de vehiculo': detalle['id_vehiculo'],
                'Patente': vehiculo['numero_patente'],
                'Marca': vehiculo['marca'],
                'Modelo': vehiculo['modelo'],
                'Tipo': vehiculo['tipo'],
                'Año': vehiculo['año'],
                'Kilometraje': vehiculo['kilometraje'],
                'Precio de compra': vehiculo['precio_compra'],
                'Precio de venta': vehiculo['precio_venta'],
                'Estado': vehiculo['estado']
            }
        }]
    else:
        for transaccion in lista_filtrada:
            cliente, vehiculo = obtener_cliente_vehivulo(leer_archivo, json, listar_archivo, transaccion['id_cliente'], transaccion['id_vehiculo'])
            print(f''' 
                  Id de transaccion: {transaccion['id_transaccion']}
                  Tipo de transacción: {transaccion['tipo_transaccion']}
                  Fecha: {transaccion['fecha']}
                  Monto: {transaccion['monto']}  
                  Cliente: {f'''
                            . Nombre y apellido: {cliente['nombre']} {cliente['apellido']}
                            . Documento: {cliente['documento']}
                            '''}
                  Vehiculo: {f'''
                            . Marca: {vehiculo['marca']} 
                            . Modelo: {vehiculo['modelo']} 
                            . Patente: {vehiculo['numero_patente']}
                            '''}
                ''')