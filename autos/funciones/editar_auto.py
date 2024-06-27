from funciones_archivos.buscar import buscar

def editar_auto(vehiculos):
    index_arreglo = buscar(vehiculos, 'id_vehiculo', 'vehiculo', 'editar')
    print('Que desea editar? \n 1: Numero de patente \n 2: Marca \n 3: Modelo \n 4: Tipo \n 5: Año \n 6: Kilometraje \n 7: Precio de compra \n 8: Precio de venta \n 9: Estado \n 0: Salir')
    accion = int(input())
    while accion != 0:
        match accion:
            case 1:
                vehiculos[index_arreglo]['numero_patente'] = input('Ingrese el numero de patente: ')
            case 2:
                vehiculos[index_arreglo]['marca'] = input('Ingrese la marca: ')
            case 3:
                vehiculos[index_arreglo]['modelo'] = input('Ingrese el modelo: ')
            case 4:
                vehiculos[index_arreglo]['tipo'] = input('Ingrese el tipo: ')
            case 5:
                vehiculos[index_arreglo]['año'] = int(input('Ingrese el año: '))
            case 6:
                vehiculos[index_arreglo]['kilometraje'] = int(input('Ingrese el kilometraje: '))
            case 7:
                vehiculos[index_arreglo]['precio_compra'] = int(input('Ingrese el precio de compra: '))
            case 8:
                vehiculos[index_arreglo]['precio_venta'] = int(input('Ingrese el precio de venta: '))
            case 9:
                vehiculos[index_arreglo]['estado'] = input('Ingrese el estado: ')
        accion = int(input('¿Desea editar otra propiedad? '))
    print('Vehiculo editado con exito.')
    return vehiculos