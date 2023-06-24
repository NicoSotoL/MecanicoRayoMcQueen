//contador
var contadorElemento = document.getElementById('contador');

function actualizarContador(numeroPersonas) {
  contadorElemento.textContent = numeroPersonas;
}

setInterval(function () {
  var numeroOnline = Math.floor(Math.random() * 30) + 1;
  actualizarContador(numeroOnline);
}, 1000);
//lista de sugerencias
var campoBusqueda = document.getElementById('campo-busqueda');
var listaSugerencias = document.getElementById('lista-sugerencias');

campoBusqueda.addEventListener('input', function () {
  var consulta = campoBusqueda.value;

  var sugerencias = obtenerSugerencias(consulta);

  mostrarSugerencias(sugerencias);
});

function mostrarSugerencias(sugerencias) {
  listaSugerencias.innerHTML = '';

  sugerencias.forEach(function (sugerencia) {
    var sugerenciaElemento = document.createElement('li');
    sugerenciaElemento.textContent = sugerencia;

    sugerenciaElemento.addEventListener('click', function () {
      campoBusqueda.value = sugerencia;
      listaSugerencias.innerHTML = '';
    });

    listaSugerencias.appendChild(sugerenciaElemento);
  });

  listaSugerencias.style.width = campoBusqueda.offsetWidth + 'px';
}

document.addEventListener('click', function (event) {
  if (!campoBusqueda.contains(event.target)) {
    listaSugerencias.innerHTML = '';
  }
});

function obtenerSugerencias(consulta) {
  var sugerencias = [];

  if (consulta === 'motor') {
    sugerencias = ['autismo', 'asperger', 'funao'];
  } else if (consulta === 'choche') {
    sugerencias = ['esto es una falta de respeto', 'me dicen waton', 'lo editan con editores de video como camtasia studio, adobe premier'];
  } else if (consulta === 'mecanicos') {
    sugerencias = ['pastero', 'cocainomano', 'weko'];
  }

  return sugerencias;
}

function validarFormulario() {
    var nombre = document.getElementById('nombre').value;
    var telefono = document.getElementById('telefono').value;
    var email = document.getElementById('email').value;
    var fecha = document.getElementById('fecha').value;
    var hora = document.getElementById('hora').value;

    if (nombre.trim() === '' || telefono.trim() === '' || email.trim() === '' || fecha === '' || hora === '') {
        alert('Por favor, completa todos los campos.');
        return false;
    }

    // Validar formato del correo electrónico
    var emailRegex = /^\S+@\S+\.\S+$/;
    if (!emailRegex.test(email)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return false;
    }

    // Validar formato del número de teléfono chileno
    var telefonoRegex = /^[9]{1}[0-9]{8}$/;
    if (!telefonoRegex.test(telefono)) {
        alert('Por favor, ingresa un número de teléfono chileno válido (9 dígitos comenzando con 9).');
        return false;
    }

    // Validar que la fecha sea posterior a la fecha actual
    var fechaActual = new Date();
    var seleccionFecha = new Date(fecha);
    if (seleccionFecha <= fechaActual) {
        alert('Por favor, selecciona una fecha posterior a la fecha actual.');
        return false;
    }

    // Validar formato de la hora (opcional)
    var horaRegex = /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/;
    if (hora.trim() !== '' && !horaRegex.test(hora)) {
        alert('Por favor, ingresa una hora válida en formato HH:mm (24 horas).');
        return false;
    }

    // Redireccionar a otra página si se cumplieron todos los requisitos
    window.location.href = "Index.html";

    return true;
}
