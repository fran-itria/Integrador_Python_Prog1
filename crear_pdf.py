from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def crear_pdf(nombre_archivo, titulo, lista):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    ancho, alto = letter

    def nueva_pagina(titulo, es_primera_pagina=False):
        if not es_primera_pagina:
            c.showPage()
        c.setFont("Helvetica-Bold", 18)
        c.drawString(30, alto - 50, titulo)
        c.setFont("Helvetica", 12)
        return 60  # Restablecer la resta para la nueva página

    # Título y configuración inicial para la primera página
    resta = nueva_pagina(titulo, es_primera_pagina=True)
    for i in range(len(lista)):
        if alto - resta < 100:  # Verificar si queda espacio suficiente para más contenido
            resta = nueva_pagina(titulo)  # Comenzar una nueva página si es necesario
        for clave, valor in lista[i].items():
            if isinstance(valor, dict):
                resta += 20
                c.drawString(30, alto - resta, f"{clave.capitalize()}:")
                for subclave, subvalor in valor.items():
                    resta += 20
                    c.drawString(30, alto - resta, f"      - {subclave.capitalize()}: {subvalor}")
            else:
                resta += 20
                c.drawString(30, alto - resta, f"{clave.capitalize()}: {valor}")
        resta += 20 
    # Pie de página
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(30, 50, "Reporte generado por el sistema de gestión de concesionaria.")

    c.showPage()
    c.save()