
def crear_auto(vehiculos):
    numero_patente = input('Ingrese el numero de patente: ')
    marca = input('Ingrese la marca: ')
    modelo = input('Ingrese el modelo: ')
    tipo = input('Ingrese el tipo: ')
    año = int(input('Ingrese el año: '))
    kilometraje = int(input('Ingrese el kilometraje: '))
    precio_compra = int(input('Ingrese el precio de compra: '))
    precio_venta = int(input('Ingrese el precio de venta: '))
    estado = input('Ingrese el estado (Disponible, Reservado o Vendido): ')
    if len(vehiculos) == 0:
        id = 1
    else:
        id = vehiculos[-1]['id_vehiculo'] + 1 
    vehiculos.append({
        'id_vehiculo': id,
        'numero_patente':numero_patente,
        'marca':marca,
        'modelo':modelo,
        'tipo':tipo,
        'año': año,
        'kilometraje':kilometraje,
        'precio_compra':precio_compra,
        'precio_venta':precio_venta,
        'estado':estado
    })
    return vehiculos
