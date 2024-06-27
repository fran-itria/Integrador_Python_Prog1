def leer_archivo(ruta, json):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        if json:
            return json.load(archivo)
        else:
            return archivo.read()