def escribir_archivo(ruta, contenido, json, texto):
    with open(ruta, 'w', encoding='utf-8') as archivo:
        if json:
            json.dump(contenido, archivo, indent=4, ensure_ascii=False)
        else:
            archivo.write(contenido)
    if texto: 
        return int(input(texto))