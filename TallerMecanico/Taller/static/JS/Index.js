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
