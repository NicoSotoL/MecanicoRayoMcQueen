import random
from .models import Resenna

def generar_resennas_azar(cantidad):
    textos_resennas = [
        "Excelente servicio. ¡Altamente recomendado!",
        "Muy satisfecho con el trabajo realizado.",
        "El personal es amable y profesional.",
        "No quedé conforme con el resultado.",
        "Me sentí decepcionado con la calidad del servicio.",
        "Buena atención al cliente, pero el precio es elevado.",
        "El servicio fue rápido y eficiente.",
        "No volvería a utilizar sus servicios en el futuro.",
        "El trabajo realizado superó mis expectativas.",
        "No tuve una buena experiencia. No lo recomendaría."
    ]

    for _ in range(cantidad):
        texto = random.choice(textos_resennas)
        calificacion = random.randint(1, 5)

        resenna = Resenna(texto=texto, calificacion=calificacion)
        resenna.save()