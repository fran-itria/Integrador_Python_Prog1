from funciones_archivos.buscar import buscar

def editar_cliente(clientes):
   index_arreglo = buscar(clientes, 'id_cliente', 'cliente', 'editar')
   print('Que porpiedad desea editar: \n 1: Nombre \n 2: Apellido \n 3: Documento \n 4: Direccion \n 5: Telefono \n 6: Email \n 0: Salir')
   propiedad = int(input())
   while propiedad != 0:
         match propiedad:
              case 1:
                clientes[index_arreglo]['nombre'] = input('Ingrese el nombre: ')
              case 2:
                clientes[index_arreglo]['apellido'] = input('Ingrese el apellido: ')
              case 3:
                clientes[index_arreglo]['documento'] = input('Ingrese el documento: ')
              case 4:
                clientes[index_arreglo]['direccion'] = input('Ingrese la direccion: ')
              case 5:
                clientes[index_arreglo]['telefono'] = input('Ingrese el telefono: ')
              case 6:
                clientes[index_arreglo]['email'] = input('Ingrese el email: ')
         propiedad = int(input('¿Desea editar otra propiedad? Coloque el numero de la propiedad o 0 para salir.'))
   print('Cliente editado con exito.')
   return clientes
   