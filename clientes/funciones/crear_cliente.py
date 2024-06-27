
def crear_cliente(clientes):
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    documento = input('Ingrese el documento: ')
    direccion = input('Ingrese la direccion: ')
    telefono = input('Ingrese el telefono: ')
    email = input('Ingrese el email: ')
    if len(clientes) == 0:
        id = 1
    else:
        id = clientes[-1]['id_cliente'] + 1
    clientes.append({
        'id_cliente': id,
        'nombre': nombre,
        'apellido': apellido,
        'documento': documento,
        'direccion': direccion, 
        'telefono': telefono,
        'email': email
    })
    return clientes