
def listar_archivo(lista, campo, autos_o_clientes, id_string, id_buscar):
    # SI NO SE INGRESA UN ID, SE LISTAN LOS ELEMENTOS SEGUN EL CAMPO INGRESADO
    if not id_string:
        lista_filtrada = []
        filtro = input(f'Ingrese el {campo} por el cual listar: ')
        if campo == 'precio_compra' or campo == 'precio_venta':
            filtro = int(filtro)
        # BUSQUEDA POR NOMBRE Y APELLIDO
        if 'y' in campo:
            nombre = filtro.split(' ')[0]
            apellido = filtro.split(' ')[1]
            for elemento in lista:
                if elemento['nombre'] == nombre and elemento['apellido'] == apellido:
                    lista_filtrada.append(elemento)   
        # BUSQUEDA POR CAMPO 
        else :
            for elemento in lista:
                if elemento[campo] == filtro:
                    lista_filtrada.append(elemento)
        if len(lista_filtrada) == 0:
                print(f'No se encontraron {autos_o_clientes} con ese {campo}')
        else:
            for elemento in lista_filtrada:
                if autos_o_clientes == 'autos': 
                    print(f'''
                          Vehiculo: {elemento["id_vehiculo"]}
                          Patente: {elemento["numero_patente"]}
                          Marca: {elemento["marca"]} 
                          Modelo: {elemento["modelo"]}
                          Tipo: {elemento["tipo"]}
                          Precio de compra: {elemento["precio_compra"]}
                          Precio de venta: {elemento["precio_venta"]}
                          ''')
                else:
                    print(f'''
                          Cliente: {elemento["id_cliente"]}
                          Nombre: {elemento["nombre"]}
                          Apellido: {elemento["apellido"]}
                          Documento: {elemento["documento"]}
                          Dirección: {elemento["direccion"]}
                          Teléfono: {elemento["telefono"]}
                          Correo electrónico: {elemento["email"]}
                          ''')
    # BUSQUEDA POR ID
    else:
        for elemento in lista:
            if id_string == 'id_cliente' and elemento['id_cliente'] == id_buscar:
               return elemento
            elif id_string == 'id_vehiculo' and elemento['id_vehiculo'] == id_buscar:
                return elemento