function generarComentario() {
    var comentario = obtenerComentarioAleatorio();

    document.getElementById('comment').textContent = comentario;
  }

  function obtenerComentarioAleatorio() {

    var resennas = [
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
    ];

    var indiceAleatorio = Math.floor(Math.random() * resennas.length);

    return resennas[indiceAleatorio];
  }