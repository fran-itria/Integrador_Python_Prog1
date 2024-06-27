from funciones_archivos.buscar import buscar

def eliminar(lista, campo, elemento):
    index_arreglo = buscar(lista, campo, elemento, 'eliminar')
    lista.pop(index_arreglo)
    print(f'{elemento} eliminado con exito.')
    return lista