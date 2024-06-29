from clientes.funciones.crear_cliente import crear_cliente
ruta_clientes = 'json/clientes.json'

def registro_cliente(leer_archivo, escribir_archivo, json):
    clientes = leer_archivo(ruta_clientes, json)
    print('\n Listado de clientes')
    if(len(clientes) == 0):
        print('No hay clientes registrados, registre el cliente')
        clientes = crear_cliente(clientes)
        escribir_archivo(ruta_clientes, clientes, json, False)
        id_cliente = clientes[-1]['id_cliente']
    else:
        for cliente in clientes:
            print(f"id del cliente {cliente['id_cliente']}: {cliente['nombre']} {cliente['apellido']}")
        id_cliente = int(input('Coloque el id del cliente si ya se encuentra registrado o si desea registrar un nuevo cliente coloque 0: '))
        cliente_encontrado = False
        while not cliente_encontrado and id_cliente != 0:
            for cliente in clientes:
                if cliente['id_cliente'] == id_cliente:
                    cliente_encontrado = True
                    break
            if not cliente_encontrado:
                id_cliente = int(input('Cliente no encontrado, coloque otro id o coloque 0 para registrarlo: '))
        if(id_cliente == 0):
            print('\n Registre al cliente')
            clientes = crear_cliente(clientes)
            escribir_archivo(ruta_clientes, clientes, json, False)
            id_cliente = clientes[-1]['id_cliente']
    return id_cliente