from reportlab.pdfgen import canvas

def crear_pdf(nombre_archivo):
    # Crear un objeto canvas (lienzo) para el PDF
    pdf = canvas.Canvas(nombre_archivo)

    # Agregar texto al PDF
    pdf.drawString(100, 750, "¡Hola, mundo!")

    # Guardar el documento PDF
    pdf.save()

if __name__ == "__main__":
    # Nombre del archivo PDF que se va a crear
    nombre_archivo = "ejemplo.pdf"

    # Crear el documento PDF
    crear_pdf(nombre_archivo)

    print(f"El archivo '{nombre_archivo}' se ha creado correctamente.")
