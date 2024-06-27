
def buscar(lista, campo, elemento, string):
    id = int(input(f'Ingrese el {campo} del {elemento} a {string}: '))
    index_arreglo = None
    while index_arreglo is None:
        for index, auto in enumerate(lista):
            if(auto[campo] == id):
                index_arreglo = index
                break
        if index_arreglo is None:
            id = int(input('El id ingresado no existe, por favor ingrese un id valido: '))
    return index_arreglo